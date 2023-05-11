# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)
require 'faker'

AdminUser.create(email: 'admin@uc.cl', password: 'password', password_confirmation: 'password')
unless User.any?
  20.times do
    user = User.create!(
      email: Faker::Internet.safe_email,
      password: 'password',
      password_confirmation: 'password',
      name: Faker::Name.name,
      address: Faker::Address.full_address,
      description: Faker::Lorem.sentence,
      gender: Faker::Gender.binary_type,
      phone: %w[2 9].sample + (Faker::Number.between(from: 10_000_000, to: 99_999_999)).to_s,
      reglas: Faker::Lorem.sentence)

    5.times do
      hora = Faker::Number.between(from: 0, to: 23).to_s
      minuto = Faker::Number.between(from: 0, to: 59).to_s
      if hora.length == 1
        hora = "0" + hora
      end
      if minuto.length == 1
        minuto = "0" + minuto
      end
      hora = hora + ":" + minuto
      user.turnos.create!(
        cantidad_asientos: Faker::Number.between(from: 1, to: 4),
        hora_salida: hora,
        direccion_salida: %w[Campus_Oriente Casa_Central Campus_Villarrica].sample,
        direccion_llegada: %w[Campus_San_Joaquín Campus_Lo_contador].sample,
        dia_semana: %w[Lunes Martes Miércoles Jueves Viernes Sábado].sample,
        tipo: %w[Ida Vuelta].sample,
        espacio: %w[Solo_mochilas Proyecto_de_tamaño_mediano Maqueta_grande].sample,
        estado: %w[ACTIVO CONFIRMADO COMPLETADO].sample)
    end

    20.times do
      user.resenas.create!(
        contenido: Faker::Lorem.sentence,
        calificacion: Faker::Number.between(from: 0, to: 5),
        turno_id: Turno.pluck(:id).sample)
    end

    20.times do
      user.reports.create!(
        usuario: Faker::Name.name,
        contenido: Faker::Lorem.sentence,
        estado: %w[En_revisión Revisado].sample)
    end

    4.times do
      user.requests.create!(
        descripcion: Faker::Lorem.sentence,
        estado: %w[ACEPTADO RECHAZADO PENDIENTE].sample,
        turno_id: Turno.pluck(:id).sample)
    end

    30.times do
      user.mensajes.create!(
        contenido: Faker::Lorem.sentence,
        turno_id: Turno.pluck(:id).sample)
    end
  end
end