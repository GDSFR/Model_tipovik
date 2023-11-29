import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.lines import Line2D

def draw_axes(axes):
    x0 = -15
    y0 = 0

    x1 = 30
    y1 = 0

    line = plt.Line2D([x0, x1], [y0, y1], color="black")
    axes.add_line(line)
    x0 = 0
    y0 = -25

    x1 = 0
    y1 = 15
    line = plt.Line2D([x0, x1], [y0, y1], color="black")
    axes.add_line(line)


def draw_func():
    #    x = np.linspace(-30, 30)
    y = np.linspace(-30, 30, 30000)
    f_vals = [25, 50, 100, 200]
    plt.text(3, -30, f"Значения построенных ф-ций:{f_vals}")
    for i in f_vals:
        x_p = - y + np.sqrt(i - (y + 6) ** 2)
        x_n = - y - np.sqrt(i - (y + 6) ** 2)
        # F = (x + y)**2 + (y + 6)**2
        plt.plot(x_p, y, 'g')
        plt.plot(x_n, y, 'g')


def input_F(x, y):
    return (x + y) ** 2 + (y + 6) ** 2


def to_plot(way, color, axes, x_pos, y_pos):
    plt.text(x_pos, y_pos, f"Начало: {way[0]} Конец: {way[-1]} Число шагов: {len(way)}")
    for i in range(len(way)):
        plt.scatter(way[i][0], way[i][1], s=10, c=color)
        if i != 0:
            line = plt.Line2D([way[i - 1][0], way[i][0]], [way[i - 1][1], way[i][1]], c=color)
            axes.add_line(line)
        # plt.plot(line)
