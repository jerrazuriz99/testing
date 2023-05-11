class RemoveIdSolicitudFromRequests < ActiveRecord::Migration[6.0]
  def change
    remove_column :requests, :id_solicitud, :integer
  end
end
