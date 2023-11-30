from plots_and_func import *

def find_min(x, y, step):

    left_val = input_F(x - step, y)
    right_val = input_F(x + step, y)
    up_val = input_F(x, y + step)
    down_val = input_F(x, y - step)
    vals_min = min(up_val, down_val, left_val, right_val)
    vals = [left_val, right_val, up_val, down_val]
    print(vals)
    for i in range(len(vals)):
        if vals[i] != vals_min:
            vals[i] = 0
    return vals

def check_circle(way, cur):
    for i in way:
        if i == cur:
            return 1
    return 0

def Gauss_Zeudel(start, step_x, step_y, e, axes):
    x_cur = start[0]
    y_cur = start[1]
    way = [[x_cur, y_cur, input_F(x_cur, y_cur)]]
    global F_min
    global F_step
    F_min = input_F(x_cur, y_cur)

    while step_x > e or step_y > e:

        F_step = find_min(x_cur, y_cur, step_x)



        if F_step[0] != 0:
            way.append([x_cur, y_cur, input_F(x_cur, y_cur)])
            F_min = F_step
            x_cur -= step_x
            if(check_circle(way, [x_cur, y_cur, input_F(x_cur, y_cur)])):
                step_x /=2
            continue

        if F_step[3] != 0:
            way.append([x_cur, y_cur, input_F(x_cur, y_cur)])
            F_min = F_step
            y_cur -= step_y
            if(check_circle(way, [x_cur, y_cur, input_F(x_cur, y_cur)])):
                step_x /=2
            continue

        if F_step[1] != 0:
            way.append([x_cur, y_cur, input_F(x_cur, y_cur)])
            F_min = F_step
            x_cur += step_x
            if(check_circle(way, [x_cur, y_cur, input_F(x_cur, y_cur)])):
                step_x /=2
            continue

        if F_step[2] != 0:
            way.append([x_cur, y_cur, input_F(x_cur, y_cur)])
            F_min = F_step
            y_cur += step_y
            if(check_circle(way, [x_cur, y_cur, input_F(x_cur, y_cur)])):
                step_x /=2
            continue



        step_x /= 2
        step_y /= 2
    print(way)
    to_plot(way, 'b', axes, -15, 20)