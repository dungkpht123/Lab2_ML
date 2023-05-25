import random
import math
import matplotlib.pyplot as plt

def kmeans(k, data_points):
    # khởi tạo các cluster
    clusters = {}
    for i in range(k):
        clusters[i] = []
    
    # chọn ngẫu nhiên k điểm ban đầu làm centroid
    centroids = random.sample(data_points, k)
    
    # lặp cho đến khi các điểm không thay đổi nữa
    while True:
        # gán các điểm vào cluster gần nhất
        for point in data_points:
            distances = []
            for centroid in centroids:
                distance = math.dist(point, centroid)           # tính khoảng cách điểm dataset vs centroid[i]
                distances.append(distance)                      # lưu khoảng cách vừa tim vào mảng distances
            closest_cluster = distances.index(min(distances))   # tìm giá trị min và lấy key lưu vào clusters [1,2]
            clusters[closest_cluster].append(point)
        
        # tính lại vị trí centroid cho từng cluster
        new_centroids = []
        for cluster in clusters.values():
            # khởi tạo mảng chứa tọa độ trung bình của từng chiều
            new_centroid = []
            # lặp qua từng chiều của điểm
            for dim in range(len(cluster[0])):
                # tính tổng tọa độ của từng chiều trong cluster
                sum_dim = 0
                for point in cluster:
                    sum_dim += point[dim]
                # tính tọa độ trung bình của chiều đó
                avg_dim = sum_dim / len(cluster)
                # thêm tọa độ trung bình vào mảng new_centroid
                new_centroid.append(avg_dim)
            # thêm new_centroid vào danh sách new_centroids
            new_centroids.append(new_centroid)
        
        # kiểm tra xem các centroid có thay đổi không
        if new_centroids == centroids:
            break
        
        # cập nhật centroid mới và reset các cluster
        centroids = new_centroids

        clusters = {}
        for i in range(k):
            clusters[i] = []

    return clusters

# ví dụ
data_points = [(1, 2), (1, 4), (1, 0), (4, 2), (4, 4), (4, 0), (7, 2), (7, 4)]
k = 3
clusters = kmeans(k, data_points)
print(clusters)

