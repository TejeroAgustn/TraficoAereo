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

1.4 Ejecución:

   - En el archivo app.py se encuentran las entradas de la simulación:
     ```
     server = AirTrafficServer(AirTrafficModel, tam_cuadricula=70, tiempo_simulacion=200, num_airports=10, 
                              num_planes=30, max_num_aisrstrips=1, max_plane_speed=1, tiempo_entre_despegues_aterrizajes=5, max_time_waiting=5)
     ```
   - El caso 1 y 2 vienen predefinidos, se descomenta aquel que se quiera ejecutar y se ejecuta la app.
   - Los parámetros pueden modificarse como se crea conveniente
   - Los cuadrados azules representan los aeropuertos y los círculos rojos los aviones
   - Si un avión se encuentra en una pista para aterrizar o despegar o está esperando al permiso del aeropuerto para usar una pista permanecerá fijo sobre dicho aeropuerto
