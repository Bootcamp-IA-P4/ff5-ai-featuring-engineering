import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import KBinsDiscretizer

# Crear datos sintéticos con relación no lineal
np.random.seed(42)
X = np.linspace(0, 100, 500)
y = np.where(X < 30, X*2, 
             np.where(X < 70, 60 + (X-30)*0.5, 
                     80 + (X-70)*0.2)) + np.random.normal(0, 3, 500)

df = pd.DataFrame({'Edad': X, 'Riesgo': y})

# Estrategias de discretización
strategies = ['uniform', 'quantile', 'kmeans']
n_bins = 5

plt.figure(figsize=(18, 5))

for i, strategy in enumerate(strategies):
    # Discretización
    discretizer = KBinsDiscretizer(n_bins=n_bins, encode='ordinal', strategy=strategy)
    df[f'Edad_{strategy}'] = discretizer.fit_transform(df[['Edad']]).astype(int)
    
    # Calcular promedio de riesgo por bin
    bin_means = df.groupby(f'Edad_{strategy}')['Riesgo'].mean()
    bin_edges = discretizer.bin_edges_[0]
    
    # Visualización
    plt.subplot(1, 3, i+1)
    plt.scatter(df['Edad'], df['Riesgo'], alpha=0.5, label='Datos originales')
    
    # Graficar bins
    for edge in bin_edges:
        plt.axvline(edge, color='red', linestyle='--', alpha=0.3)
    
    # Graficar promedio por bin
    for bin_num in range(n_bins):
        mask = (df[f'Edad_{strategy}'] == bin_num)
        plt.hlines(bin_means[bin_num], 
                   bin_edges[bin_num], 
                   bin_edges[bin_num+1], 
                   colors='black', linewidth=3)
    
    plt.title(f'Discretización {strategy.capitalize()}')
    plt.xlabel('Edad')
    plt.ylabel('Riesgo')
    plt.legend()

plt.tight_layout()
plt.show()

# Comparación de modelos con y sin discretización
X = df[['Edad']]
y = df['Riesgo']

# Modelo lineal sin discretización
lr_raw = LinearRegression()
lr_raw.fit(X, y)
y_pred_raw = lr_raw.predict(X)
mse_raw = mean_squared_error(y, y_pred_raw)

# Modelo lineal con discretización (mejor estrategia)
df['Edad_bin'] = discretizer.fit_transform(X)
X_bin = pd.get_dummies(df['Edad_bin'], prefix='bin')
lr_bin = LinearRegression()
lr_bin.fit(X_bin, y)
y_pred_bin = lr_bin.predict(X_bin)
mse_bin = mean_squared_error(y, y_pred_bin)

# Modelo de árbol de decisión (para comparación)
tree = DecisionTreeRegressor(max_depth=3)
tree.fit(X, y)
y_pred_tree = tree.predict(X)
mse_tree = mean_squared_error(y, y_pred_tree)

# Resultados
print("\nComparación de MSE:")
print(f"Regresión Lineal (sin discretización): {mse_raw:.2f}")
print(f"Regresión Lineal (con discretización): {mse_bin:.2f}")
print(f"Árbol de Decisión: {mse_tree:.2f}")

# Visualización comparativa
plt.figure(figsize=(12, 6))
plt.scatter(df['Edad'], df['Riesgo'], alpha=0.3, label='Datos reales')
plt.plot(df['Edad'], y_pred_raw, color='red', label='Regresión Lineal (sin bin)', linewidth=2)
plt.plot(df['Edad'], y_pred_bin, color='green', label='Regresión Lineal (con bin)', linewidth=2)
plt.plot(df['Edad'], y_pred_tree, color='blue', label='Árbol de Decisión', linewidth=2)
plt.title('Comparación de Modelos con/sin Discretización')
plt.xlabel('Edad')
plt.ylabel('Riesgo')
plt.legend()
plt.show()

# Análisis de bins óptimos
mse_values = []
bin_range = range(2, 15)

for n in bin_range:
    discretizer = KBinsDiscretizer(n_bins=n, encode='ordinal', strategy='quantile')
    X_bin = discretizer.fit_transform(X)
    X_bin_dummies = pd.get_dummies(X_bin.ravel(), prefix='bin')
    lr = LinearRegression()
    lr.fit(X_bin_dummies, y)
    y_pred = lr.predict(X_bin_dummies)
    mse_values.append(mean_squared_error(y, y_pred))

plt.figure(figsize=(10, 5))
plt.plot(bin_range, mse_values, marker='o')
plt.title('Selección del Número Óptimo de Bins')
plt.xlabel('Número de Bins')
plt.ylabel('MSE')
plt.grid()
plt.show()