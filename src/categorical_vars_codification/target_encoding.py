import pandas as pd
import matplotlib.pyplot as plt

# Dataset de ejemplo
data = {
    "Ciudad": ["Madrid", "Barcelona", "Valencia", "Madrid", "Barcelona"],
    "Precio": [300000, 400000, 250000, 320000, 380000]
}
df = pd.DataFrame(data)
# Calcular promedio del target (precio) por ciudad
target_map = df.groupby("Ciudad")["Precio"].mean().to_dict()
df["Ciudad_TargetEnc"] = df["Ciudad"].map(target_map)

# Gráfico
plt.figure(figsize=(10, 4))
plt.bar(target_map.keys(), target_map.values(), color='orange')
plt.title("Target Encoding: Precio promedio por ciudad")
plt.xlabel("Ciudad")
plt.ylabel("Precio Promedio (€)")
plt.show()

