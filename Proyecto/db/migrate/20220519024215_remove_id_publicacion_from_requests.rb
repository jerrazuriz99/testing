class RemoveIdPublicacionFromRequests < ActiveRecord::Migration[6.0]
  def change
    remove_column :requests, :id_publicacion, :integer
  end
end
