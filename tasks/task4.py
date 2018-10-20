import numpy as np
import matplotlib.pyplot as plt

from SplineInterpolation import SplineInterpolation


if __name__ == '__main__':

    # Task 4

    # Input:

    v_x = [0, 0.2, 0.4, 0.6, 0.8, 1., 1.2, 1.4, 1.6, 1.8, 2., 2.2, 2.4, 2.6, 2.8, 3]
    v_f = [0, 1.09351, -0.47812, -0.0620008, 0.965999, -0.960168, -1.421145, -0.328504, -1.88517, -2.36515, 2.33714, -0.684984,
    -0.695581, 1.9807, 2.44249, 3.48356]

    point1 = 0.7
    point2 = 1.5
    point3 = 2.3

    # Solution:

    spline = SplineInterpolation(v_x, v_f)

    x = np.linspace(v_x[0], v_x[-1], 400, endpoint=True)
    y = [spline(x) for x in x]
    plt.plot(x, y, 'r')
    plt.show()
    print(spline(point1))
    print(spline(point2))
    print(spline(point3))
