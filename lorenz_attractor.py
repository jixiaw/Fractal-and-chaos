from tqdm import tqdm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import numpy as np


def mkpoints(x=0.0, y=0.0, z=0.0):
    xlist, ylist, zlist = [], [], []
    sigma, R, beta = 10, 28, 8/3
    x0, y0, z0 = x, y, z
    h = 0.01
    for i in tqdm(range(10000)):
        x1 = h * (sigma * (y0 - x0)) + x0
        y1 = h * (x0 * (R - z0) - y0) + y0
        z1 = h * (x0 * y0 - beta * z0) + z0
        xlist.append(x1)
        ylist.append(y1)
        zlist.append(z1)
        x0, y0, z0 = x1, y1, z1
    return xlist, ylist, zlist


def LorenzAttractor():
    fig = plt.figure()
    ax = Axes3D(fig)
    xlist, ylist, zlist = mkpoints(1, 0, 0)
    ax.plot(xlist, ylist, zlist)
    # xlist, ylist, zlist = mkpoints(1.001, 0, 0)
    # ax.plot(xlist, ylist, zlist)
    plt.show()


# def update(frame):
#     ax.scatter(xlist[frame], ylist[frame], zlist[frame], c='r')
#     return ax


if __name__ == '__main__':
    # fig = plt.figure()
    # ax = Axes3D(fig)
    # ax.scatter(1, 0, 0, c='r')
    # xlist, ylist, zlist = mkpoints(1, 0, 0)
    # anim = FuncAnimation(fig, update, frames=10000, interval=200)
    # plt.show()
    LorenzAttractor()