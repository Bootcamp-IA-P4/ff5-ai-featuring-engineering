import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Crear datos sintéticos no lineales
np.random.seed(42)
X = np.linspace(-10, 10, 100)
y = 2*X**3 - 5*X**2 + 3*X + 10 + np.random.normal(0, 50, 100)
df = pd.DataFrame({'X': X, 'y': y})

# Dividir en train y test
X_train, X_test, y_train, y_test = train_test_split(df[['X']], df['y'], test_size=0.2, random_state=42)

# Crear características polinómicas de diferentes grados
degrees = [1, 2, 3, 4, 5]
results = []

plt.figure(figsize=(15, 10))
for i, degree in enumerate(degrees):
    # Transformación polinómica
    poly = PolynomialFeatures(degree=degree, include_bias=False)
    X_train_poly = poly.fit_transform(X_train)
    X_test_poly = poly.transform(X_test)
    
    # Entrenar modelo
    model = LinearRegression()
    model.fit(X_train_poly, y_train)
    
    # Predecir y evaluar
    y_pred = model.predict(X_test_poly)
    mse = mean_squared_error(y_test, y_pred)
    results.append({'degree': degree, 'mse': mse, 'model': model, 'poly': poly})
    
    # Visualización
    plt.subplot(2, 3, i+1)
    plt.scatter(X_train, y_train, color='blue', alpha=0.3, label='Train')
    plt.scatter(X_test, y_test, color='red', alpha=0.3, label='Test')
    
    # Ordenar valores para la curva
    X_plot = np.linspace(-10, 10, 100).reshape(-1, 1)
    X_plot_poly = poly.transform(X_plot)
    y_plot = model.predict(X_plot_poly)
    
    plt.plot(X_plot, y_plot, color='black', linewidth=2)
    plt.title(f'Grado {degree}\nMSE: {mse:.2f}')
    plt.legend()

plt.tight_layout()
plt.show()

# Comparación de resultados
results_df = pd.DataFrame(results)
print("\nComparación de modelos polinómicos:")
print(results_df[['degree', 'mse']])

# Extraer coeficientes del mejor modelo
best_model_idx = results_df['mse'].idxmin()
best_degree = results_df.loc[best_model_idx, 'degree']
best_model = results_df.loc[best_model_idx, 'model']
best_poly = results_df.loc[best_model_idx, 'poly']

print(f"\nMejor grado polinómico: {best_degree}")
print("Coeficientes del modelo:")
feature_names = best_poly.get_feature_names_out(['X'])
for name, coef in zip(feature_names, best_model.coef_):
    print(f"{name}: {coef:.4f}")