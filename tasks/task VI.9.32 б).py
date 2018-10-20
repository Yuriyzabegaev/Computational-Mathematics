from SplineInterpolation import SplineInterpolation
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # Task VI.9.32 б)

    # Input
    v_x = [i * 10 for i in range(1, 11)]
    v_f = [92228496.0,
           106021537.0,
           123202624.0,
           132164569.0,
           151325798.0,
           179323175.0,
           203211926.0,
           226545805.0,
           248709873.0,
           281421906.0]

    f = SplineInterpolation(v_x, v_f)
    x = np.linspace(v_x[0], v_x[-1], 400, endpoint=True)
    y = [f(x) for x in x]
    plt.plot(x, y, 'r')

    # f = SplineInterpolation(v_x, v_f)

    print('difference in extrapolation: ' + str(f(110) - 308745538))

    plt.show()
