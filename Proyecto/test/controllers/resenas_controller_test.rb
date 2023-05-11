# frozen_string_literal: true

require 'test_helper'

class ResenasControllerTest < ActionDispatch::IntegrationTest
  # Se utiliza FactoryBot si utilizan MiniTest traspasar los archivos de spec/factories a test/factories
  # Si no quieren utilizar esa gema pueden revisar el ejemplo en el test modelo de usuarios entregado
  def setup
    @user = FactoryBot.create(:user)
    sign_in @user # Helper de la gema devise para simular el login de un usuario en la base de datos
  end

  test 'should get index' do
    sign_in @user
    get resenas_index_url
    # Lo esperado es que la respuesta tenga un status ok o 200 que representa que ha salido bien
    assert_response :success
  end

  test 'should not get index adn redirect' do
    sign_out @user # Helper de la gema devise para simular el logout de un usuario de la base de datos
    get resenas_index_url
    # Lo esperado es que la respuesta tenga un status redirect o 3xx que representa un redirecionamiento
    # esto porque la vista es protegida y requiere realizar antes el login
    assert_response :redirect # redirect to login
  end
end
