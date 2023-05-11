class RemoveIdClienteEvaluadoFromResena < ActiveRecord::Migration[6.0]
  def change
    remove_column :resenas, :id_cliente_evaluado, :integer
  end
end
