import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Fixing random state for reproducibility
np.random.seed(19680801)


def gen_rand_line(length, dims=2):
    """
    Create a line using a random walk algorithm.

    Parameters
    ----------
    length : int
        The number of points of the line.
    dims : int
        The number of dimensions of the line.
    """
    line_data = np.empty((dims, length))
    line_data[:, 0] = np.random.rand(dims)
    for index in range(1, length):
        # scaling the random numbers by 0.1 so
        # movement is small compared to position.
        # subtraction by 0.5 is to change the range to [-0.5, 0.5]
        # to allow a line to move backwards.
        step = (np.random.rand(dims) - 0.5) * 0.1
        line_data[:, index] = line_data[:, index - 1] + step
    # print(line_data)
    return line_data


def update_lines(num, data_lines, lines):
    for line, data in zip(lines, data_lines):
        # NOTE: there is no .set_data() for 3 dim data...
        line.set_data(data[0:2, :num])
        line.set_3d_properties(data[2, :num])
    return lines


def list_transform(list):
    list_len = len(list)
    nlist = []
    nlist.append([])
    nlist.append([])
    nlist.append([])
    list.reverse()
    for i in range(list_len):
        nlist[0].append(list[i][0])
        nlist[1].append(list[i][1])
        nlist[2].append(list[i][2])
    print(nlist)
    return  nlist


def ani(list,size):
# Attaching 3D axis to the figure
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    data = []
    # Fifty lines of random 3-D lines
    for i in range(len(list)):
        data = data + [np.array(list_transform(list[i]))]
    print(data)
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

            #x2,y2,z2  data[i][0][len_data],data[i][1][len_data],data[i][2][len_data]
    ax.scatter(x1, y1, z1, c=z1, marker='^', label='My Points 1')
    ax.scatter(x2, y2, z2, c=z2, marker='o', label='My Points 2')


    ax.legend()
    # Creating the Animation object
    line_ani = animation.FuncAnimation(
       fig, update_lines, 100, fargs=(data, lines), interval=200)

    plt.show()





