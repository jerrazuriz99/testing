# frozen_string_literal: true

# This class is for the reports controller
class ReportsController < ApplicationController
  before_action :authenticate_user!
  def show
    @report = Report.find(params[:id])
  end

  def new
    @report = Report.new
  end

  def create
    @report = Report.new(report_params_create)
    @report.user = current_user
    if @report.save
      redirect_to users_show_path(id: current_user.id), notice: 'Solicitud enviada exitosamente'
    else
      render action: 'new', notice: 'Error al crear solicitud'
    end
  end

  private

  def report_params_create
    params.require(:report).permit(:usuario, :contenido, :estado)
  end
end
