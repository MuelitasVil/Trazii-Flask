# Introduccion 
Explicar librerias del proyecto y como ejecutarlo.

# Ejecutar el proyecto : 

## Configurar ambiente local 

1. Clonar el repositorio en equipo personal 

2. ingrese a la carpeta de la proyecto (app)

3. Cree el ambiente vitual usando el comando "py -m venv .venv"

4. Para activar el ambiente virtual ejecute el siguiente comando :
    - windouws : ".venv\Scripts\activate" 
    - macOS y Linux :  "source .venv/bin/activate"  

5. En su consola deberia aparecer (.venv) al principio si hizo este proceso correctamente. 

6. Descargue los paquetes pip asociados al proyecto con el comando "pip install -r .\requirements.txt "

7. Ejecute "flask run" para ejecutar el proyecto. Si desea ejecutar el proyecto en modo Debug ingrese el comando "flask run --debug".

8. Si desea salir del entorno virtual ejecute "deactivate"  

9. Llegado el caso que necesite agregar otro paquete al proyecto descaguelo dentro del ambiente virtual y ejecute le comando "pip freeze > requirements.txt" tenga cuidado con este comando pues sobreescribirta el archivo requeriments.txt 

## Configurar ambiente de produccion : 

Si desea probar su codigo en un ambiente de produccion, ejecute el siguiente comando para verificar si funcionan sus cambios en el docker.
- docker-compose up --build


# Estrucutura del proyecto : 

Con el fin de no crear un archivo __init__.py en cada carpeta, unicamente se inicializa como un paquete de python la carpeta app, por esta razon todas las impotaciones de archivos se van a realizar de la siguiente forma :

from app.folder.archivo import funcion


## **routes :**

En la carpeta routes va a encontrar los end-points asociados a las vistas de la página web, esto se realiza usando los BluePrints con el fin de organizar el proyecto. 

### home :

En home encontrara la pestaña de inicio de la página web, llamara a la función Login que encontrara en el archivo sincronizar de la carpeta sync. Si el inicio de sesión fue exitoso retornara la página web del menú donde se visualizarán los datos generales del usuario.

### menu : 

En menú encontrara la pestaña principal del dashboard, actualmente solamente cuenta con unos datos básicos de la finca. Llamando los datos de las trazas y trazables usando la funcion sincronizar_datos que encontrara en el archivo sincronizar de la carpeta sync. 

## **services :** 

En la carpeta services va a encontrar la lógica de extracción de datos para ser visualización de datos en la pagina web.

### auth : 

En la carpeta auth encontrara las funciones que permiten a la persona autorizarse en la página web.

- *authentication :* En autenticación se llama al end-point desde el archivo constants, verifica que el usuario exista y guarda la información del usuario y el token usando la clase localStorage.

### sync : 

En la carpeta sync encontrara las funciones que permiten al proyecto traer los datos del metamodelo.

- *datos y ubicaciones:* Usando la clase localStorage llamara la información del usuario y el token para hacer un peticion al end-point desde el archivo constants, filtrara la información de los trazables y los organizara en un diccionario dependiendo de su tipo de trazable y contara la cantidad de estos en un diccionario, donde el trazii-id sera la llave primaria de los datos del trazable. Finalmente enviara la información recolectada al localStorage con el fin de reutilizar la información.     
 
- *trazas y caracteristicas:* Usando la clase localStorage llamara la informacion del usuario y el token para hacer un petición al end-point desde el archivo constants, filtrara la información de las trazas y los organizara en un diccionario dependiendo de su tipo de tarea, donde la hora de inicio será la llave primaria los datos de la tarea. Finalmente enviara la información recolectada al localStorage con el fin de reutilizar la información.

## **utils :** 

En la carpeta utils encontrara las funciones para filtrar los datos del metamodelo. 

## **shared :** 

En esta carpeta encontrar clases y variables que serán compartida en todo el proyecto.

- *constants:* Encontrara los end-points relacionados con la comunicación con el back-end, el tipo de token jwt, los tipos de trazas y trazables.

- *localStorage:* Encontrara la clase localStorage donde se encapsula los métodos para guardar la información en localStorage. 

- *trazables:* Encontrara la clase de trazables, se declarar como atributos de la clase los diccionarios donde se va a almacenar la información de la respuesta de sincronización. Se encapsulan métodos como setters, getters o comprobar el tipo de trazable. 

- *trazas:* Encontrara la clase de trazas, se declarar como atributos de la clase los diccionarios donde se va a almacenr la informacion de la respuesta de sincronización. Se encapsulan métodos como setters, getters o comprobar el tipo de traza.

## **static**  
En esta carpeta encontrara los archivos estáticos que pertenecen al html. encontrará el css de la página y archivos javascript.

## **templates**
En esta carpeta encontrara el html de la página web, utiliza como el gestor de platillas llamado jinja2, además de esto se encapsulan componentes en la carpeta macros.

- *base:* Archivo que declara los archivos css que se usan en todas las vistas de la página, el resto de plantillas de jinja2 heredan estilos de esta página.

- *home* Pagina principal de trazii.com encontrara información general, podrá ingresar y registrarse a la aplicación. 

- *menu:* Pagina principal del menú de dashboard de la información perteneciente al usuario.

# Documentacion para subir el proyecto a azure 

## Iniciar una app web de python 

- https://learn.microsoft.com/es-es/azure/app-service/quickstart-python?tabs=flask%2Cwindows%2Cazure-cli%2Cvscode-deploy%2Cdeploy-instructions-azportal%2Cterminal-bash%2Cdeploy-instructions-zip-azcli

## Configuración de una aplicación de Python en Linux para Azure App Service

- https://learn.microsoft.com/es-es/azure/app-service/configure-language-python

