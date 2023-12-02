import numpy as np
import matplotlib.pyplot as plt

from plots_and_func import draw_axes, draw_func
from GZ_method import Gauss_Zeudel
from HJ_method import Hooke_Jeeves
from simplex1 import simplex_method
from simplex2 import simplex_method_Nelder_Mead
from downhill_method import downhill_method

if __name__ == "__main__":
    plt.xlim(-15, 30)
    plt.ylim(-25, 15)
    plt.grid()
    axes = plt.gca()
    axes.set_aspect("equal")

    e = 0.124
    a1 = 2
    a2 = 2
    a_d = 0.1
    start = [10, 8]
    step_x = 2
    step_y = 2

    draw_axes(axes)
    draw_func()
    Gauss_Zeudel(start, step_x, step_y, e, axes)
    Hooke_Jeeves(start, step_x, step_y, e, axes)
    simplex_method(start, a1, e, axes)
    simplex_method_Nelder_Mead(start, a2, e, axes)
    downhill_method(start, axes, a_d, e)


    plt.show()
