class RemoveCalificacionFromResena < ActiveRecord::Migration[6.0]
  def change
    remove_column :resenas, :calificacion, :float
  end
end
