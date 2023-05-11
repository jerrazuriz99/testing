# frozen_string_literal: true

require 'rails_helper'

class ResenasTest < ActiveSupport::TestCase
  RSpec.describe 'Resena', type: :request do
    # Aquí se utiliza la factory de Resena para la creación de una publicación, en caso de no querer
    # ocupar este gema revisar el ejemplo del test modelo de usuarios entregado
    before do
      @user = FactoryBot.create(:user)
      sign_in @user # Helper de devise que permite simular el login de un usuario de la base de datos
    end
    # Otra forma de crear instancias de modelo con FactoryBot y que se puedan aceder dentro de los tests
    let!(:turno) { create(:turno) }
    let!(:resena) { create(:resena) }

    # Se describe lo que se testea
    describe 'get new' do
      # Comportamiento esperado
      it 'should return a successful resena' do
        get resenas_path(id: resena.id, id_viaje: turno.id)
        # Lo esperado es que la respuesta tenga un status ok o 200 que representa que ha salido bien
        expect(response).to have_http_status(:ok)
      end
      # Comportamiento esperado
      it 'should return a redirect if not login' do
        sign_out @user # Metodo de devise para simular el logout de un usuario
        get resenas_path(id: resena.id, id_viaje: turno.id)
        # Lo esperado es que la respuesta tenga un status redirect o 3xx que representa un redirecionamiento
        # esto porque la vista es protegida y requiere realizar antes el login
        expect(response).to have_http_status(:redirect)
      end
    end
  end
end
