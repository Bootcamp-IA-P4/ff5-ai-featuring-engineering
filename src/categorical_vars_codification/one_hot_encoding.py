import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Ciudad": ["Madrid", "Barcelona", "Valencia", "Madrid", "Barcelona"],
    "Precio": [300000, 400000, 250000, 320000, 380000]
}
df = pd.DataFrame(data)
print("Dataset original:")
print(df)

df_encoded = pd.get_dummies(df, columns=["Ciudad"])
print("\nDataset con One-Hot Encoding:")
print(df_encoded)

plt.figure(figsize=(10, 6))

# Seleccionar solo las columnas one-hot (excluyendo 'Precio')
one_hot_cols = [col for col in df_encoded.columns if col.startswith("Ciudad_")]

# Crear un gráfico de barras apiladas para todas las filas
for i, row in df_encoded.iterrows():
    plt.bar(one_hot_cols, row[one_hot_cols], label=f"Fila {i}: {df.loc[i, 'Ciudad']}")

plt.title("One-Hot Encoding - Todas las Filas")
plt.xlabel("Ciudades Codificadas")
plt.ylabel("Valor Binario (1 = Pertenece, 0 = No)")
plt.legend()
plt.show()

# Sumar las columnas one-hot para ver la frecuencia
sum_one_hot = df_encoded[one_hot_cols].sum()

plt.figure(figsize=(10, 4))
sum_one_hot.plot(kind='bar', color='skyblue')
plt.title("Conteo de Ciudades en One-Hot Encoding")
plt.xlabel("Ciudades")
plt.ylabel("Número de Apariciones")
plt.show()