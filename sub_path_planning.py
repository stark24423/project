import matplotlib.pyplot as plt
import numpy as np
import ani


def create_search_block():  # 建立鄰邊方塊搜尋用陣列
    x, y, z = 0, 0, 0
    num = [-1, 1]
    list = []
    for i in num:
        list.append([x + i, y, z, 1])
        list.append([x, y + i, z, 1])
        list.append([x, y, z + i, 1])

    for i in num:
        for j in num:
            list.append([x + i, y + j, 0, 1.4])
    for i in num:
        list.append([x + i, y , 1, 1.4])
        list.append([x + i, y, -1, 1.4])
    for i in num:
        list.append([x , y+i , 1, 1.4])
        list.append([x , y+i, -1, 1.4])


    for i in num:
        for j in num:
            list.append([x + i, y + j, 1, 1.7])
            list.append([x + i, y + j, -1, 1.7])
    #print(list)
    return list


def creat_Vijk(infinty_number, size):
    list = []
    num = 0
    for i in range(size):
        list.append([])
        for j in range(size):
            list[i].append([])
            for k in range(size):
                list[i][j].append([0, infinty_number, False])
    return list


def get_vijk_at(list, p):
    return list[p[0]][p[1]][p[2]][1]

def get_vijk_vis(list, p):
    return list[p[0]][p[1]][p[2]][2]


def give_vijk_at(list, p, value):
    list[p[0]][p[1]][p[2]][1] = value
    return list

def give_vijk_vis(list, p, value):
    list[p[0]][p[1]][p[2]][2] = value
    return list



def add_for_list(list1, list2):
    le = len(list1)
    list3 = []
    for i in range(le):
        list3.append(list1[i] + list2[i])
    return list3


def tl_to_ll(list1,list2,list3,tl, Vijk,index,index_number):
    len_tl = len(tl)
    list_head = 10000
    num = 0

    list_head = int(index_number)

    for i in range(len_tl):

        num = int(get_vijk_at(Vijk, tl[i]))

        #print("list_head=", list_head,"num = ",num )
        if index == 1:
            if num == list_head:
                list1.append(tl[i])
            elif num == list_head + 1:
                list2.append(tl[i])
            else:
                list3.append(tl[i])
        elif index == 2:
            if num == list_head:
                list2.append(tl[i])
            elif num == list_head + 1:
                list3.append(tl[i])
            else:
                list1.append(tl[i])
        else:
            if num == list_head:
                list3.append(tl[i])
            elif num == list_head + 1:
                list1.append(tl[i])
            else:
                list2.append(tl[i])
    return list1, list2, list3


def update_at(p, vijk, size, search_block_3d,TL):
    for i in search_block_3d:
        np = add_for_list(p, i)
        if check_size(np, size):
            if check_block(p, np, vijk):
                if get_vijk_vis(vijk,np) == 0:
                    nat = get_vijk_at(vijk,p)+i[3]
                    if get_vijk_at(vijk,np)>nat:
                        give_vijk_at(vijk,np,nat)
                        give_vijk_vis(vijk,np,1)
                        TL.append(np)

    return vijk,TL


def check_size(np, size):
    if np[0] >= size or np[1] >= size or np[2] >= size or np[0] < 0 or np[1] < 0 or np[2] < 0:
        return False
    return True


def check_block(p, np, vijk):
    x, y, z = p
    nx, ny, nz = np
    if nz - z == 0:
        if vijk[nx][y][z][0] == 1 or vijk[x][ny][z][0] == 1:
            return False
        else:
            return True
    else:
        if vijk[nx][y][nz][0] == 1 or vijk[x][ny][nz][0] == 1 or vijk[x][y][nz][0] == 1:
            return False
        else:
            return True

