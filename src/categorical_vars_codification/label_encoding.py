from sklearn.preprocessing import LabelEncoder
import pandas as pd
import matplotlib.pyplot as plt

# Dataset de ejemplo
data = {
    "Ciudad": ["Madrid", "Barcelona", "Valencia", "Madrid", "Barcelona"],
    "Precio": [300000, 400000, 250000, 320000, 380000]
}
df = pd.DataFrame(data)
# Aplicar Label Encoding
encoder = LabelEncoder()
df["Ciudad_LabelEnc"] = encoder.fit_transform(df["Ciudad"])

# Gráfico
plt.figure(figsize=(10, 4))
plt.scatter(df["Ciudad"], df["Ciudad_LabelEnc"], color='red', s=100)
plt.title("Label Encoding: Asigna números únicos")
plt.xlabel("Ciudad Original")
plt.ylabel("Código Numérico")
plt.grid()
plt.show()