import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Crear datos de ejemplo: transacciones de clientes
np.random.seed(42)
data = {
    "Cliente_ID": np.random.randint(1, 6, 100),
    "Fecha_Compra": pd.date_range(start="2023-01-01", periods=100),
    "Monto_Compra": np.random.uniform(10, 500, 100),
    "Categoría": np.random.choice(["Electrónicos", "Ropa", "Hogar", "Alimentos"], 100)
}
df = pd.DataFrame(data)

# 1. Agregaciones básicas por cliente
agg_features = df.groupby("Cliente_ID").agg({
    "Monto_Compra": ["count", "sum", "mean", "max", "min", "std"],
    "Fecha_Compra": ["min", "max", "nunique"]
}).reset_index()

# Renombrar columnas
agg_features.columns = [
    "Cliente_ID", 
    "Total_Compras", 
    "Gasto_Total", 
    "Gasto_Promedio", 
    "Gasto_Máximo", 
    "Gasto_Mínimo", 
    "Desviación_Gasto",
    "Primera_Compra",
    "Última_Compra",
    "Días_Compra_Únicos"
]

# 2. Frecuencia de compra (días entre compras)
df = df.sort_values(["Cliente_ID", "Fecha_Compra"])
df["Días_Entre_Compras"] = df.groupby("Cliente_ID")["Fecha_Compra"].diff().dt.days

# 3. Comportamiento por categoría
categoria_features = df.groupby(["Cliente_ID", "Categoría"]).agg({
    "Monto_Compra": "sum"
}).unstack(fill_value=0)
categoria_features.columns = [f"Gasto_{cat}" for cat in categoria_features.columns.get_level_values(1)]

# Combinar todas las características
final_features = pd.merge(agg_features, categoria_features, on="Cliente_ID")

# Calcular antigüedad del cliente
final_features["Antigüedad_Días"] = (pd.to_datetime("today") - final_features["Primera_Compra"]).dt.days

# Visualización
plt.figure(figsize=(12, 6))
final_features.set_index("Cliente_ID")[["Gasto_Total", "Gasto_Promedio", "Total_Compras"]].plot(kind="bar", subplots=True)
plt.tight_layout()
plt.show()

print("=== Características agregadas ===")
print(final_features.head())