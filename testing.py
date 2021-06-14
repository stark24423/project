import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider


def update_lines(num, data_lines, lines):

    for line, data in zip(lines, data_lines):
        # NOTE: there is no .set_data() for 3 dim data...
        line.set_data(data[0:2, :num])
        line.set_3d_properties(data[2, :num])
        #step_text.set_text(step_template % (num))
    return lines


def list_transform(list):
    list_len = len(list)
    nlist = []
    nlist.append([])
    nlist.append([])
    nlist.append([])
    nlist.append([])
    list.reverse()
    for i in range(list_len):
        nlist[0].append(list[i][0])
        nlist[1].append(list[i][1])
        nlist[2].append(list[i][2])
        nlist[3].append(list[i][3])
    #print(nlist)
    list.reverse()
    return  nlist



def ani(list,size,maxtime):
# Attaching 3D axis to the figure

    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    step_text = ax.text(0.5, 0.9, 0.9, '', transform=ax.transAxes)
    step_template = 'step = %d'


    def update_lines_ani(num, data_lines, lines):
        for line, data in zip(lines, data_lines):
            # NOTE: there is no .set_data() for 3 dim data...
            line.set_data(data[0:2, :num])
            line.set_3d_properties(data[2, :num])
            step_text.set_text(step_template % (num))
        return lines
    data = []

    # Fifty lines of random 3-D lines
    for i in range(len(list)):
        data = data + [np.array(list_transform(list[i]))]

    lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]


    ax.set_xlim3d([0.0, size])
    ax.set_xlabel('X')
    ax.set_ylim3d([0.0, size])
    ax.set_ylabel('Y')
    ax.set_zlim3d([0.0, size])
    ax.set_zlabel('Z')
    ax.set_title('3D Test')


    x1, y1, z1 ,x2,y2,z2= [],[],[],[],[],[]
    for i in range(len(data)):
        len_data = len(data[i][0])-1
        x1.append(data[i][0][0])
        y1.append(data[i][1][0])
        z1.append(data[i][2][0])
        x2.append(data[i][0][len_data])
        y2.append(data[i][1][len_data])
        z2.append(data[i][2][len_data])

    ax.scatter(x1, y1, z1,c = "r",marker='^', label='start')
    ax.scatter(x2, y2, z2, c='b', marker='o',label='destination')
    ax.legend()

    line_ani = animation.FuncAnimation(fig, update_lines_ani,maxtime, fargs=(data, lines), interval=300)
    #line_ani.save("test.gif", writer='pillow')
    plt.show()

def ani_crash(list,size,maxtime,crash_position):

    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    data = []
    # Fifty lines of random 3-D lines
    for i in range(len(list)):
        data = data + [np.array(list_transform(list[i]))]
    #print(data)
    # Creating fifty line objects.
    # NOTE: Can't pass empty arrays into 3d version of plot()
    lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]

    # Setting the axes properties
    ax.set_xlim3d([0.0, size])
    ax.set_xlabel('X')
    ax.set_ylim3d([0.0, size])
    ax.set_ylabel('Y')
    ax.set_zlim3d([0.0, size])
    ax.set_zlabel('Z')
    ax.set_title('Collision Path')


    x1, y1, z1 ,x2,y2,z2= [],[],[],[],[],[]
    x,y,z = [],[],[]#這是紀錄碰撞用的
    for i in range(len(data)):
        len_data = len(data[i][0])-1
        x1.append(data[i][0][0])
        y1.append(data[i][1][0])
        z1.append(data[i][2][0])
        x2.append(data[i][0][len_data])
        y2.append(data[i][1][len_data])
        z2.append(data[i][2][len_data])
    for i in range(len(crash_position)):
        x.append(crash_position[i][0])
        y.append(crash_position[i][1])
        z.append(crash_position[i][2])


    ax.scatter(x1, y1, z1,c = "r",marker='^', label='start')
    ax.scatter(x2, y2, z2, c='b', marker='o',label='destination')
    ax.scatter(x,y,z, c='g', marker='x',label='collision')
    ax.legend()
    # Creating the Animation object
    line_ani = animation.FuncAnimation(
       fig, update_lines,maxtime, fargs=(data, lines), interval=300)
    #print("純黨")
    #line_ani.save("test.gif",writer='pillow')
    plt.show()


