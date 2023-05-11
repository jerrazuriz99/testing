class AddReglasToUser < ActiveRecord::Migration[6.0]
  def change
    add_column :users, :reglas, :string
  end
end
