class CreateRequests < ActiveRecord::Migration[6.0]
  def change
    create_table :requests do |t|
      t.integer :id_solicitud
      t.integer :id_usuario
      t.integer :id_publicacion
      t.string :estado
      t.text :descripcion

      t.timestamps
    end
  end
end
