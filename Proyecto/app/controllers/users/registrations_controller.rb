# frozen_string_literal: true

module Users
  # This class is for the users controller
  class RegistrationsController < Devise::RegistrationsController
    # rubocop:disable Rails/LexicallyScopedActionFilter
    before_action :configure_sign_up_params, only: [:create]
    before_action :configure_account_update_params, only: [:update]
    # rubocop:enable Rails/LexicallyScopedActionFilter

    def sort_resenas(resenas)
      resenas_usuario = []
      cantidad = 0
      acumulado = 0
      existen_resenas = false
      resenas.each do |resena|
        cantidad += 1
        acumulado += resena.calificacion.to_i
        resenas_usuario << resena
      end
      if cantidad != 0
        existen_resenas = true
        promedio = acumulado / cantidad
      end
      [existen_resenas, resenas_usuario, promedio]
    end

    def sort_reportes(reports)
      existen_reportes = false
      reportes_usuario = []
      reports.each do |report|
        reportes_usuario << report
        existen_reportes = true
      end
      [existen_reportes, reportes_usuario]
    end

    def show
      if params[:id].to_i.zero?
        redirect_to '/users/sign_in'
      else
        @user = User.includes(:reports).find(params[:id])
        @resenas = Resena.joins(:turno).where(turnos: { user_id: params[:id] })
        @existen_resenas, @resenas_usuario, @promedio = sort_resenas(@resenas)
        @existen_reportes, @reportes_usuario = sort_reportes(@user.reports)
        @tipo_lista = params[:tipo_lista]
      end
    end

    # GET /resource/sign_up
    # def new
    #   super
    # end

    # POST /resource

    # GET /resource/edit

    # GET /resource/cancel
    # Forces the session data which is usually expired after sign
    # in to be expired now. This is useful if the user wants to
    # cancel oauth signing in/up in the middle of the process,
    # removing all OAuth session data.
    # def cancel
    #   super
    # end

    # protected

    # If you have extra params to permit, append them to the sanitizer.
    def configure_sign_up_params
      devise_parameter_sanitizer.permit(:sign_up, keys: %i[name address description gender phone foto reglas image])
    end

    # If you have extra params to permit, append them to the sanitizer.
    def configure_account_update_params
      devise_parameter_sanitizer.permit(:account_update,
                                        keys: %i[name address description gender phone foto reglas image])
    end

    # The path used after sign up.
    # def after_sign_up_path_for(resource)
    #   super(resource)
    # end

    # The path used after sign up for inactive accounts.
    # def after_inactive_sign_up_path_for(resource)
    #   super(resource)
    # end
  end
end
