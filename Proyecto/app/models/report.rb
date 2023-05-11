# frozen_string_literal: true

# Esta clase modela la ascociacion de los reportes y atributos a validar
class Report < ApplicationRecord
  belongs_to :user
  validates :usuario,
            presence: { message: 'agrega el nombre' },
            length: { minimum: 3, message: 'tiene menos de 3 caracteres' }
  validates :contenido,
            presence: { message: 'agrega una descripción de tu reporte' },
            length: { minimum: 5, message: 'tiene menos de 5 caracteres' }
end
