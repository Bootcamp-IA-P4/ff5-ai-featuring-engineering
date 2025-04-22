import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler


# Datos de ejemplo con outlier
data = [10, 20, 30, 40, 500]

# Aplicar escalados
minmax = MinMaxScaler().fit_transform(np.array(data).reshape(-1, 1))
standard = StandardScaler().fit_transform(np.array(data).reshape(-1, 1))
robust = RobustScaler().fit_transform(np.array(data).reshape(-1, 1))

# Gráfico
plt.figure(figsize=(12, 4))
plt.plot(data, label="Original", marker='o')
plt.plot(minmax, label="Min-Max", marker='s')
plt.plot(standard, label="Estandarización", marker='^')
plt.plot(robust, label="Robusto", marker='d')
plt.legend()
plt.title("Comparación de Técnicas de Escalado")
plt.show()