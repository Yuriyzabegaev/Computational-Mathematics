import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

from SimpleIterationMethod import simple_iteration_root_searcher
from DichotomyRootSearcher import dichotomy_root_searcher


if __name__ == '__main__':

    # Task 2

    # Input:

    x = sp.Symbol('x')
    func = (x) * sp.cos(x) - 0.56
    bounds = [-2, 2]
    error = 10 ** (-6)

    # Solution:

    # отрезки на которых один корень найдем графически

    y = sp.lambdify(x, func, 'numpy')

    t_list = np.linspace(bounds[0], bounds[1], 120, endpoint=True)
    y_list = [y(x) for x in t_list]

    plt.plot(t_list, y_list, 'b')
    plt.plot([-2, 2], [0, 0], 'r')
    plt.show()

    # визуально есть 2 корня на отрезках [-2, -1.5] и [0.5, 1.5]

    sections = [[-2, -1.5], [0.5, 1.5]]

    # fi(x) = x = arccos(0.56/x)
    # fi'(x) = 0.56/(x^2*sqrt(1-0.56/x)), условие сходимости выполняется на отрезках (проверено графически)

    # отрезок не входит в область определения arccos, поэтому применен метод дихотомии
    fi = 0.56/sp.cos(x)
    print('First of roots: ' + str(dichotomy_root_searcher(x, fi, (sections[0][0], sections[0][1]), error=error)))

    fi = sp.acos(0.56/x)
    print('Second of roots: ' + str(simple_iteration_root_searcher(x, fi, sections[1][0], sections[1][1], error=error)))

