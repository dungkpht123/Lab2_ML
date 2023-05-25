# Dữ liệu người dùng và đánh giá sách
users = {
    'User1': {'Sách 1': 5, 'Sách 2': 4, 'Sách 3': 3, 'Sách 4': 2},
    'User2': {'Sách 1': 3, 'Sách 2': 4, 'Sách 3': 2, 'Sách 5': 5},
    'User3': {'Sách 1': 2, 'Sách 2': 3, 'Sách 3': 4, 'Sách 4': 5},
    'User4': {'Sách 2': 5, 'Sách 3': 3, 'Sách 5': 4},
    'User5': {'Sách 1': 4, 'Sách 3': 5, 'Sách 4': 2, 'Sách 5': 3}
}

# Hàm tính độ tương tự giữa hai người dùng dựa trên đánh giá sách
def calculate_similarity(user1, user2):
    common_books = set(user1.keys()) & set(user2.keys())  # Tìm các sách chung
    if len(common_books) == 0:
        return 0  # Trường hợp không có sách chung
    
    # Tính toán độ tương tự dựa trên đánh giá sách chung
    squared_diff_sum = sum((user1[book] - user2[book]) ** 2 for book in common_books)
    similarity = 1 / (1 + squared_diff_sum)
    return similarity

# Hàm gợi ý sách cho một người dùng dựa trên đánh giá của các người dùng khác
def recommend_books(user, n):
    similarities = {}  # Từ điển lưu trữ độ tương tự với các người dùng khác
    
    # Tính toán độ tương tự với các người dùng khác
    for other_user in users:
        if other_user != user:
            similarity = calculate_similarity(users[user], users[other_user])
            similarities[other_user] = similarity
    
    # Sắp xếp các người dùng khác theo độ tương tự giảm dần
    sorted_users = sorted(similarities, key=similarities.get, reverse=True)
    
    recommendations = []  # Danh sách sách gợi ý
    
    # Gợi ý sách dựa trên đánh giá của người dùng khác
    for other_user in sorted_users:
        other_user_books = users[other_user]
        for book in other_user_books:
            if book not in users[user]:
                recommendations.append((book, other_user_books[book] * similarities[other_user]))
    
    # Sắp xếp danh sách gợi ý theo độ ưu tiên giảm dần
    recommendations.sort(key=lambda x: x[1], reverse=True)
    
    # Trả về n sách có độ ưu tiên cao nhất
    return [book for book, _ in recommendations[:n]]

# Gợi ý 3 sách cho người dùng "User1"
recommended_books = recommend_books('User2', 3)

# In kết quả gợi ý
for book in recommended_books:
    print(book)
