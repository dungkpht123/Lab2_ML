import numpy as np
from sklearn.model_selection import train_test_split

# Định nghĩa lớp cây quyết định
class DecisionTree:
    def __init__(self, max_depth=None):
        self.max_depth = max_depth

    def fit(self, X, y):
        self.n_classes = len(np.unique(y))
        self.n_features = X.shape[1]
        self.tree = self._build_tree(X, y)

    def predict(self, X):
        return np.array([self._predict(x, self.tree) for x in X])

    def _build_tree(self, X, y, depth=0):
        n_samples_per_class = [np.sum(y == i) for i in range(self.n_classes)]
        predicted_class = np.argmax(n_samples_per_class)

        node = {'predicted_class': predicted_class}

        if depth < self.max_depth:
            feature, threshold = self._find_best_split(X, y)
            if feature is not None and threshold is not None:
                indices_left = X[:, feature] < threshold
                X_left, y_left = X[indices_left], y[indices_left]
                X_right, y_right = X[~indices_left], y[~indices_left]

                node['feature'] = feature
                node['threshold'] = threshold
                node['left'] = self._build_tree(X_left, y_left, depth + 1)
                node['right'] = self._build_tree(X_right, y_right, depth + 1)

        return node

    def _find_best_split(self, X, y):
        best_gini = 1.0
        best_feature = None
        best_threshold = None

        for feature in range(self.n_features):
            thresholds = np.unique(X[:, feature])
            for threshold in thresholds:
                gini = self._gini_index(X, y, feature, threshold)
                if gini < best_gini:
                    best_gini = gini
                    best_feature = feature
                    best_threshold = threshold

        return best_feature, best_threshold

    def _gini_index(self, X, y, feature, threshold):
        indices_left = X[:, feature] < threshold
        y_left = y[indices_left]
        y_right = y[~indices_left]

        gini_left = 1.0 - sum((np.sum(y_left == i) / len(y_left)) ** 2 for i in range(self.n_classes))
        gini_right = 1.0 - sum((np.sum(y_right == i) / len(y_right)) ** 2 for i in range(self.n_classes))

        gini_index = (len(y_left) * gini_left + len(y_right) * gini_right) / len(y)

        return gini_index

    def _predict(self, x, node):
        if 'predicted_class' in node:
            return node['predicted_class']
        
        if x[node['feature']] < node['threshold']:
            return self._predict(x, node['left'])
        else:
            return self._predict(x, node['right'])


# Load dữ liệu Iris
X = np.array([
    [5.1, 3.5, 1.4, 0.2],
    [4.9, 3.0, 1.4, 0.2],
    [4.7, 3.2, 1.3, 0.2],
    [7.0, 3.2, 4.7, 1.4],
    [6.4, 3.2, 4.5, 1.5],
    [6.9, 3.1, 4.9, 1.5],
    [6.3, 3.3, 6.0, 2.5],
    [5.8, 2.7, 5.1, 1.9],
    [7.1, 3.0, 5.9, 2.1],
    [6.3, 2.9, 5.6, 1.8],
    [6.5, 3.0, 5.8, 2.2],
    [7.6, 3.0, 6.6, 2.1],
    [4.9, 2.5, 4.5, 1.7],
    [7.3, 2.9, 6.3, 1.8],
    [6.7, 2.5, 5.8, 1.8],
    [6.2, 3.4, 5.4, 2.3],
    [5.9, 3.0, 5.1, 1.8],
    # ...Thêm các dữ liệu vào đây
])
y = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2])  # Nhãn tương ứng

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Xây dựng mô hình Rừng quyết định
model = DecisionTree(max_depth=3)
model.fit(X_train, y_train)

# Dự đoán nhãn cho tập kiểm tra
y_pred = model.predict(X_test)

# Đánh giá độ chính xác
accuracy = np.mean(y_pred == y_test)
print("Độ chính xác:", accuracy)
