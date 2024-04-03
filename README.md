# Trafico Aereo Python
## Tabla de Contenidos
1. [Configuración del entorno local](#configuracion-entorno-local)

------------------------------------------------------------------------------------------------------------------------------------

<a name="configuracion-entorno-local"></a>
**1. Configuración del entorno local**

Para comenzar, asegúrate de tener GIT, Visual Studio Code y Python instalados en tu ordenador.

1.1 Descarga del repositorio:

   - Navega a la carpeta deseada para almacenar tu proyecto localmente.
   - Haz clic derecho, selecciona "Git Bash here" y ejecuta el siguiente comando:
     ```
     git clone https://github.com/TejeroAgustn/TraficoAereo.git
     ```

1.2 Configuración de Visual Studio Code:

   - Abre Visual Studio Code y selecciona "Open Folder". Elige la carpeta de tu proyecto.
   - Abre el archivo llamado `app.py`.
   - Asegúrate de tener la extensión de Python instalada en Visual Studio Code. Si no la tienes, aparecerá una opción para descargarla en la esquina inferior derecha. Con esta extensión, verás un icono de un triángulo en la esquina superior derecha para ejecutar la aplicación.

1.3 Configuración del entorno virtual:

   - En la consola, ejecuta el siguiente comando para crear un entorno de desarrollo local:
     ```
     python -m venv ./venv
     ```
     Si no funciona prueba con:
     ```
     py -m venv ./venv
     ```
   - Activa el entorno recién creado con el comando:
     ```
     .\venv\scripts\Activate.ps1
     ```
     Si te da errores dáselos a chatGPT para que te diga la mierda que tienes que poner en GitBash para que no te de error.
   - Instala las librerías y dependencias del proyecto con: (cosa que no hace falta porque aún no usamos librerías externas)
     ```
     pip install -r requirements.txt
     ```

Con estas configuraciones, debería estar todo listo para ejecutar el proyecto correctamente. Si te da algún error ya sabes, a chatGPT.