def ani_final1(list,size,maxtime):


    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    step_text = ax.text(0.5, 0.9, 0.9, '', transform=ax.transAxes)
    step_template = 'step = %d'

    def update_lines_final(num, data_lines, lines):
        for line, data in zip(lines, data_lines):
            # NOTE: there is no .set_data() for 3 dim data...
            line.set_data(data[0:2, :num])
            line.set_3d_properties(data[2, :num])
            step_text.set_text(step_template % (num))
        return lines


    data =[]
    for i in range(len(list)):
        data = data + [np.array(list_transform(list[i]))]

    lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]


    ax.set_xlim3d([0.0, size])
    ax.set_xlabel('X')
    ax.set_ylim3d([0.0, size])
    ax.set_ylabel('Y')
    ax.set_zlim3d([0.0, size])
    ax.set_zlabel('Z')
    ax.set_title('Final Path')

    x1, y1, z1 ,x2,y2,z2= [],[],[],[],[],[]
    for i in range(len(data)):
        len_data = len(data[i][0])-1
        x1.append(data[i][0][0])
        y1.append(data[i][1][0])
        z1.append(data[i][2][0])
        x2.append(data[i][0][len_data])
        y2.append(data[i][1][len_data])
        z2.append(data[i][2][len_data])

    ax.scatter(x1, y1, z1,c = "r",marker='^', label='start')
    ax.scatter(x2, y2, z2, c='b', marker='o',label='destination')
    ax.legend()
    line_ani = animation.FuncAnimation(fig, update_lines_final,maxtime, fargs=(data, lines), interval=300)
    plt.show()

def ani_crash(list,size,maxtime,crash_position):

    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    data = []
    # Fifty lines of random 3-D lines
    for i in range(len(list)):
        data = data + [np.array(list_transform(list[i]))]
    #print(data)
    # Creating fifty line objects.
    # NOTE: Can't pass empty arrays into 3d version of plot()
    lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]

    # Setting the axes properties
    ax.set_xlim3d([0.0, size])
    ax.set_xlabel('X')
    ax.set_ylim3d([0.0, size])
    ax.set_ylabel('Y')
    ax.set_zlim3d([0.0, size])
    ax.set_zlabel('Z')
    ax.set_title('Collision Path')


    x1, y1, z1 ,x2,y2,z2= [],[],[],[],[],[]
    x,y,z = [],[],[]#這是紀錄碰撞用的
    for i in range(len(data)):
        len_data = len(data[i][0])-1
        x1.append(data[i][0][0])
        y1.append(data[i][1][0])
        z1.append(data[i][2][0])
        x2.append(data[i][0][len_data])
        y2.append(data[i][1][len_data])
        z2.append(data[i][2][len_data])
    for i in range(len(crash_position)):
        x.append(crash_position[i][0])
        y.append(crash_position[i][1])
        z.append(crash_position[i][2])


    ax.scatter(x1, y1, z1,c = "r",marker='^', label='start')
    ax.scatter(x2, y2, z2, c='b', marker='o',label='destination')
    ax.scatter(x,y,z, c='g', marker='x',label='collision')
    ax.legend()
    # Creating the Animation object
    line_ani = animation.FuncAnimation(
       fig, update_lines,maxtime, fargs=(data, lines), interval=300)
    #print("純黨")
    #line_ani.save("test.gif",writer='pillow')
    plt.show()

