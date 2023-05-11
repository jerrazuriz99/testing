class AddIdUsuarioSolicitudToRequests < ActiveRecord::Migration[6.0]
  def change
    add_column :requests, :id_usuario_solicitud, :integer
  end
end
