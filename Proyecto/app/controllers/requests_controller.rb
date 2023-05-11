# frozen_string_literal: true

# This class is for the requests controller
class RequestsController < ApplicationController
  before_action :authenticate_user!

  #### READ
  def index
    @requests = Request.all
    @tipo_index = params[:tipo]
    @tipo_lista = params[:tipo_lista]
  end

  def show
    @request = Request.find(params[:id])
  end

  def new
    @turno_id = params[:id_viaje]
    @request = Request.new
  end

  #### UPDATE
  def edit
    @request = Request.find(params[:id])
  end

  def create
    @request = Request.new(request_params_create)
    @request.turno = Turno.find(params[:id_viaje].to_i)
    @request.estado = 'PENDIENTE'
    @request.user = current_user
    if @request.save
      redirect_to requests_index_path, notice: 'Solicitud enviada exitosamente'
    else
      redirect_to requests_create_path(params[:id_viaje]), flash: { errors: @request.errors.full_messages }
    end
  end

  def update
    @request = Request.find(params[:id])
    if request_params_update.key?('descripcion')
      if @request.update(request_params_update)
        redirect_to requests_index_path(tipo: 2, tipo_lista: 0), notice: 'Solicitud editada exitosamente'
      else
        redirect_to requests_edit_path(params[:id]), flash: { errors: @request.errors.full_messages }
      end
    elsif request_params_update.key?('estado')
      if @request.update(request_params_update)
        update_solicitud_turno(@request) if request_params_update[:estado] == 'ACEPTADO'
        redirect_to requests_index_path(tipo: 1, tipo_lista: 0), notice: 'Solicitud editada exitosamente'
      else
        redirect_to requests_edit_path(params[:id]), flash: { errors: @request.errors.full_messages }
      end
    end
  end

  #### DELETE
  def delete
    @request = Request.find(params[:id])
    @turno = Turno.find(@request.turno_id)
    @asientos_actualizado = @turno.cantidad_asientos + 1
    parametros = { 'cantidad_asientos' => @asientos_actualizado }
    if @turno.cantidad_asientos.zero? && (@turno.estado == 'CONFIRMADO')
      parametros = { 'cantidad_asientos' => @asientos_actualizado, 'estado' => 'ACTIVO' }
    end
    @turno.update(parametros)
    @request.destroy

    redirect_to requests_index_path, notice: 'Request eliminado'
  end

  private

  def request_params_create
    params.require(:request).permit(:descripcion, :turno_id)
  end

  def request_params_update
    params.require(:request).permit(:estado, :descripcion)
  end
end

def update_solicitud_turno(request)
  turno = Turno.find(request.turno_id)
  asientos_actualizado = turno.cantidad_asientos - 1
  parametros = { 'cantidad_asientos' => asientos_actualizado }
  parametros = { 'estado' => 'CONFIRMADO', 'cantidad_asientos' => '0' } if asientos_actualizado.zero?
  turno.update(parametros)
  turno
end
