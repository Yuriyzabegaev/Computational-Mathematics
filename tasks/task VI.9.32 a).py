from NewtonInterpolation import NewtonInterpolation
import numpy as np
import math
import matplotlib.pyplot as plt



if __name__ == "__main__":
    # Task VI.9.32 a)

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

    # Solution
    n = NewtonInterpolation(x=v_x,
                            f_x=v_f).get_polynomial_function()

    # f = SplineInterpolation(x, y)
    x = np.linspace(v_x[0], v_x[-1], 400, endpoint=True)
    y = [n(x) for x in x]
    plt.plot(x, y, 'r')
    plt.show()

    print('difference in extrapolation: ' + str(n(110) -  308745538))
