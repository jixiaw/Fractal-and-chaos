from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np


def LogisticMap():
    mu = np.arange(2.5, 4, 0.0001)
    x = 0.2
    iters = 1000
    last = 100
    # result = np.zeros((iters+last, len(mu)))
    for i in tqdm(range(iters+last)):
        x = mu * x * (1 - x)
        if i >= iters:
            plt.plot(mu, x, ',k', alpha=0.25)
    plt.show()


if __name__ == '__main__':
    LogisticMap()
