class RemoveColumnsFromResenas < ActiveRecord::Migration[6.0]
  def change
    remove_column :resenas, :id_viaje, :integer
    remove_column :resenas, :id_cliente_evaluador, :integer
  end
end
