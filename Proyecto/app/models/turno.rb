# frozen_string_literal: true

# Esta clase modela la ascociacion de los turnos y atributos a validar
class Turno < ApplicationRecord
  belongs_to :user
  has_many :requests, dependent: :destroy
  has_many :resenas, dependent: :destroy
  has_many :mensajes, dependent: :destroy
  validates :cantidad_asientos,
            presence: { message: 'escoge una cantidad' }, numericality: { only_integer: true }
  validates :direccion_salida, presence: { message: 'agrega una dirección de salida' },
                               length: { minimum: 1, message: 'agrega una dirección de salida' }
  validates :direccion_llegada, presence: { message: 'agrega una dirección de llegada' },
                                length: { minimum: 1, message: 'agrega una dirección de llegada' }
  validates :dia_semana, presence: { message: 'agrega un día de la semana' }
  validates :tipo, presence: { message: 'agrega un tipo de turno' }
  validates :hora_salida, presence: true
  validates :espacio, presence: { message: 'escoge una opción' }
end
