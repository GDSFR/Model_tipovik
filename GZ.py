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
    plt.text(3, 18, f"Значения построенных ф-ций:{f_vals}")
    for i in f_vals:
        x_p = - y + np.sqrt(i - (y + 6) ** 2)
        x_n = - y - np.sqrt(i - (y + 6) ** 2)
        # F = (x + y)**2 + (y + 6)**2
        plt.plot(x_p, y, 'g')
        plt.plot(x_n, y, 'g')


def GZ_F(x, y):
    return (x + y) ** 2 + (y + 6) ** 2


def Gauss_Zeudel(axes):
    e = 0.2
    start = [10, 8]
    x_cur = start[0]
    y_cur = start[1]
    way = [[x_cur, y_cur]]
    step_x = 2;
    step_y = 2;
    global F_min
    global F_step
    F_min = GZ_F(x_cur, y_cur)

    while step_x > e or step_y > e:
        x_cur -= step_x
        F_step = GZ_F(x_cur, y_cur)
        if F_min > F_step:
            line = plt.Line2D([x_cur + step_x, x_cur], [y_cur, y_cur], color="red")
            axes.add_line(line)
            way.append([x_cur, y_cur])
            F_min = F_step
            continue
        else:
            x_cur += step_x

        y_cur -= step_y
        F_step = GZ_F(x_cur, y_cur)
        if F_min > F_step:
            line = plt.Line2D([x_cur, x_cur], [y_cur + step_y, y_cur], color="red")
            axes.add_line(line)
            way.append([x_cur, y_cur])
            F_min = F_step
            continue
        else:
            y_cur += step_y

        x_cur += step_x
        F_step = GZ_F(x_cur, y_cur)
        if F_min > F_step:
            line = plt.Line2D([x_cur - step_x, x_cur], [y_cur, y_cur], color="red")
            axes.add_line(line)
            way.append([x_cur, y_cur])
            F_min = F_step
            continue
        else:
            x_cur -= step_x

        y_cur += step_y
        F_step = GZ_F(x_cur, y_cur)
        if F_min > F_step:
            line = plt.Line2D([x_cur, x_cur], [y_cur - step_y, y_cur], color="red")
            axes.add_line(line)
            way.append([x_cur, y_cur])
            F_min = F_step
            continue
        else:
            y_cur -= step_y

        step_x /= 2
        step_y /= 2

    plt.text(-20, 18, f"Начало: {start}\nКонец: {way[-1]}")

if __name__ == "__main__":
    plt.xlim(-15, 30)
    plt.ylim(-25, 15)
    plt.grid()
    axes = plt.gca()
    axes.set_aspect("equal")

    draw_axes(axes)
    draw_func()
    Gauss_Zeudel(axes)
    plt.show()
