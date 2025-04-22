from sklearn.preprocessing import MinMaxScaler

data = [[30], [40], [50], [20], [60]]
scaler = MinMaxScaler()
normalized = scaler.fit_transform(data)
print(normalized)