## Proyecto:Análisis de Datos de una Aerolínea

Este proyecto analiza el comportamiento de los clientes de un programa de lealtad de una aerolínea, utilizando datos históricos sobre vuelos y perfiles de clientes. El objetivo es extraer conclusiones relevantes sobre su actividad, segmentación y tendencias.

## Contenido:
1.Descripción del Proyecto
2.Estructura del Proyecto
3.Datos Utilizados
4.Metodología
5.Resultados Clave
6.Requisitos
7.Cómo Usar este Repositorio
8.Contacto


## 1. Descripción del Proyecto:
Este análisis se realiza en el contexto de un programa de lealtad de aerolíneas, donde se evalúan:

 -Actividades relacionadas con vuelos (reservas, distancias, puntos acumulados/redimidos).
 -Información demográfica y financiera de los clientes.
 -Relación entre las características de los clientes y su comportamiento en el programa.
 -El proyecto se divide en tres fases principales:

     -Exploración y Limpieza de los Datos.
     -Análisis y Visualización de Resultados.
     -Evaluación Estadística de Patrones de Comportamiento.

    
## 2.Estructura del Proyecto
El repositorio contiene los siguientes archivos y carpetas:

  ├── Data/                   # Contiene los datasets proporcionados para el análisis

  │   ├── Customer Flight Activity.csv

  │   ├── Customer Loyalty History.csv

  ├── scr/

  │   ├── soporte.py          # Librerías y Funciones reutilizables para limpieza y análisis de datos

  ├── docs/

  │   ├── enunciado-ejercicio-ev.pdf    #Enunciado de la práctica desarollada

  │   ├── README.md               # Documentación del proyecto

  ├── ev-main.ipynb           # Código principal del análisis en Jupyter Notebook

  ├── main.py                 # Código principal del análisis en Python


## 3.Datos Utilizados
- Customer Flight Activity.csv: 
  Contiene información sobre la actividad de vuelo de los clientes, como:

  ** Número de vuelos reservados.
  ** Distancias recorridas.
  ** Puntos acumulados y redimidos.
  ** Costos en dólares de los puntos redimidos.

- Customer Loyalty History.csv
  Incluye detalles de perfil de los clientes:

  ** Información demográfica (país, género, estado civil).
  ** Ingresos, nivel educativo y tipo de tarjeta de lealtad.
  ** Fechas de inscripción y cancelación del programa.
  
## 4.Metodología

  - Fase 1: Exploración y Limpieza
    Verificación de valores nulos y duplicados.
      - Limpieza de datos incorrectos (salarios negativos, valores inconsistentes).
      - Unión de datasets para análisis combinado.
      - Imputación de valores faltantes (e.g., Salary con la mediana).
    
  - Fase 2: Análisis y Visualización
    - Análisis de las siguientes preguntas:
    - Distribución de vuelos reservados por mes.
    - Relación entre distancia de vuelo y puntos acumulados.
    - Distribución de clientes por provincia/estado.
    - Comparación del salario promedio por nivel educativo.
    - Proporción de clientes por tipo de tarjeta de fidelidad.
    - Distribución según estado civil y género.
    - Visualizaciones creadas con Matplotlib y Seaborn.
  
## Fase 3: Evaluación Estadística
  - Análisis descriptivo por nivel educativo.
  

## 5. Resultados clave:
   
  Algunas de las conclusiones tras el análisis son la siguientes:

  - Tendencias en Reservas de Vuelos:
  
      - Diferencias notables entre los años 2017 y 2018.
      - Los meses de verano (julio y agosto) presentan un aumento significativo en las reservas.
   
   
  - Segmentación por Demografía:

    - Ontario concentra el mayor número de clientes.
    - Los salarios más altos corresponden a clientes con doctorado.
    
  - Relación entre Distancia y Puntos Acumulados en el programa de Lealtad:

    - Relación lineal esperada: mayor distancia -> mayor acumulación de puntos.
    
  - Prueba Estadística:

   - Existen diferencias significativas en el número de vuelos reservados según el nivel educativo.



## 6.Requisitos
- Lenguaje: Python 3.x
- Librerías utilizadas:
    - pandas
    - numpy
    - matplotlib
    - seaborn
 -scipy

## 7. Cómo Usar este Repositorio
Clonar el repositorio:
bash
Copiar código
git clone <(https://github.com/Adalab/bda-modulo-3-evaluacion-final-Zoraida-AP.git)>
cd <bda-modulo-3-evaluacion-final-Zoraida-AP>


## Ejecutar el análisis:   

Abrir el archivo ev-main.ipynb en Jupyter Notebook o cualquier editor compatible.
Asegurarse de que los datos se encuentren en la carpeta Data/.
Opcional: Usar funciones personalizadas:

Importar las funciones de limpieza y transformación desde soporte.py si deseas reutilizarlas en otros proyectos.


## 8. Contacto

Si tienes preguntas o comentarios sobre este proyecto, no dudes en contactarme:
email: mzoraida82@gmail.com
GitHub: Zoraida-AP