is_manual = False
def ani_test(list,size,maxtime):

    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    step_text = ax.text(0.5, 0.9, 0.9, '', transform=ax.transAxes)
    step_template = 'AT = %1.1f'
    axamp = plt.axes([0.25, 0.03, 0.50, 0.02])
    samp = Slider(axamp, 'Arrive time ', 0, maxtime, valinit=0,valfmt='%1.1f' )
    def update_lines_final(num, data_lines, lines):
        AT = samp.val
        global is_manual
        for line, data in zip(lines, data_lines):
            # NOTE: there is no .set_data() for 3 dim data...
            #print(is_manual)
            if is_manual==True:
                counter = 0
                for i in data[3]:
                    if i <AT:
                        counter =counter+1
                line.set_data(data[0:2, :counter])
                line.set_3d_properties(data[2, :counter])
                step_text.set_text(step_template % (AT))
            else:
                line.set_data(data[0:2, :num])
                line.set_3d_properties(data[2, :num])
                step_text.set_text(step_template % (num))
                samp.set_val(num)
                is_manual = False

        return lines

    def on_click(event):
        # Check where the click happened
        (xm, ym), (xM, yM) = samp.label.clipbox.get_points()
        if xm < event.x < xM and ym < event.y < yM:
            # Event happened within the slider, ignore since it is handled in update_slider
            return
        else:
            # user clicked somewhere else on canvas = unpause
            global is_manual
            is_manual = False

    def update_slider(val):
        global is_manual
        is_manual = True
        #print('slidering')
        #print(is_manual)

    fig.canvas.mpl_connect('button_press_event', on_click)
    samp.on_changed(update_slider)

    data =[]
    for i in range(len(list)):
        data = data + [np.array(list_transform(list[i]))]
    #print(data)
    lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]
    #print('lines=>',lines)


    ax.set_xlim3d([0.0, size])
    ax.set_xlabel('X')
    ax.set_ylim3d([0.0, size])
    ax.set_ylabel('Y')
    ax.set_zlim3d([0.0, size])
    ax.set_zlabel('Z')
    ax.set_title('Final Path')

    x1, y1, z1 ,x2,y2,z2= [],[],[],[],[],[]
    for i in range(len(data)):
        len_data = len(data[i][0])-1
        x1.append(data[i][0][0])
        y1.append(data[i][1][0])
        z1.append(data[i][2][0])
        x2.append(data[i][0][len_data])
        y2.append(data[i][1][len_data])
        z2.append(data[i][2][len_data])

    ax.scatter(x1, y1, z1,c = "r",marker='^', label='start')
    ax.scatter(x2, y2, z2, c='b', marker='o',label='destination')
    ax.legend()
    line_ani = animation.FuncAnimation(fig, update_lines_final,maxtime, fargs=(data, lines), interval=300)
    plt.show()

    def ani_test(list, size, maxtime):

        fig = plt.figure()
        ax = fig.add_subplot(projection="3d")
        step_text = ax.text(0.5, 0.9, 0.9, '', transform=ax.transAxes)
        step_template = 'AT = %1.1f'
        axamp = plt.axes([0.25, 0.03, 0.50, 0.02])
        samp = Slider(axamp, 'Arrive time ', 0, maxtime, valinit=0, valfmt='%1.1f')

        def update_lines_final(num, data_lines, lines):
            AT = samp.val
            global is_manual
            for line, data in zip(lines, data_lines):
                # NOTE: there is no .set_data() for 3 dim data...
                # print(is_manual)
                if is_manual == True:
                    counter = 0
                    for i in data[3]:
                        if i < AT:
                            counter = counter + 1
                    line.set_data(data[0:2, :counter])
                    line.set_3d_properties(data[2, :counter])

                    step_text.set_text(step_template % (AT))
                else:
                    line.set_data(data[0:2, :num])
                    line.set_3d_properties(data[2, :num])
                    step_text.set_text(step_template % (num))
                    samp.set_val(num)
                    is_manual = False

            return lines

        def on_click(event):
            # Check where the click happened
            (xm, ym), (xM, yM) = samp.label.clipbox.get_points()
            if xm < event.x < xM and ym < event.y < yM:
                # Event happened within the slider, ignore since it is handled in update_slider
                return
            else:
                # user clicked somewhere else on canvas = unpause
                global is_manual
                is_manual = False

        def update_slider(val):
            global is_manual
            is_manual = True
            # print('slidering')
            # print(is_manual)

        fig.canvas.mpl_connect('button_press_event', on_click)
        samp.on_changed(update_slider)

        data = []
        for i in range(len(list)):
            data = data + [np.array(list_transform(list[i]))]
        # print(data)
        lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]
        # print('lines=>',lines)

        ax.set_xlim3d([0.0, size])
        ax.set_xlabel('X')
        ax.set_ylim3d([0.0, size])
        ax.set_ylabel('Y')
        ax.set_zlim3d([0.0, size])
        ax.set_zlabel('Z')
        ax.set_title('Final Path')

        x1, y1, z1, x2, y2, z2 = [], [], [], [], [], []
        for i in range(len(data)):
            len_data = len(data[i][0]) - 1
            x1.append(data[i][0][0])
            y1.append(data[i][1][0])
            z1.append(data[i][2][0])
            x2.append(data[i][0][len_data])
            y2.append(data[i][1][len_data])
            z2.append(data[i][2][len_data])

        ax.scatter(x1, y1, z1, c="r", marker='^', label='start')
        ax.scatter(x2, y2, z2, c='b', marker='o', label='destination')
        ax.legend()
        line_ani = animation.FuncAnimation(fig, update_lines_final, maxtime, fargs=(data, lines), interval=300)
        plt.show()

is_manual = False


