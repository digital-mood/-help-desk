# Aplicación Simple de Help Desk
Esta es una aplicación web sencilla para gestionar tickets de soporte o solicitudes de ayuda. La aplicación permite a los usuarios crear nuevos tickets, ver una lista de todos los tickets existentes y marcar los tickets como resueltos.

## Características
* ***Creación de tickets***: Formulario para enviar nuevas solicitudes, incluyendo un título y una descripción.
* ***Listado de tickets***: Muestra todos los tickets en una tabla, con su ID, título, descripción y estado actual.
* ***Gestión de estado***: Los tickets tienen un estado que puede ser abierto o resuelto.

* ***Persistencia de datos***: Los datos de los tickets se guardan en un archivo tickets.json, lo que permite que la información persista incluso si la aplicación se reinicia.

## Tecnologías Utilizadas
* ***Python***: El lenguaje de programación principal.
* ***Flask***: Un framework web ligero y fácil de usar para Python.
* ***JSON***: Utilizado como una base de datos simple para almacenar los tickets.
* ***HTML/CSS***: Para la interfaz de usuario.

## Cómo Ejecutar la Aplicación
Sigue estos sencillos pasos para poner en marcha la aplicación en tu entorno local.

1. Requisitos previos
Asegúrate de tener Python instalado en tu sistema.

2. Configuración del proyecto
Crea una nueva carpeta para el proyecto y navega hasta ella en tu terminal.

> Bash

``mkdir helpdesk_app``
``cd helpdesk_app``
``Instala las librerías necesarias: Flask y uuid.``

> Bash

``pip install Flask uuid``

3. Estructura de archivos
Crea los siguientes archivos y carpetas dentro de la carpeta principal del proyecto:

helpdesk_app/
├── app.py
├── tickets.json
└── templates/
    └── index.html
4. Copiar el código
Copia el código proporcionado para cada archivo:

app.py: El código principal de la aplicación, que maneja las rutas y la lógica.

index.html: La plantilla HTML para la interfaz de usuario.

tickets.json: Un archivo vacío que la aplicación usará para guardar los tickets.

5. Iniciar la aplicación
Una vez que tengas todos los archivos en su lugar, ejecuta la aplicación desde tu terminal:

Bash

python app.py
La aplicación se ejecutará en http://127.0.0.1:5000/. Abre esta dirección en tu navegador para empezar a usarla.

Este README.md es un punto de partida excelente para que cualquiera pueda entender y usar tu aplicación. ¿Te gustaría añadirle alguna sección o modificar algo?


