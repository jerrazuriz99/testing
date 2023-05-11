ActiveAdmin.register Report do
  # See permitted parameters documentation:
  # https://github.com/activeadmin/activeadmin/blob/master/docs/2-resource-customization.md#setting-up-strong-parameters
  #
  # Uncomment all parameters which should be permitted for assignment
  #
  # permit_params :usuario, :contenido, :user_id
  #
  belongs_to :user, optional: true
  permit_params :estado
  # or
  #
  # permit_params do
  #   permitted = [:usuario, :contenido, :user_id]
  #   permitted << :other if params[:action] == 'create' && current_user.admin?
  #   permitted
  # end
end
