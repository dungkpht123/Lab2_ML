import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

class PCA:
  def __init__(self, n_dimention: int):
    self.n_dimention = n_dimention

  def fit_transform(self, X):
    mean = np.mean(X, axis=0)
    X = X - mean
    cov = X.T.dot(X) / X.shape[0] 
    eigen_values, eigen_vectors, = np.linalg.eig(cov)
    select_index = np.argsort(eigen_values)[::-1][:self.n_dimention]
    U = eigen_vectors[:, select_index]
    X_new = X.dot(U)
    return X_new
    
if __name__ == "__main__":
  df = pd.read_csv(r"/content/iris.csv")
  X = df[["sepal_length",	"sepal_width",	"petal_length",	"petal_width"]].to_numpy()
  Y = df["species"].to_numpy()

  pca = PCA(n_dimention=2)
  new_X = pca.fit_transform(X)
  
  for label in set(Y):
    X_class = new_X[Y == label]
    plt.scatter(X_class[:, 0], X_class[:, 1], label=label)

  plt.legend()