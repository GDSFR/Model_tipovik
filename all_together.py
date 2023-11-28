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


def simplex_method(start, a, e, axes):
    x_cur = start[0]
    y_cur = start[1]
    way = [[x_cur, y_cur, input_F(x_cur, y_cur)]]
    global F_step
    last_hills2 = [[[0], [0], [0]], [[0], [0], [0]]]
    global c
    hills = hills_calc(x_cur, y_cur, a)
    for i in range(len(hills)):
        hills[i].append(round(input_F(hills[i][0], hills[i][1]), 4))
        way.append(hills[i])
    while a > e:
        print(hills)
        Fmax = simp_max(hills)

        # new_hill = [hills[0][0] + hills[1][0] - hills[2][0], hills[0][1] + hills[1][1] - hills[2][1]]
        for i in range(len(hills)):
            if hills[i] == Fmax:
                last_hills2.append(hills.copy())
                last_hills2.remove(last_hills2[0])
                hills.remove(hills[i])
                hills.append(
                    [round(hills[0][0] + hills[1][0] - Fmax[0], 4), round(hills[0][1] + hills[1][1] - Fmax[1], 1)])
                way.append(hills[-1])
                way[-1].append(round(input_F(way[-1][0], way[-1][1]), 4))
                x_cur = hills[-1][0]
                y_cur = hills[-1][1]
                break
        if ((last_hills2[0][2] == hills[2])
                or (last_hills2[1][2] == hills[2])):
            a /= 2
            hills = hills_calc(x_cur, y_cur, a)
    print(way)
    to_plot(way, 'y', axes, -15, 16)


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
            way.append([x_cur, y_cur, input_F(x_cur, y_cur)])
            F_min = F_step
            continue
        else:
            x_cur += step_x
            y_cur += step_y

        x_cur -= step_x
        y_cur += step_y
        F_step = input_F(x_cur, y_cur)
        if F_min > F_step:
            way.append([x_cur, y_cur, input_F(x_cur, y_cur)])
            F_min = F_step
            continue
        else:
            x_cur += step_x
            y_cur -= step_y

        x_cur += step_x
        y_cur -= step_y
        F_step = input_F(x_cur, y_cur)
        if F_min > F_step:
            way.append([x_cur, y_cur, input_F(x_cur, y_cur)])
            F_min = F_step
            continue
        else:
            x_cur -= step_x
            y_cur += step_y

        x_cur += step_x
        y_cur += step_y
        F_step = input_F(x_cur, y_cur)
        if F_min > F_step:
            way.append([x_cur, y_cur, input_F(x_cur, y_cur)])
            F_min = F_step
            continue
        else:
            x_cur -= step_x
            y_cur -= step_y

        step_x /= 2
        step_y /= 2
    print(way)
    to_plot(way, 'r', axes, -15, 18)


def Gauss_Zeudel(start, step_x, step_y, e, axes):
    x_cur = start[0]
    y_cur = start[1]
    way = [[x_cur, y_cur, input_F(x_cur, y_cur)]]
    global F_min
    global F_step
    F_min = input_F(x_cur, y_cur)

    while step_x > e or step_y > e:
        x_cur -= step_x
        F_step = input_F(x_cur, y_cur)
        if F_min > F_step:
            way.append([x_cur, y_cur, input_F(x_cur, y_cur)])
            F_min = F_step
            continue
        else:
            x_cur += step_x

        y_cur -= step_y
        F_step = input_F(x_cur, y_cur)
        if F_min > F_step:
            way.append([x_cur, y_cur, input_F(x_cur, y_cur)])
            F_min = F_step
            continue
        else:
            y_cur += step_y

        x_cur += step_x
        F_step = input_F(x_cur, y_cur)
        if F_min > F_step:
            way.append([x_cur, y_cur, input_F(x_cur, y_cur)])
            F_min = F_step
            continue
        else:
            x_cur -= step_x

        y_cur += step_y
        F_step = input_F(x_cur, y_cur)
        if F_min > F_step:
            way.append([x_cur, y_cur, input_F(x_cur, y_cur)])
            F_min = F_step
            continue
        else:
            y_cur -= step_y

        step_x /= 2
        step_y /= 2
    print(way)
    to_plot(way, 'b', axes, -15, 20)

def simp_max(hills):
    hill_max_val = input_F(hills[0][0], hills[0][1])
    global Fstep
    global hill_max
    for i in hills:
        Fstep = input_F(i[0], i[1])
        if Fstep > hill_max_val:
            hill_max = i
    return hill_max


def hills_calc(x, y, a):
    res = [[], [], []]
    return [[round(x - a / 2, 4), round(y - 0.29 * a, 4)], [round(x + a / 2, 4), round(y - 0.29 * a, 4)],
            [round(x, 4), round(y + 0.58 * a, 4)]]


def simp_min(hills):
    hill_min_val = input_F(hills[0][0], hills[0][1])
    global Fstep
    hill_min = 0
    for i in hills:
        Fstep = input_F(i[0], i[1])
        if Fstep <= hill_min_val:
            hill_min = i
    return hill_min

def Nelder_Mead(start, a, e, axes):
    x_cur = start[0]
    y_cur = start[1]
    way = [[x_cur, y_cur, input_F(x_cur, y_cur)]]
    global F_step
    last_hills2 = [[[0], [0], [0]], [[0], [0], [0]]]
    global c
    hills = hills_calc(x_cur, y_cur, a)
    for i in range(len(hills)):
        hills[i].append(round(input_F(hills[i][0], hills[i][1]), 4))
        way.append(hills[i])
    while a > e:
        print(hills)
        Fmax = simp_max(hills)
        Fmin = simp_min(hills)
        for i in range(len(hills)):
            if hills[i] == Fmax:
                last_hills2.append(hills.copy())
                last_hills2.remove(last_hills2[0])
                hills.remove(hills[i])
                hills.append(
                    [round(hills[0][0] + hills[1][0] - Fmax[0], 4), round(hills[0][1] + hills[1][1] - Fmax[1], 1)])
                break
        for i in range(len(hills)):
            if hills[i] == Fmin:
                hills.remove(hills[i])
                hills.append(Fmin)
                hill_stretch = [round(2 * hills[-1][0] - (hills[0][0] + hills[1][0]) / 2, 4),
                                round(2 * hills[-1][1] - (hills[0][1] + hills[1][1]) / 2, 4),
                                round(input_F(round(2 * hills[-1][0] - (hills[0][0] + hills[1][0]) / 2, 4),
                                              round(2 * hills[-1][1] - (hills[0][1] + hills[1][1]) / 2, 4)))]
                hills.remove(hills[-1])
                hills.append(hill_stretch)
                way.append(hills[-1])
                # way[-1].append(round(input_F(way[-1][0], way[-1][1]), 4))
                x_cur = hills[-1][0]
                y_cur = hills[-1][1]

        if ((last_hills2[0][2] == hills[2])
                or (last_hills2[1][2] == hills[2])):
            a /= 2
            hills = hills_calc(x_cur, y_cur, a)
    print(way)
    to_plot(way, "purple", axes, -15, 16)


def main():
    return 0


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
    # Gauss_Zeudel(start, step_x, step_y, e, axes)
    # Hooke_Jeeves(start, step_x, step_y, e, axes)
    # simplex_method(start, a, e, axes)
    Nelder_Mead(start, a, e, axes)
    plt.show()
