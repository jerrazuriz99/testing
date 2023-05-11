class AddFotoToUsers < ActiveRecord::Migration[6.0]
  def change
    add_column :users, :foto, :string
  end
end