def trace_back(vijk,s,d,search_block_3d,size):
    trace_flag = True
    p = d
    at = 10000
    search_list = []
    path=[]
    path.append(d)
    while trace_flag:
        for i in search_block_3d:
            np = add_for_list(p, i)
            #print("np",np)
            if check_size(np, size) :
                if check_block(p, np, vijk):
                    search_list.append([get_vijk_at(vijk,np),np[0],np[1],np[2]])
        search_list.sort()
        #print("這是搜尋的點",search_list)
        p = [search_list[0][1],search_list[0][2],search_list[0][3]]
        path.append(p)
        search_list=[]
        #print("p=",p)
        if get_vijk_at(vijk,p)==0:
            break
    #print("這是回朔路徑",path)
    return path


def prt_vijk(vijk,num,size):  # 0 是障礙物 1是AT 2 是VIS
    for i in range(size):
        for j in range(size):
            for k in range(size):
                print("{:.3f}".format(vijk[i][j][k][num]), end=',')
            print()
        print()

def prt_graph(path,size,s,d):
    x, y, z = np.indices((size, size, size))
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_xlim(0, size)
    ax.set_ylim(0, size)
    ax.set_zlim(0, size)
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    for i in path:
        xx,yy,zz=i
        ax.voxels((x == xx) & (y == yy) & (z ==zz), facecolors='green', edgecolor='k')
        print(i)
    ax.voxels((x == s[0]) & (y == s[1]) & (z == s[2]), facecolors='red', edgecolor='k')
    ax.voxels((x == d[0]) & (y == d[1]) & (z == d[2]), facecolors='blue', edgecolor='k')

    #ax.legend()

    # 顯示圖形
    plt.show()
    print("輸出完成")
def update_lines(num, data_lines, lines):
    for line, data in zip(lines, data_lines):
        # NOTE: there is no .set_data() for 3 dim data...
        line.set_data(data[0:2, :num])
        line.set_3d_properties(data[2, :num])
    return lines

def prt_g(path,size):
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.set_xlim3d([0.0, size])
    ax.set_xlabel('X')

    ax.set_ylim3d([0.0, size])
    ax.set_ylabel('Y')

    ax.set_zlim3d([0.0, size])
    ax.set_zlabel('Z')

    ax.set_title('3D Test')
    data = []


    

def path_planning(S,D,voxel_size,infinty_number):
    search_block_3d = create_search_block()
    #voxel_size = 20
    #infinty_number = 10000

    Vijk = []  # (障礙物,AT到達時間,vis是否訪問過)
    Vijk = creat_Vijk(infinty_number, voxel_size)
    path_done=True
    TL = []
    LL0 = []
    LL1 = []
    LL2 = []
    # 目的地設定
    #S = [0, 0, 0]
    #D = [0, 0, 19]
    Vijk = give_vijk_at(Vijk, S, 0)
    TL.append(S)
    index = 1
    index_number = 0
    while(path_done):
        LL0, LL1, LL2 = tl_to_ll(LL0, LL1, LL2,TL, Vijk,index,index_number)

        #print("TL=",TL)
        TL = []
        #print("ll0=",LL0)
        #print("ll1=",LL1)
        #print("ll2=",LL2)
        if index == 1:
            for i in range(len(LL0)):
                Vijk,TL = update_at(LL0[i],Vijk,voxel_size,search_block_3d,TL)
            LL0 = []
            indexflag = 2
        elif index == 2:
            for i in range(len(LL1)):
                Vijk,TL = update_at(LL1[i],Vijk,voxel_size,search_block_3d,TL)
            LL1 = []
            indexflag = 3
        elif index == 3:
            for i in range(len(LL2)):
                Vijk,TL = update_at(LL2[i],Vijk,voxel_size,search_block_3d,TL)
            LL2 = []
            indexflag = 1
        index = indexflag
        index_number  = index_number +1
        #print(get_vijk_at(Vijk,D))
        if get_vijk_at(Vijk,D)!= infinty_number :
            path_done =False

    #prt_vijk(Vijk,1,voxel_size)
    path=trace_back(Vijk,S,D,search_block_3d,voxel_size)
    #ani.ani(path,voxel_size)
    return path,get_vijk_at(Vijk , path[0])
    print("done")





