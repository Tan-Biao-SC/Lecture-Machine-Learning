import numpy as np
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
import pandas as pd

fn = "yhkdx.csv"
df = pd.read_csv(fn)
sub_df = df.values[:, ]
X = sub_df[:, 1:]

# K = range(1, 10)
# mean_dist = []
# for k in K:
#     kmeans = KMeans(n_clusters=k)
#     kmeans.fit(X)
#     mean_dist.append(sum(np.min(cdist(X, kmeans.cluster_centers_, 'euclidean'), axis=1)) / X.shape[0])
# plt.plot(K, mean_dist, 'bx-')
# plt.xlabel('k')
# plt.ylabel('SSE')
# plt.title('Selecting k with the Elbow Method')
# plt.show()


kmeans = KMeans(n_clusters=2)
kmeans.fit(X)
nar = kmeans.labels_
for i in range(len(nar)):
    print(sub_df[i][0], "\t:type_%d" % nar[i])

# from sklearn.decomposition import PCA
# pca = PCA(n_components=2)
# pca.fit(X)
# X_new = pca.transform(X)
# plt.scatter(X_new[:, 0], X_new[:, 1], marker='o', c=nar)
# plt.show()

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
lda = LinearDiscriminantAnalysis()
lda.fit(X, nar)
X_new = lda.transform(X)
Y_new = np.random.rand(len(nar))
plt.scatter(X_new, Y_new, marker='s', c=nar)
plt.show()

