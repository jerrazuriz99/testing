class CreateResenas < ActiveRecord::Migration[6.0]
  def change
    create_table :resenas do |t|
      t.integer :id_viaje
      t.integer :id_cliente_evaluador
      t.integer :id_cliente_evaluado
      t.text :contenido
      t.float :calificacion

      t.timestamps
    end
  end
end
