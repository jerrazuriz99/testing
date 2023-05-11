require 'test_helper'

class UserTest < ActiveSupport::TestCase
  # Usando FactoryBot, mover los archivos de spec/factories a test/factories en caso de ocupar MiniTest
  def setup
    @user = create(:user)
  end

  # Sin FactoryBot:
  # def setup
  #   @user = User.create(<Incluir aqui el data para los atributos>)
  # end
  #
  # Ojo con la diferencia entre usar create y new al crear una instancia de un modelo. La primera lo guarda
  # en la base de datos (aplica un .save) y el segundo no lo hace. Para decidir si es valido o no un modelo
  # basta con usar new ya que si ocupan create con datos invalidos para el modelo la base de datos se los va
  # a rechazar por las validaciones al guardarlo.
  test 'is valid with valid attributes' do
    assert @user.valid?
  end
end
