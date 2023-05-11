# frozen_string_literal: true

ActiveAdmin.register Turno do
  # See permitted parameters documentation:
  # https://github.com/activeadmin/activeadmin/blob/master/docs/2-resource-customization.md#setting-up-strong-parameters
  #
  # Uncomment all parameters which should be permitted for assignment
  #
  # permit_params :cantidad_asientos, :hora_salida, :direccion_salida, :direccion_llegada,
  # :dia_semana, :tipo, :estado, :user_id
  #
  # or
  #
  # permit_params do
  #   permitted = [:cantidad_asientos, :hora_salida, :direccion_salida, :direccion_llegada,
  # :dia_semana, :tipo, :estado, :user_id]
  #   permitted << :other if params[:action] == 'create' && current_user.admin?
  #   permitted
  # end
end
