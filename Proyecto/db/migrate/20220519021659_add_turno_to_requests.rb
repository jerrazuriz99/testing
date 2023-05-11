class AddTurnoToRequests < ActiveRecord::Migration[6.0]
  def change
    add_reference :requests, :turno, null: false, foreign_key: true
  end
end
