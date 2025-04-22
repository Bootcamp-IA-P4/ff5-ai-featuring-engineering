import pandas as pd
import matplotlib.pyplot as plt

# Crear DataFrame de ejemplo con fechas
data = {
    "Fecha": pd.date_range(start="2023-01-01", periods=10, freq="D"),
    "Ventas": [120, 150, 80, 200, 250, 180, 90, 300, 350, 400]
}
df = pd.DataFrame(data)

# Extraer componentes de fecha
df["Año"] = df["Fecha"].dt.year
df["Mes"] = df["Fecha"].dt.month
df["Día"] = df["Fecha"].dt.day
df["Día_Semana"] = df["Fecha"].dt.dayofweek  # 0=Lunes, 6=Domingo
df["Es_FinDeSemana"] = df["Día_Semana"].apply(lambda x: 1 if x >= 5 else 0)
df["Trimestre"] = df["Fecha"].dt.quarter
df["Día_Año"] = df["Fecha"].dt.dayofyear

# Visualizar ventas por día de semana
plt.figure(figsize=(10, 5))
df.groupby("Día_Semana")["Ventas"].mean().plot(kind="bar")
plt.title("Ventas promedio por día de la semana")
plt.xlabel("Día de la semana (0=Lunes, 6=Domingo)")
plt.ylabel("Ventas promedio")
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()