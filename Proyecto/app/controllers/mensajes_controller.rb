# frozen_string_literal: true

# This class is for the requests mensajes
class MensajesController < ApplicationController
  before_action :authenticate_user!
  #### CREATE
  def new
    turnos = Turno.all
    @turnos_usuario = []
    @mensajes_turnos = {}
    @existen_turnos = false
    if current_user && Turno.any?
      @existen_turnos = true
      turnos.each do |turno|
        @turnos_usuario << turno if turno.user_id == current_user.id
        mensajes_turno = Mensaje.where({ turno_id: turno.id })
        existen_mensajes = mensajes_turno.length.positive?
        @mensajes_turnos[turno.id] = { mensajes: mensajes_turno, existen: existen_mensajes }
      end
      solicitudes = Request.where({ user_id: current_user.id, estado: 'ACEPTADO' })

      solicitudes.each do |solicitud|
        @turnos_usuario << Turno.find(solicitud.turno_id)
      end
      @mensaje = Mensaje.new
    end
    @turno_chat = params[:id_turno]
  end

  def create
    @mensajes_params = params.require(:mensaje).permit(:contenido, :turno_id, :user_id)
    @mensaje = Mensaje.create(@mensajes_params)
    @mensaje.user = current_user
    @mensaje.turno = Turno.find(@mensajes_params['turno_id'])
    if @mensaje.save
      redirect_to mensajes_path(id_turno: @mensajes_params['turno_id']), notice: 'Solicitud enviada exitosamente'
    else
      redirect_to mensajes_path(id_turno: @mensajes_params['turno_id']), notice: 'Error al crear mensaje'
    end
  end
end
