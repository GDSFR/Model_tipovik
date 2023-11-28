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


def simp_min(hills):
    Fmin = input_F(hills[0][1], hills[0][2])
    global Fstep
    for i in hills:
        Fstep = input_F(i[0], i[1])
        if Fstep < Fmin:
            Fmin = Fstep
    return Fmin

def simplex_method(start, a, e, axes):
    x_cur = start[0]
    y_cur = start[1]
    way = [[x_cur, y_cur]]
    global F_min
    global F_step
    F_min = input_F(x_cur, y_cur)
    hills = [[x_cur - a / 2, y_cur - 0.29 * a], [x_cur + a / 2, y_cur - 0.29 * a], [x_cur, y_cur + 0.58 * a]]

    for i in range(len(hills)):
        way.append(hills[i])

    simp_min(hills)

    return 0


def Hooke_Jeeves(start, step_x, step_y, e, axes):
    x_cur = start[0]
    y_cur = start[1]
    way = [[x_cur, y_cur]]
    global F_min
    global F_step
    F_min = input_F(x_cur, y_cur)

    while step_x > e or step_y > e:
        x_cur -= step_x
        y_cur -= step_y
        F_step = input_F(x_cur, y_cur)
        if F_min > F_step:
            way.append([x_cur, y_cur])
            F_min = F_step
            continue
        else:
            x_cur += step_x
            y_cur += step_y

        x_cur -= step_x
        y_cur += step_y
        F_step = input_F(x_cur, y_cur)
        if F_min > F_step:
            way.append([x_cur, y_cur])
            F_min = F_step
            continue
        else:
            x_cur += step_x
            y_cur -= step_y

        x_cur += step_x
        y_cur -= step_y
        F_step = input_F(x_cur, y_cur)
        if F_min > F_step:
            way.append([x_cur, y_cur])
            F_min = F_step
            continue
        else:
            x_cur -= step_x
            y_cur += step_y

        x_cur += step_x
        y_cur += step_y
        F_step = input_F(x_cur, y_cur)
        if F_min > F_step:
            way.append([x_cur, y_cur])
            F_min = F_step
            continue
        else:
            x_cur -= step_x
            y_cur -= step_y

        step_x /= 2
        step_y /= 2
    to_plot(way, 'y', axes, -15, 18)


def Gauss_Zeudel(start, step_x, step_y, e, axes):
    x_cur = start[0]
    y_cur = start[1]
    way = [[x_cur, y_cur]]
    global F_min
    global F_step
    F_min = input_F(x_cur, y_cur)

    while step_x > e or step_y > e:
        x_cur -= step_x
        F_step = input_F(x_cur, y_cur)
        if F_min > F_step:
            way.append([x_cur, y_cur])
            F_min = F_step
            continue
        else:
            x_cur += step_x

        y_cur -= step_y
        F_step = input_F(x_cur, y_cur)
        if F_min > F_step:
            way.append([x_cur, y_cur])
            F_min = F_step
            continue
        else:
            y_cur += step_y

        x_cur += step_x
        F_step = input_F(x_cur, y_cur)
        if F_min > F_step:
            way.append([x_cur, y_cur])
            F_min = F_step
            continue
        else:
            x_cur -= step_x

        y_cur += step_y
        F_step = input_F(x_cur, y_cur)
        if F_min > F_step:
            way.append([x_cur, y_cur])
            F_min = F_step
            continue
        else:
            y_cur -= step_y

        step_x /= 2
        step_y /= 2
    to_plot(way, 'b', axes, -15, 20)


if __name__ == "__main__":
    plt.xlim(-15, 30)
    plt.ylim(-25, 15)
    plt.grid()
    axes = plt.gca()
    axes.set_aspect("equal")

    e = 0.2
    a = 2
    start = [10, 8]
    step_x = 2
    step_y = 2

    draw_axes(axes)
    draw_func()
    Gauss_Zeudel(start, step_x, step_y, e, axes)
    Hooke_Jeeves(start, step_x, step_y, e, axes)
    simplex_method(start, step_x, step_y, e, axes)
    plt.show()
