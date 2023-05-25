import numpy as np

# Hàm tính ma trận hiệp phương sai
def compute_covariance_matrix(X):
    n_samples = X.shape[0]
    covariance_matrix = np.dot(X.T, X) / (n_samples - 1)
    return covariance_matrix

# Hàm tính các thành phần chính và giá trị riêng tương ứng
def compute_eigenvectors_and_eigenvalues(covariance_matrix):
    eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
    return eigenvalues, eigenvectors

# Hàm giảm chiều dữ liệu PCA
def reduce_dimension_PCA(X, n_components):
    # Tính ma trận hiệp phương sai
    covariance_matrix = compute_covariance_matrix(X)
    
    # Tính các thành phần chính và giá trị riêng
    eigenvalues, eigenvectors = compute_eigenvectors_and_eigenvalues(covariance_matrix)
    
    # Sắp xếp các thành phần chính theo giá trị riêng giảm dần
    sorted_indices = np.argsort(eigenvalues)[::-1]
    sorted_eigenvectors = eigenvectors[:, sorted_indices]
    
    # Lấy n thành phần chính đầu tiên
    selected_eigenvectors = sorted_eigenvectors[:, :n_components]
    
    # Giảm chiều dữ liệu
    reduced_data = np.dot(X, selected_eigenvectors)
    
    return reduced_data

# Đọc dữ liệu từ tệp CSV
def load_data(filename):
    dataset = np.genfromtxt(filename, delimiter=',', skip_header=1)
    X = dataset[:, :-1]  # Lấy tất cả các cột trừ cột cuối là nhãn
    y = dataset[:, -1]  # Lấy cột cuối là nhãn
    return X, y

# Thực hiện giảm chiều PCA trên tập dữ liệu Iris
X, y = load_data('iris.csv')

# Chuẩn hóa dữ liệu
mean_X = np.mean(X, axis=0)
X -= mean_X

# Tính ma trận hiệp phương sai
covariance_matrix = compute_covariance_matrix(X)

# Tính các thành phần chính và giá trị riêng
eigenvalues, eigenvectors = compute_eigenvectors_and_eigenvalues(covariance_matrix)

# Sắp xếp các thành phần chính theo giá trị riêng giảm dần
sorted_indices = np.argsort(eigenvalues)[::-1]
sorted_eigenvectors = eigenvectors[:, sorted_indices]

# Lấy n thành phần chính đầu tiên
selected_eigenvectors = sorted_eigenvectors[:, :2]

# Giảm chiều dữ liệu
reduced_data = np.dot(X, selected_eigenvectors)

# In dữ liệu sau khi được giảm chiều
print("Dữ liệu sau khi giảm chiều:")
print(reduced_data)