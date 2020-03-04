import numpy as np
import matplotlib.pyplot as plt


def fractal(iters=1000):
    eq1 = np.array([[0, 0, 0], [0, 0.16, 0]])
    eq2 = np.array([[0.2, -0.26, 0], [0.23, 0.22, 1.6]])
    eq3 = np.array([[-0.15, 0.28, 0], [0.26, 0.24, 0.44]])
    eq4 = np.array([[0.85, 0.04, 0], [-0.04, 0.85, 1.6]])
    p = [0.01, 0.07, 0.07, 0.85]
    m = np.array([[0], [0]])
    A = np.array((eq1, eq2, eq3, eq4))
    points = np.zeros((iters, 2))
    for i in range(iters):
        idx = np.random.choice([0, 1, 2, 3], p=p)
        m = np.dot(A[idx, :, :2], m) + A[idx, :, 2:]
        points[i] = m.T
    return points


if __name__ == '__main__':
    trajectory = fractal(10000)
    plt.scatter(trajectory[:, 0], trajectory[:, 1], c='b', s=1)
    plt.show()
