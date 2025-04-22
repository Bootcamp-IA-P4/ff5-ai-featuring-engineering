import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# 1. Generar Datos Sintéticos
# Crear datos no lineales con ruido
np.random.seed(42)
X = np.linspace(0, 10, 100).reshape(-1, 1)
y = np.sin(X).ravel() + np.random.normal(0, 0.1, X.shape[0])  # Ruido añadido

# Split en train y test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)



# 3. Modelo Generalizado (Random Forest)
# Random Forest (menos propenso a overfitting)
rf = RandomForestRegressor(n_estimators=100, max_depth=3)
rf.fit(X_train, y_train)

# Predicciones
y_pred_train_rf = rf.predict(X_train)
y_pred_test_rf = rf.predict(X_test)

# Métricas
print(f"MSE Train (RF): {mean_squared_error(y_train, y_pred_train_rf):.4f}")  # ~0.02
print(f"MSE Test (RF): {mean_squared_error(y_test, y_pred_test_rf):.4f}")    # ~0.03 (similar)

# Gráfica de Generalización:
plt.figure(figsize=(10, 6))
plt.scatter(X_train, y_train, color='blue', label='Train', alpha=0.5)
plt.scatter(X_test, y_test, color='red', label='Test', alpha=0.5)
plt.plot(X, rf.predict(X), color='green', label='Random Forest', linewidth=2)
plt.legend()
plt.title("Modelo Generalizado: Captura la tendencia sin memorizar ruido")
plt.show()