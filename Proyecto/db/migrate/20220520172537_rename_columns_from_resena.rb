class RenameColumnsFromResena < ActiveRecord::Migration[6.0]
  def change
    rename_column :resenas, :turnos_id, :turno_id
    rename_column :resenas, :users_id, :user_id
  end
end
