class AddForeignKeys < ActiveRecord::Migration[6.0]
  def change
    add_reference :resenas, :turnos, foreign_key: true
    add_reference :resenas, :users, foreign_key: true
  end
end
