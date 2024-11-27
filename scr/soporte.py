# Librerías de manipulación de datos
import pandas as pd          # Para la manipulación y análisis de datos
import numpy as np           # Para cálculos numéricos y operaciones en arrays

# Visualización de datos
import seaborn as sns        # Para crear gráficos estadísticos avanzados
import matplotlib.pyplot as plt  # Para crear gráficos básicos (líneas, barras, etc.)

# Evaluación de linealidad de relaciones entre variables (estadísticas)
import scipy.stats as stats  # Para métodos estadísticos generales
from scipy.stats import shapiro   # Para prueba de normalidad (Shapiro-Wilk)
from scipy.stats import levene   # Para prueba de homogeneidad de varianzas (Levene)
from scipy.stats import ttest_ind  # Para prueba t de muestras independientes
from scipy.stats import mannwhitneyu  # Para prueba de Mann-Whitney (no paramétrica)
from scipy.stats import chi2_contingency  # Para prueba de chi-cuadrado (asociación entre variables categóricas)


def limpiar_y_transformar_datos(df):
    """
    Realiza las operaciones de limpieza y transformación necesarias en el dataset combinado.

    Parámetros:
        df (DataFrame): El DataFrame combinado que contiene los datos de vuelos y lealtad.

    Retorno:
        DataFrame: El DataFrame transformado y limpio.
    """
    # Corregir valores negativos en la columna 'Salary' transformándolos a valores absolutos
    df['Salary'] = df['Salary'].abs()

    # Imputar valores nulos en 'Salary' con la mediana
    df['Salary'].fillna(df['Salary'].median(), inplace=True)

    # Eliminar duplicados
    df = df.drop_duplicates()
    
    return df