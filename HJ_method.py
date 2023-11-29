from plots_and_func import *
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
