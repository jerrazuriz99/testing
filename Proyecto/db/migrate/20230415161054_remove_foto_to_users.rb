class RemoveFotoToUsers < ActiveRecord::Migration[7.0]
  def change
    remove_column :users, :foto, :string
  end
end
