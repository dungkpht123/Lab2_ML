# Dữ liệu phim (tên phim và thể loại)
movies = {
    'Phim 1': ['Hành động', 'Phiêu lưu'],
    'Phim 2': ['Tình cảm', 'Lãng mạn'],
    'Phim 3': ['Hài', 'Tâm lý'],
    'Phim 4': ['Khoa học viễn tưởng', 'Phiêu lưu'],
    'Phim 5': ['Hành động', 'Tâm lý'],
    'Phim 6': ['Tình cảm', 'Lãng mạn'],
    'Phim 7': ['Hài', 'Tâm lý']
}

# Hàm gợi ý phim tương tự dựa trên thể loại
def recommend_movies(movie, n):
    movie_genres = movies[movie]  # Lấy thể loại của phim đầu vào
    recommendations = []  # Danh sách phim gợi ý
    
    # Duyệt qua tất cả các phim và tìm các phim có thể loại tương tự
    for title, genres in movies.items():
        if title != movie:
            common_genres = set(movie_genres) & set(genres)  # Tìm các thể loại chung
            similarity = len(common_genres) / len(movie_genres)  # Tính độ tương đồng
            recommendations.append((title, similarity))
    
    # Sắp xếp danh sách gợi ý theo độ tương đồng giảm dần
    recommendations.sort(key=lambda x: x[1], reverse=True)
    
    # Trả về n phim có độ tương đồng cao nhất
    return recommendations[:n]

# Gợi ý 3 phim tương tự với phim "Phim 1"
recommended_movies = recommend_movies('Phim 3', 6);
print(recommended_movies);
# In kết quả gợi ý
for movie, similarity in recommended_movies:
    print(movie)