class CreateMensajes < ActiveRecord::Migration[6.0]
  def change
    create_table :mensajes do |t|
      t.string :contenido
      t.references :user, null: false, foreign_key: true
      t.references :turno, null: false, foreign_key: true

      t.timestamps
    end
  end
end