def muti_frame(list,size,maxtime):

    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    step_text = ax.text(0.5, 0.9, 0.9, '', transform=ax.transAxes)
    step_template = 'AT = %1.1f'
    axamp = plt.axes([0.25, 0.03, 0.50, 0.02])
    samp = Slider(axamp, 'Arrive time ', 0, maxtime, valinit=0,valfmt='%1.1f' )
    def update_lines_final(num, data_lines, lines,scatters):
        AT = samp.val
        global is_manual
        for line, data,scatter in zip(lines, data_lines,scatters):
            # NOTE: there is no .set_data() for 3 dim data...
            #print(is_manual)
            if is_manual==True:
                counter = 0
                for i in data[3]:
                    if i <AT:
                        counter =counter+1
                line.set_data(data[0:2, :counter])
                line.set_3d_properties(data[2, :counter])
                #scatter._offsets3d = ([int(data[0][counter])],[int(data[1][counter])],[int(data[2][counter])])
                if counter!= 0:
                    scatter._offsets3d = ([data[0][counter-1]],[data[1][counter-1]],[data[2][counter-1]])
                #print(data[2, :counter])
                #print(data[2][counter])
                #print(data)

                step_text.set_text(step_template % (AT))
            else:
                line.set_data(data[0:2, :num])
                line.set_3d_properties(data[2, :num])
                #scatter._offsets3d = ([data[num][0]], [[data[num][1]]], [[data[num][2]]])
                step_text.set_text(step_template % (num))
                if num-1<len(data[0]):
                    scatter._offsets3d = ([data[0][num - 1]], [data[1][num - 1]], [data[2][num - 1]])
                samp.set_val(num)
                is_manual = False

        return lines

    def on_click(event):
        # Check where the click happened
        (xm, ym), (xM, yM) = samp.label.clipbox.get_points()
        if xm < event.x < xM and ym < event.y < yM:
            # Event happened within the slider, ignore since it is handled in update_slider
            return
        else:
            # user clicked somewhere else on canvas = unpause
            global is_manual
            is_manual = False

    def update_slider(val):
        global is_manual
        is_manual = True
        #print('slidering')
        #print(is_manual)

    fig.canvas.mpl_connect('button_press_event', on_click)
    samp.on_changed(update_slider)

    data =[]
    for i in range(len(list)):
        data = data + [np.array(list_transform(list[i]))]
    #print(data)
    lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]
    #print('lines=>',lines)


    ax.set_xlim3d([0.0, size])
    ax.set_xlabel('X')
    ax.set_ylim3d([0.0, size])
    ax.set_ylabel('Y')
    ax.set_zlim3d([0.0, size])
    ax.set_zlabel('Z')
    ax.set_title('Muti frame')

    x1, y1, z1 ,x2,y2,z2= [],[],[],[],[],[]
    '''for i in range(len(data)):
        len_data = len(data[i][0])-1
        x1.append(data[i][0][0])
        y1.append(data[i][1][0])
        z1.append(data[i][2][0])
        x2.append(data[i][0][len_data])
        y2.append(data[i][1][len_data])
        z2.append(data[i][2][len_data])

    ax.scatter(x1, y1, z1,c = "r",marker='^', label='start')
    ax.scatter(x2, y2, z2, c='b', marker='o',label='destination')'''

    scatters = [ax.scatter(path[-1][0],path[-1][1],path[-1][2]) for path in list]
    drone_labal_list = []
    for g in range(len(list)):
        drone_labal_list = drone_labal_list + ['Drone ' + str(g+1)]


    startposition = [ax.scatter(path[-1][0],path[-1][1],path[-1][2], marker='x',label=drone_labal) for path,drone_labal in zip(list, drone_labal_list)]
    ax.legend()
    line_ani = animation.FuncAnimation(fig, update_lines_final,maxtime, fargs=(data, lines,scatters), interval=300)
    plt.show()




if __name__ == '__main__':
    f = [[[2, 6, 1, 5.1], [3, 7, 2, 3.4], [4, 7, 3, 2], [5, 7, 3, 1], [6, 7, 3, 0]], [[3, 4, 6, 3.7], [2, 3, 5, 2], [2, 3, 4, 1], [2, 3, 3, 0]], [[8, 5, 8, 5.1], [9, 6, 7, 3.4], [9, 7, 6, 2], [9, 8, 6, 1], [9, 9, 6, 0]], [[1, 4, 3, 4.1], [2, 5, 2, 2.4], [3, 5, 1, 1], [4, 5, 1, 0]], [[8, 1, 5, 2.4], [9, 1, 6, 1], [9, 1, 7, 0]], [[3, 4, 1, 4.4], [4, 5, 1, 3], [5, 5, 1, 2], [6, 5, 1, 1], [7, 5, 1, 0]], [[3, 2, 7, 4.5], [4, 3, 6, 2.8], [4, 4, 5, 1.4], [4, 5, 4, 0]], [[7, 1, 1, 3.8], [8, 2, 1, 2.4], [9, 3, 1, 1], [9, 4, 1, 0]], [[3, 4, 4, 5.199999999999999], [4, 5, 4, 3.8], [5, 6, 4, 2.4], [6, 7, 4, 1], [7, 7, 4, 0]], [[7, 3, 7, 2.8], [6, 3, 8, 1.4], [5, 3, 9, 0]]]

    muti_frame(f,10,10)