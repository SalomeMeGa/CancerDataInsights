import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos del archivo
df = pd.read_csv('salud_cancer.csv')

# Mostrar las primeras filas 
print(df.head())

# Resumen estadístico
print(df.describe())

# Distribución de los tipos de cáncer
print(df['tipo_cancer'].value_counts())

# Histograma de edades
sns.histplot(df['edad'], bins=10, kde=True)
plt.title('Distribución de Edades')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
# Guardar la figura en un archivo
plt.savefig('histograma_edades.png')

# Supervivencia media por tipo de cáncer
df.groupby('tipo_cancer')['supervivencia_meses'].mean().plot(kind='bar')
plt.title('Supervivencia Promedio por Tipo de Cáncer')
plt.ylabel('Meses')
plt.savefig('histograma_supervivencia.png')