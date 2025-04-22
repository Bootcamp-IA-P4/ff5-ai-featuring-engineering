import category_encoders as ce
import pandas as pd
import matplotlib.pyplot as plt

# Dataset de ejemplo
data = {
    "Ciudad": ["Madrid", "Barcelona", "Valencia", "Madrid", "Barcelona"],
    "Precio": [300000, 400000, 250000, 320000, 380000]
}
df = pd.DataFrame(data)

# Aplicar Binary Encoding
encoder = ce.BinaryEncoder(cols=["Ciudad"])
df_binary = encoder.fit_transform(df)

# Gráfico (primeras 2 columnas binarias)
plt.figure(figsize=(10, 4))
plt.bar(df_binary["Ciudad_0"].unique(), df_binary["Ciudad_0"].value_counts(), color='green')
plt.title("Binary Encoding: Bits de la representación binaria")
plt.xlabel("Bit 0")
plt.ylabel("Conteo")
plt.show()