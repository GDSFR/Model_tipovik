import numpy as np

from plots_and_func import *


def calc_plan(x, y):
    return [[x - 1, y - 1, input_F(x - 1, y - 1)],
            [x + 1, y - 1, input_F(x + 1, y - 1)],
            [x - 1, y + 1, input_F(x - 1, y + 1)],
            [x + 1, y + 1, input_F(x + 1, y + 1)]]


def calc_regression(plan):
    vals = []
    for i in plan:
        vals.append(i[2])
    b1 = (- vals[0] + vals[1] - vals[2] + vals[3]) / 4
    b2 = (- vals[0] - vals[1] + vals[2] + vals[3]) / 4
    return [b1, b2]


def calc_step(regres, a):
    hx = a * 1 * regres[0]
    hy = a * 1 * regres[1]
    return [hx, hy]

def check_cycle(regression, e):
    if np.sqrt(regression[0]**2 + regression[1]**2) < e:
        return False
    return True

def downhill_method(start, axes, a, e):
    x_cur = start[0]
    y_cur = start[1]
    way = [[x_cur, y_cur, round(input_F(x_cur, y_cur), 4)]]
    global F_step
    global c
    c = 0
    plan = calc_plan(x_cur, y_cur)
    regression = calc_regression(plan)

    while check_cycle(regression, e):
        plan = calc_plan(x_cur, y_cur)
        regression = calc_regression(plan)
        step = calc_step(regression, a)

        enter_point = [x_cur, y_cur, round(input_F(x_cur, y_cur), 4)]
        point_step = [x_cur - step[0], y_cur - step[1], round(input_F(x_cur - step[0], y_cur - step[1]), 4)]
        while point_step[2] < enter_point[2]:
            enter_point = point_step
            point_step = [round(enter_point[0] - step[0], 4), round(enter_point[1] - step[1], 4),
                          round(input_F(enter_point[0] - step[0], enter_point[1] - step[1]), 4)]
            x_cur = enter_point[0]
            y_cur = enter_point[1]
        c += 1
        way.append(enter_point)

    print(way)
    to_plot(way, 'orange', axes, -15, 16)
