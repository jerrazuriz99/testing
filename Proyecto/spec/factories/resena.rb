# frozen_string_literal: true

require 'faker'

FactoryBot.define do
  factory :resena do
    contenido { Faker::Lorem.sentence }
    calificacion { Faker::Number.between(from: 0, to: 5) }
    association :user, factory: :user
    association :turno, factory: :turno
  end
end
