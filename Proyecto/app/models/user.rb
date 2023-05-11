# frozen_string_literal: true

# Esta clase modela la ascociacion de los usuarios y atributos a validar
class User < ApplicationRecord
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable, :trackable and :omniauthable
  has_many :turnos, dependent: :destroy
  has_many :requests, dependent: :destroy
  has_many :resenas, dependent: :destroy
  has_many :mensajes, dependent: :destroy
  has_many :reports, dependent: :destroy
  has_one_attached :image, dependent: :destroy
  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :validatable
  validates :name, presence: { message: 'agrega un nombre' },
                   length: { minimum: 3, message: 'tiene un minimo de 3 caracteres' }
  validates :address, presence: { message: 'agrega una dirección' }
  validates :description, presence: { message: 'agrega una descripción' }
  validates :phone, presence: { message: 'agrega un numero telefonico' },
                    length: { minimum: 8, message: 'ingresa un numero de 8 digitos' },
                    numericality: { only_integer: true, message: 'ingresa tan solo valores numericos' },
                    format: { with: /(\+?56){0,1}(9|2)[1-9]\d{7}/,
                              message: 'tiene que comenzar con 2 o 9 seguido de 8 digitos, el +56 es opcional' }
  validates :gender, presence: { message: 'escoge un genero' }
end
