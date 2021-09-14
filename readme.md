Para instalar primero se tiene que contar con python, luego se instala django con, se uso python 3.9 para el proyecto

`pip install django`

`pip install -r requirements.txt`

Se uso un entorno virtual para este proyecto

Configurar la base de datos de acuerdo a sus preferencias (settings.py>databases), en este caso se uso Postgres

`python manage.py makemigrations`

`python manage.py migrate`

Para ejecutar el servicio de APIRest ejecutar el comando

`python manage.py runserver`
