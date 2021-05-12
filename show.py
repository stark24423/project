import sub_mapping as mp
import sub_path_planning as pp
import sub_ani

drone_number = 8
voxel_size = 10
frame_1 = [[3,1,5],[1,2,5],[0,3,5],[1,4,5],[3,5,5],[4,4,5],[3,3,5],[4,1,5]]
init_frame = [[1,0,0],[2,0,0],[3,0,0],[4,0,0],[1,1,0],[2,1,0],[3,1,0],[4,1,0]]
path =[]
AT = []

for i in range(drone_number):
    AT.append([])
    path.append([])
    for j in range(drone_number):
        path[i].append([])
        AT[i].append([])
        path[i][j],AT[i][j] = pp.path_planning(init_frame[i],frame_1[j],voxel_size,10000)

print(path)
mp.pr_list2(AT)
choose = mp.mapping(AT)
total_path = []

for i in range(drone_number):
    for j in range(drone_number):
        if choose[i][j] == 1:
            total_path.append(path[i][j])

sub_ani.ani(total_path,voxel_size)
print(total_path)