# Proyecto DCCinema Setup

## Requisitos
* ruby 3.1.3
* rails 7 (la version correcta se deberia instalar solo con el bundler)
* PostgreSQL

## Instalación

Primero tienes que definir las variables de entorno DB_USER y DB_PASSWORD  en tu computador las cuales seran usadas para la base de datos de PostgreSQL.
Si quieren utilizar alguna gema que les permita cargar variables siempre que esta no involucre cambiar el archivo config/database.yml.

Luego ejecutar lo siguiente:

```
bundle install
```

```
rails db:create
```

```
rails db:migrate
```

```
rails db:seed
```
Con las seeds se crea el usario admin y se pobla la base de datos con algunas instancias de distintos modelos

Para entrar como admin la ruta es: /admin
Usuario: admin@uc.cl
Clave: password

## Correr la pagina

Para levantar el servidor correr el siguiente comando, se debería levantar en el localhost puerto ```3000```

```
rails server
```

## Correr tests
Antes de ejecutar los tests correr
```
rails db:migrate RAILS_ENV=test
```

Para ejecutar los tests unitarios y de integracion de MiniTest se puede usar:

```
rails test
```

Lo anterior no incluye los tests de sistema

Para ejecutar los tests de Rspec se puede utilizar
```
rspec
```

## Informacion importante para realizar el deploy
A continuacion se entregan algunos datos generales de como realizar el deploy del proyecto, como no se entrega de manera detallada es tarea suya investigar más sobre como funciona render, hay bastante material en internet. 

* Tener una cuenta en cloudinary, van a necesitar el **CLOUDINARY_URL** de esa cuenta se saca en la pagina de Cloudinary.
* Crear una base de datos gratis de PostgreSQL en Render, guardar el **Internal Database URL** si su web service esta en la misma localidad o el **External Database URL** si no esta en la misma localidad.
* Crear un web service gratis en Render, tendran que conectar su repositorio a render. Si no encuentran su repositorio tienen que configurar su cuenta github en render(el boton a la derecha cuando estan creando el servicio) y entregarle permiso a render para acceder a su repositorio privado.

Su web service deberia tener las siguientes configuraciones minimas para funcionar correctamente:
* El build command: bundle install;rails assets:precompile; rails db:create; rails db:migrate; rails db:seed 
* El start command: bundle exec puma -t 5:5 -p ${PORT:-3000} -e ${RACK_ENV:-development}

Tienen que agregar las siguientes variables de entorno:
* **CLOUDINARY_URL**: La CLOUDINARY_URL de su cuenta cloudinary. Esto permite gratis almacenar las imagenes en la nube y no localmente.
* **DATABASE_URL**: La url para conectarse a su base de datos
* **RAILS_MASTER_KEY**: ae94302e7c7a0cd66fac66fc897aa77f

El resto de las configuraciones pueden definirlas a su criterio.

Con con todo lo anterior su deploy deberia construirse sin problemas
