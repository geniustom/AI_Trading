from numpy import array, dot, mean, std, empty, argsort
from numpy.linalg import eigh, solve
from numpy.random import randn
from matplotlib.pyplot import subplots, show
from sklearn.decomposition import PCA


def pca2(data, pc_count = None):
    return PCA(n_components = 4).fit(data).transform(data)

def cov(data):
    """
        covariance matrix
        note: specifically for mean-centered data
    """
    N = data.shape[1]
    C = empty((N, N))
    for j in range(N):
        C[j, j] = mean(data[:, j] * data[:, j])
        for k in range(N):
            C[j, k] = C[k, j] = mean(data[:, j] * data[:, k])
    return C

def pca(data, pc_count = None):
    """
        Principal component analysis using eigenvalues
        note: this mean-centers and auto-scales the data (in-place)
    """
    data -= mean(data, 0)
    data /= std(data, 0)
    C = cov(data)
    E, V = eigh(C)
    key = argsort(E)[::-1][:pc_count]
    E, V = E[key], V[:, key]
    U = dot(V.T, data.T).T
    return U, E, V

""" test data """
data = array([randn(8) for k in range(150)])
data[:50, 2:4] += 5
data[50:, 2:5] += 5

""" visualize """
T= pca(data, 3)
trans = T[0]
fig, (ax1, ax2) = subplots(1, 2)
ax1.scatter(data[:50, 0], data[:50, 1], c = 'r')
ax1.scatter(data[50:, 0], data[50:, 1], c = 'b')
ax2.scatter(trans[:50, 0], trans[:50, 1], c = 'r')
ax2.scatter(trans[50:, 0], trans[50:, 1], c = 'b')
show()