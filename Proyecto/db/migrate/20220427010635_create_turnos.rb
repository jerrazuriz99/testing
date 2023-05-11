class CreateTurnos < ActiveRecord::Migration[6.0]
  def change
    create_table :turnos do |t|
      t.integer :id_usuario
      t.integer :cantidad_asientos
      t.string :hora_salida
      t.string :direccion_salida
      t.string :direccion_llegada
      t.string :dia_semana
      t.string :tipo
      t.integer :id_viaje

      t.timestamps
    end
  end
end
