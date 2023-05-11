class RemoveIdViajeFromTurnos < ActiveRecord::Migration[6.0]
  def change
    remove_column :turnos, :id_viaje, :integer
  end
end
