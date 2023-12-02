import numpy as np

from plots_and_func import *


def simp_max(hills):
    Fmax = hills[0]
    Fmax_val = Fmax[2]
    global Fstep
    for i in hills:
        Fstep = input_F(i[0], i[1])
        if Fstep > Fmax_val:
            Fmax_val = i[2]
            Fmax = i
    return Fmax


def simp_min(hills):
    Fmin = hills[0]
    Fmin_val = Fmin[2]
    global Fstep
    for i in hills:
        Fstep = input_F(i[0], i[1])
        if Fstep < Fmin_val:
            Fmin_val = i[2]
            Fmin = i
    return Fmin


def hills_calc(x, y, a):
    return [
        [round(x - a / 2, 4), round(y - 0.29 * a, 4), round(input_F(round(x - a / 2, 4), round(y - 0.29 * a, 4)), 4)],
        [round(x + a / 2, 4), round(y - 0.29 * a, 4), round(input_F(round(x + a / 2, 4), round(y - 0.29 * a, 4)), 4)],
        [round(x, 4), round(y + 0.58 * a, 4), round(input_F(round(x, 4), round(y + 0.58 * a, 4)), 4)]
    ]


def calc_hill_1(hills, Fmax):
    return [round(hills[0][0] + hills[1][0] - Fmax[0], 4),
            round(hills[0][1] + hills[1][1] - Fmax[1], 4),
            round(
                input_F(round(hills[0][0] + hills[1][0] - Fmax[0], 4), round(hills[0][1] + hills[1][1] - Fmax[1], 4)))]


# return [
#     [round(, 4), round(, 4), round(, 4)],
#     [round(, 4), round(, 4), round(, 4)],
#     [round(, 4), round(, 4), round(, 4)]
# ]

def calc_hill_2(hills, Fmin, a):
    return [
        round(2 * Fmin[0] - (hills[0][0] + hills[1][0]) / a, 4),
        round(2 * Fmin[1] - (hills[0][1] + hills[1][1]) / a, 4),
        round(input_F(round(2 * Fmin[0] - (hills[0][0] + hills[1][0]) / 2, 4),
                      round(2 * Fmin[1] - (hills[0][1] + hills[1][1]) / 2, 4), ), 4)
    ]


def calc_hill_2red(hills, Fmin, a, red_c):
    k = 0.5
    x_res = round(k * Fmin[0] + (hills[0][0] + hills[1][0]) / (a * 2**red_c), 4)
    y_res = round(k * Fmin[1] + (hills[0][1] + hills[1][1]) / (a * 2**red_c), 4)
    f_res = round(input_F(x_res, y_res), 4)

    res = [
        x_res,
        y_res,
        f_res
    ]
    return res


def check_red(hills):
    if hills[2] != simp_min(hills):
        return True
    return False


def check_sqrt(hills, e):
    if round(np.sqrt(hills[1][0]**2 - hills[0][0]**2), 4) < e:
        return False
    return True


def simplex_method_Nelder_Mead(start, a, e, axes):
    x_cur = start[0]
    y_cur = start[1]
    way = [[x_cur, y_cur, input_F(x_cur, y_cur)]]
    global F_step
    last_hills2 = [[[0], [0], [0]], [[0], [0], [0]]]
    global c
    global red_c
    red_c = 0
    c = 0
    k = 0.5
    hills = hills_calc(x_cur, y_cur, a)
    for i in range(len(hills)):
        way.append(hills[i])
    while check_sqrt(hills, e):
        print(f"Step:\n{hills}")
        Fmax = simp_max(hills)
        c += 1
        last_hills2.append(hills.copy())
        last_hills2.remove(last_hills2[0])
        # new_hill = [hills[0][0] + hills[1][0] - hills[2][0], hills[0][1] + hills[1][1] - hills[2][1]]
        for i in hills:
            if i == Fmax:
                hills.remove(i)
                hills.append(calc_hill_1(hills, Fmax))
                break
#        print(f"- max, + better hill :\n{hills}")

        Fmin = simp_min(hills)
        for i in hills:
            if i == Fmin:
                hill_min = calc_hill_2(hills, Fmin, a)
#                print(f"hill_min: \n{hill_min}")
                if hill_min[2] < hills[2][2]:
                    hills.remove(hills[2])
                    hills.append(hill_min)
                else:
                    break
                if hill_min[2] < hills[2][2] or hill_min[2] < hills[1][2] or hill_min[2] < hills[0][2]:
                    break
                # hills.remove(i)
                # hills.append(Fmin)
                red_c += 1
                hill_min_red = calc_hill_2red(hills, hills[2], a, red_c)
#                print(f"hill_red: \n{hill_min_red}")
                if hill_min_red[2] < hills[2][2]:
                    hills.remove(hills[2])
                    hills.append(hill_min_red)
                break

        way.append(hills[-1])
        x_cur = hills[-1][0]
        y_cur = hills[-1][1]
#        print(f"- max, ++ better hill :\n{hills}")
        for i in hills:
            if input_F(i[0], i[1]) == 0:
                a = e
        c += 1

    print(way)
    to_plot(way, 'purple', axes, -15, 16)
