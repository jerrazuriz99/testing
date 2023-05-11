class RemoveIdUsuarioFromTurnos < ActiveRecord::Migration[6.0]
  def change
    remove_column :turnos, :id_usuario, :integer
  end
end
