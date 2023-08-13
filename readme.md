## 1- Clonar repositorio

## 2- Instalar virtualvenv pip install virtual venv

## 3- Crear entorno virtual python -m venv env(nombre del entorno) ; sino funciona, crear carpeta con 'mkdir venv' ubircarse dentro de esta y comando 'virtualenv venv'

## 4- Activar entorno source .\env\Scripts\activate (si se esta por fuera de la ruta 'env'), desactivar: deactivate

## 5- Instalar dependencias: pip install -r requirements.txt

## 6- Si el anterior no funciona, instalar cada uno de las dependencias nombradas:

- pip install Django==4.2 verificar que queda bien instalado en el venv: .\env\Scripts\Django-admin.exe debe mostrar los comandos de Django

## 7- desde la ruta del proyecto que desea correr Django, ejecutar: python manage.py runserver

## 8- Crear proyecto con Django(si aun no se ha creado, si no tiene una carpeta 'src' o con el nombre del proyecto y dentro 'settings.py') .\env\Scripts\Django-admin.exe startproject src(nombre de la aplicacion)

## 9- python manage.py startapp registration (crea el modulo de registro, entorno activado)

## 10- Instalar texto enriquecido: pip install django-ckeditor y el gestor de imagenes: pip install Pillow: pip install Pillow

## 11- Crear usuario administrador: python manage.py createsuperuser

## 12- Ingresar a http://127.0.0.1:8000/admin y logearse con las credenciales del paso anterior

## 13- Instalar core: python manage.py startapp core
