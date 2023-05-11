# frozen_string_literal: true

# Esta clase modela la ascociacion de las solicitudes de turnos y atributos a validar
class Request < ApplicationRecord
  belongs_to :user
  belongs_to :turno
  validates :descripcion,
            presence: { message: 'agrega una dirección o descripción de tu solicitud' },
            length: { minimum: 5, message: 'tiene menos de 5 caracteres' }
  validates :estado, presence: { message: 'agrega un estado valido' }
end
