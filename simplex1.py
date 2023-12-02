from plots_and_func import *


def simp_max(hills):
    Fmax = hills[0]
    Fmax_val = Fmax[2]
    global Fstep
    for i in hills:
        Fstep = input_F(i[0], i[1])
        if Fstep > Fmax_val:
            Fmax = i
    return Fmax



def hills_calc(x, y, a):
    return [[round(x - a / 2, 4), round(y - 0.29 * a, 4), round(input_F(round(x - a / 2, 4), round(y - 0.29 * a, 4)), 4)],
            [round(x + a / 2, 4), round(y - 0.29 * a, 4), round(input_F(round(x + a / 2, 4), round(y - 0.29 * a, 4)), 4)],
            [round(x, 4), round(y + 0.58 * a, 4), round(input_F(round(x, 4), round(y + 0.58 * a, 4)), 4)]
            ]


# def check_reduction(hills):


def simplex_method(start, a, e, axes):
    x_cur = start[0]
    y_cur = start[1]
    way = [[x_cur, y_cur, input_F(x_cur, y_cur)]]
    global F_step
    last_hills2 = [[[0], [0], [0]], [[0], [0], [0]]]
    global c
    c = 0
    hills = hills_calc(x_cur, y_cur, a)
    for i in range(len(hills)):
        way.append(hills[i])
    while a > e:
        print(hills)
        Fmax = simp_max(hills)
        c += 1
        # new_hill = [hills[0][0] + hills[1][0] - hills[2][0], hills[0][1] + hills[1][1] - hills[2][1]]
        for i in hills:
            if i == Fmax:
                last_hills2.append(hills.copy())
                last_hills2.remove(last_hills2[0])
                hills.remove(i)
                hills.append(
                    [round(hills[0][0] + hills[1][0] - Fmax[0], 4),
                     round(hills[0][1] + hills[1][1] - Fmax[1], 4)])
                way.append(hills[-1])
                way[-1].append(round(input_F(way[-1][0], way[-1][1]), 4))
                x_cur = hills[-1][0]
                y_cur = hills[-1][1]
                break
        for i in hills:
            if input_F(i[0], i[1]) == 0:
                a = e

        if ((last_hills2[0][2] == hills[2])
                or (last_hills2[1][2] == hills[2])):
            a /= 2
            hills = hills_calc(x_cur, y_cur, a)

    print(way)
    to_plot(way, 'y', axes, -15, 16)
