import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm


def mandelbort_iteration(c):
    z = c
    for i in range(100):
        if abs(z) > 2:
            break
        z = z * z + c
    return i


def julia_iteration(z, c):
    for i in range(100):
        if abs(z) > 2:
            break
        z = z * z + c
    return i


def mandelbort_set(xl, xr, yl, yr):
    y, x = np.ogrid[yl:yr:1000j, xl:xr:1000j]
    c = x + y * 1j
    matset = np.frompyfunc(mandelbort_iteration, 1, 1)(c).astype(np.float)
    plt.imshow(matset, cmap=cm.jet, extent=(xl, xr, yl, yr))
    plt.show()


def julia_set(xl, xr, yl, yr):
    y, x = np.ogrid[yl:yr:1000j, xl:xr:1000j]
    z = x + y * 1j
    matset = np.frompyfunc(julia_iteration, 2, 1)(z, -1).astype(np.float)
    plt.imshow(matset, cmap=cm.jet, extent=(xl, xr, yl, yr))
    plt.show()


if __name__ == '__main__':
    mandelbort_set(-2, 1, -1.5, 1.5)
    # julia_set(-2, 2, -2, 2)