class AddEstadoToTurnos < ActiveRecord::Migration[6.0]
  def change
    add_column :turnos, :estado, :string
  end
end
