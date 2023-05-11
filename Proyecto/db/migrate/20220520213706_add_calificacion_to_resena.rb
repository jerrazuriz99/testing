class AddCalificacionToResena < ActiveRecord::Migration[6.0]
  def change
    add_column :resenas, :calificacion, :integer
  end
end
