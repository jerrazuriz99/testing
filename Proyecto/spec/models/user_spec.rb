# frozen_string_literal: true

require 'rails_helper'
require 'faker'

RSpec.describe User, type: :model do
  # Usando la gema FactoryBot, revisar la carpeta factories
  before do
    @user = create(:user)
  end

  # Sin usar FactoryBot:
  # before do
  #   @user = User.create(<Incluir aqui el data para los atributos>)
  # end
  #
  # Ojo con la diferencia entre usar create y new al crear una instancia de un modelo. La primera lo guarda
  # en la base de datos (aplica un .save) y el segundo no lo hace. Para decidir si es valido o no un modelo
  # basta con usar new ya que si ocupan create con datos invalidos para el modelo la base de datos se los va
  # a rechazar por las validaciones.

  it 'is valid with valid attributes' do
    expect(@user).to be_valid
  end
end
