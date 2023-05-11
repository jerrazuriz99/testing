# frozen_string_literal: true

# Esta clase modela la ascociacion de los mensajes y atributos a validar
class Mensaje < ApplicationRecord
  belongs_to :user
  belongs_to :turno
  validates :contenido, presence: true
end
