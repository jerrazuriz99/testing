class AddEspacioToTurno < ActiveRecord::Migration[6.0]
  def change
    add_column :turnos, :espacio, :string
  end
end
