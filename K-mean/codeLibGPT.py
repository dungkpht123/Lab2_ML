import numpy as np
import matplotlib.pyplot as plt

# Generate random data
X = np.random.rand(100, 2)

# Initialize centroids
centroids = np.array([[0.2, 0.4], [0.6, 0.7]])

# Loop until convergence
max_iter = 10
for i in range(max_iter):
    # Assign points to the closest centroid
    distances = np.sqrt(((X - centroids[:, np.newaxis])**2).sum(axis=2))
    labels = np.argmin(distances, axis=0)
    
    # Update centroids
    for j in range(len(centroids)):
        centroids[j] = np.mean(X[labels == j], axis=0)
    
    # Plot the clusters and centroids
    plt.scatter(X[:, 0], X[:, 1], c=labels)
    plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=200, linewidths=3)
    plt.show()



"""
Trong mỗi vòng lặp, chúng ta tính khoảng cách Euclidean giữa mỗi điểm dữ liệu và trung tâm của các cụm bằng cách sử dụng công thức distances = np.sqrt(((X - centroids[:, np.newaxis])**2).sum(axis=2)). 
Sau đó, chúng ta gán các điểm dữ liệu vào cụm gần nhất bằng cách chọn chỉ mục của cụm có khoảng cách nhỏ nhất bằng `labels'. 
Tiếp theo, chúng ta cập nhật trung tâm của các cụm bằng cách tính trung bình của các điểm dữ liệu trong mỗi cụm bằng đoạn code centroids[j] = np.mean(X[labels == j], axis=0). 
Cuối cùng, chúng ta hiển thị kết quả phân cụm trên đồ thị bằng cách sử dụng hàm plt.scatter() để vẽ các điểm dữ liệu và plt.scatter() với marker x để vẽ trung tâm của các cụm.

Với mỗi vòng lặp, chúng ta sẽ nhìn thấy một đồ thị hiển thị phân cụm của các điểm dữ liệu và vị trí của các trung tâm cụm tương ứng. 
Quá trình lặp lại sẽ tiếp tục cho đến khi thuật toán hội tụ hoặc đạt đến giới hạn số lần lặp cho trước.
"""