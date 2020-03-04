import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def init():
    points = np.array([[0, 0], [100, 0], [50, 80]])  # 三点坐标
    m = np.array([0, 0])  # 初始点坐标
    return points, m


def coordinates_transform(m, point):
    return m + (point - m) / 2


def IFS(m, points, iters, p=None):  # Sierpinski triangle
    trajectory = np.zeros((iters+1, 2))
    for i in range(iters):
        idx = np.random.choice([0, 1, 2], p=p)
        m = coordinates_transform(m, points[idx])
        trajectory[i+1] = m
    return trajectory


def update(frame):
    ax.scatter(trajectory[frame, 0], trajectory[frame, 1], c='b', s=1)
    return ax,


def fig_init():
    ax.scatter(m[0], m[1], c='b', s=1)
    return ax,


if __name__ == '__main__':
    points, m = init()
    trajectory = IFS(m, points, 100000)  # p 为概率
    fig, ax = plt.subplots()
    ax.scatter(points[:, 0], points[:, 1], c='r')
    # anim = FuncAnimation(fig, update, frames=10000, interval=20, blit=True)
    ax.scatter(trajectory[:, 0], trajectory[:, 1], c='b', s=1)
    plt.show()

