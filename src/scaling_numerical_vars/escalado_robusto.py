from sklearn.preprocessing import RobustScaler

data = [[1000], [2000], [3000], [4000], [100000]]  # 100,000 es outlier
scaler = RobustScaler()
robust = scaler.fit_transform(data)
print(robust)