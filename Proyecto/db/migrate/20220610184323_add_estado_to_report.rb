class AddEstadoToReport < ActiveRecord::Migration[6.0]
  def change
    add_column :reports, :estado, :string
  end
end
