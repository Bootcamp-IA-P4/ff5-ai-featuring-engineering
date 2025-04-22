import pandas as pd
import matplotlib.pyplot as plt

# Dataset de ejemplo
data = {
    "Ciudad": ["Madrid", "Barcelona", "Valencia", "Madrid", "Barcelona"],
    "Precio": [300000, 400000, 250000, 320000, 380000]
}
df = pd.DataFrame(data)
# Calcular frecuencias
freq_map = df["Ciudad"].value_counts(normalize=True).to_dict()
df["Ciudad_FreqEnc"] = df["Ciudad"].map(freq_map)

# Gráfico
plt.figure(figsize=(10, 4))
plt.bar(freq_map.keys(), freq_map.values(), color='purple')
plt.title("Frequency Encoding: Frecuencia relativa de cada categoría")
plt.xlabel("Ciudad")
plt.ylabel("Frecuencia")
plt.show()