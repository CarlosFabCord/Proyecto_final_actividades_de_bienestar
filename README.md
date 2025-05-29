# Proyecto_final_actividades_de_bienestar
Respositorio de proyecto final:
Proyecto_final_actividades_de_bienestar

📌 Descripción del Proyecto
En este repositorio está el código fuente de nuestro proyecto “Proyecto_final_actividades_de_bienestar”, desarrollado como parte del curso de programación para el proyecto final del tercer corte del año 2025-1. El objetivo del proyecto es realizar un código para una comunidad de un centro de bienestar el cual les permita gestionar de forma organizada el registro de actividades físicas, recreativas y de salud de sus miembros (spinning, fisioterapia, rumba y fortalecimiento). La aplicación permite registrar los datos de los usuarios (DI, nombre, edad), gestionar su suscripción a las diferentes clases del centro por cada mes, calcular pagos de acuerdo con cada mes facturado teniendo en cuenta el valor de cada clase, generar varias gráficas estadísticas sobre la cantidad de usuarios inscritos en cada clase u otros valores relevante, y almacena esta información para su posterior análisis.

📁 Estructura del Repositorio
A continuación, se describe la organización del código:

- app/interfaz.py: Interfaz gráfica construida con Tkinter.
- app/logica.py: Lógica de clases del proyecto (Usuario).
- app/analisis.py: Generación de reportes y visualización con Pandas y Matplotlib.
- datos/usuarios.csv: Archivo de datos registrado por la aplicación.
- README.md: Este documento.

⚙️ Cómo Usar el Código
1. Clona el repositorio:
   git clone https://github.comCarlosFabCordProyecto_final_actividades_de_bienestar.git

2. Instala las librerías:
   conda install pandas matplotlib seaborn

3. Ejecuta el archivo principal:
   python interfaz.py


4. Una vez realizado el comando le aparecerá una interfaz grafica con varios botones, cada uno para una determinada función, inicialmente agregue un primer usuario presionando, llenando los campos del registro, y posterior a eso digite los campos de la facturación, esto creará dos archivos csv en la carpeta clonada del repositorio, uno con la información de los usuarios, y el otro con las diversas facturaciones de cada usuario. Una vez hecho este primer paso podrá realizar el resto de las funciones de graficas, edición y renovación de usuarios.

5. Para hacer la cotización por cada clase de cada mes, realize la facturación, escriba su cedula, la clase y por ultima la cantidad de clases de esa actividad, luego si desea registrar otro mes, presione guardar y posterior a eso seleccione nuevamente la activdad que desee y la cantidad de clases, una vez haya agregado la cantidad de meses deseada presione enviar para solicitar el total del valor pagado.

🖥️ Requisitos del Sistema
- Python 3.8 o superior
- Librerías: pandas, matplotlib, seaborn

📌Referencias codigos externos 
Para poner imagenes sobre iconos e imagenes sobre tkinter: 
https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Resampling.LANCZOS 

👨‍💻 Autores
Este proyecto fue desarrollado por:
- Johann Eduardo Gonzales
- Carlos Fabian Cordoba
- Sebastián Jiménez Solís 

