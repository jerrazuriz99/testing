# frozen_string_literal: true

# En caso de utilizar MiniTest con FactoryBot tienen que eliminar los archivos de esta carpeta y
# ubicarlos en la carpeta factories dentro de test

require 'faker'

FactoryBot.define do
  factory :user do
    email { Faker::Internet.safe_email }
    password { 'password' }
    password_confirmation { 'password' }
    name { Faker::Name.name }
    address { Faker::Address.full_address }
    description { Faker::Lorem.sentence }
    gender { Faker::Gender.binary_type }
    phone { '+56998765432' }
    reglas { Faker::Lorem.sentence }
  end
end
