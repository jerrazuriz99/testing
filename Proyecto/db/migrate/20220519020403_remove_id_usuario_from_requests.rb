class RemoveIdUsuarioFromRequests < ActiveRecord::Migration[6.0]
  def change
    remove_column :requests, :id_usuario, :integer
  end
end
