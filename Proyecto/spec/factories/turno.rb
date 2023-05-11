# frozen_string_literal: true

require 'faker'

FactoryBot.define do
  factory :turno do
    cantidad_asientos { Faker::Number.between(from: 1, to: 4) }
    hora_salida { Time.zone.now }
    direccion_salida { Faker::Address.full_address }
    direccion_llegada { Faker::Address.full_address }
    dia_semana { %w[Lunes Martes Miércoles Jueves Viernes Sabado].sample }
    tipo { %w[Ida Vuelta].sample }
    espacio { %w[Solo_mochilas Proyecto_de_tamaño_mediano Maqueta_grande].sample }
    estado { %w[ACTIVO CONFIRMADO COMPLETADO].sample }
    association :user, factory: :user
  end
end
