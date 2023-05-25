import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Đọc dữ liệu từ tập tin iris.csv
data = pd.read_csv('iris.csv')

# Chia các đặc trưng và nhãn thành hai DataFrame riêng biệt
X = data.iloc[:, :-1]  # Đặc trưng
y = data.iloc[:, -1]   # Nhãn

# Chuẩn hóa đặc trưng bằng phương pháp StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Tạo mô hình PCA với số chiều giảm xuống là 2
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# In các thành phần chính
print('Các thành phần chính (Principal Components):')
print(pca.components_)

# In tỉ lệ phương sai giải thích bởi các thành phần chính
print('\nTỉ lệ phương sai giải thích:')
print(pca.explained_variance_ratio_)