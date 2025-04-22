from sklearn.preprocessing import StandardScaler

data = [[60000], [40000], [50000], [70000]]
scaler = StandardScaler()
standardized = scaler.fit_transform(data)
print(standardized)