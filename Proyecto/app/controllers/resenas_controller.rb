# frozen_string_literal: true

# This class is for the resenas controller
class ResenasController < ApplicationController
  before_action :authenticate_user!
  #### READ
  def index
    @resenas = Resena.all
    @id_viaje = params[:id_viaje]
  end

  def show
    @resena = Resena.find(params[:id])
    @user_conductor = User.find(@resena.turno.user_id)
  end

  #### CREATE
  def new
    @resena = Resena.new
    @id_viaje = params[:id_viaje]
  end

  #### UPDATE
  def edit
    @resena = Resena.find(params[:id])
  end

  def create
    @resenas_params = params.require(:resena).permit(:contenido, :calificacion, :turno_id, :user_id)
    @resena = Resena.create(@resenas_params)
    @resena.user = current_user
    @resena.turno = Turno.find(@resenas_params['turno_id'])
    if @resena.save
      redirect_to turnos_show_path(id: @resena.turno.id), notice: 'Solicitud enviada exitosamente'
    else
      @id_viaje = @resenas_params['turno_id']
      render action: 'new', notice: 'Error al crear reseña'
    end
  end

  def update
    @resena = Resena.find(params[:id])
    @resenas_params = params.require(:resena).permit(:contenido, :calificacion, :turno_id, :user_id)
    if @resena.update(@resenas_params)
      redirect_to turnos_show_path(id: @resena.turno.id), notice: 'Reseña editada exitosamente'
    else
      render action: 'edit', notice: 'Error al editar reseña'
    end
  end

  #### DELETE
  def delete
    @resena = Resena.find(params[:id])
    @resena.destroy

    redirect_to turnos_show_path(id: @resena.turno.id), notice: 'Reseña eliminado'
  end
end
