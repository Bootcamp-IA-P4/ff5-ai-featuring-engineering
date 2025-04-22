import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

# Dataset de ejemplo
data = {
    "Área": [50, 80, 120],
    "Precio_por_m2": [2000, 1800, 2500],
    "Edad": [25, 40, 60]
}
df = pd.DataFrame(data)

# 1. Interacción
df["Precio_total"] = df["Área"] * df["Precio_por_m2"]

# 2. Polinómico
df["Edad_cuadrada"] = df["Edad"] ** 2

# 3. Binning
df["Grupo_Edad"] = pd.cut(df["Edad"], bins=[0, 30, 50, 100], labels=["Joven", "Adulto", "Senior"])

print(df)

