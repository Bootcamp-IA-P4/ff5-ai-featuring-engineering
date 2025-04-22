import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from mpl_toolkits.mplot3d import Axes3D

# Crear dataset sintético de propiedades
np.random.seed(42)
n_samples = 200
df = pd.DataFrame({
    'Área': np.random.normal(100, 30, n_samples).clip(50, 200),
    'Habitaciones': np.random.randint(1, 6, n_samples),
    'Distancia_Centro': np.random.exponential(5, n_samples).clip(0.5, 20),
    'Año_Construcción': np.random.randint(1950, 2023, n_samples)
})

# Crear interacciones manuales
df['Precio_por_m2'] = 2000 + 50*df['Distancia_Centro'] - 2*(2023 - df['Año_Construcción'])
df['Precio_Base'] = df['Área'] * df['Precio_por_m2']

# Interacciones complejas
df['Área_x_Habitaciones'] = df['Área'] * df['Habitaciones']
df['Área_x_Año'] = df['Área'] * (2023 - df['Año_Construcción'])
df['Habitaciones_x_Distancia'] = df['Habitaciones'] / (df['Distancia_Centro'] + 1)

# Precio final con ruido
df['Precio'] = df['Precio_Base'] * (0.9 + 0.2*df['Habitaciones']) + np.random.normal(0, 50000, n_samples)

# Visualización 3D de interacciones
fig = plt.figure(figsize=(14, 6))
ax1 = fig.add_subplot(121, projection='3d')
ax1.scatter(df['Área'], df['Habitaciones'], df['Precio'], c=df['Precio'], cmap='viridis')
ax1.set_xlabel('Área (m²)')
ax1.set_ylabel('Habitaciones')
ax1.set_zlabel('Precio')
ax1.set_title('Interacción Área x Habitaciones')

ax2 = fig.add_subplot(122, projection='3d')
ax2.scatter(df['Año_Construcción'], df['Distancia_Centro'], df['Precio'], c=df['Precio'], cmap='plasma')
ax2.set_xlabel('Año Construcción')
ax2.set_ylabel('Distancia Centro (km)')
ax2.set_zlabel('Precio')
ax2.set_title('Interacción Año x Distancia')

plt.tight_layout()
plt.show()

# Modelado para evaluar interacciones
interaction_features = ['Área', 'Habitaciones', 'Distancia_Centro', 'Año_Construcción', 'Área_x_Habitaciones']
X = df[interaction_features]
y = df['Precio']

model = LinearRegression()
model.fit(X, y)

print("Coeficientes del modelo:")
for feature, coef in zip(interaction_features, model.coef_):
    print(f"{feature}: {coef:.2f}")
print(f"Intercepto: {model.intercept_:.2f}")

# Importancia de las interacciones
importance = pd.DataFrame({
    'Feature': interaction_features,
    'Importance': np.abs(model.coef_)
}).sort_values('Importance', ascending=False)

plt.figure(figsize=(10, 5))
plt.barh(importance['Feature'], importance['Importance'])
plt.title('Importancia de las Características e Interacciones')
plt.xlabel('Valor Absoluto del Coeficiente')
plt.show()