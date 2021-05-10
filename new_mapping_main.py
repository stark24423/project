


import random as rd
#from tqdm import tqdm
import numpy as np
import time

def create_random_table(table_size, len_number):
    list = []
    for i in range(0, table_size):
        list.append([])
        for j in range(0, table_size):
            list[i].append(rd.randrange(1, len_number))
    return list


def create_table_index(table, table_len):
    table_index = []
    for i in range(table_len):
        for j in range(table_len):
            table_index.append([table[i][j], i, j])
    table_index.sort(reverse=True)
    return table_index


def create_pd(len_number):
    pd1 = []
    pd2 = []
    for i in range(len_number):
        pd1.append(i)
    for i in range(len_number):
        pd2.append(i)
    return pd1, pd2

def create_pd_counter(size):
    pd1 = []
    pd2 = []
    for i in range(size):
        pd1.append(size)
    for i in range(size):
        pd2.append(size)
    return pd1, pd2


def create_table_choose(table_size):
    list = []
    for i in range(0, table_size):
        list.append([])
        for j in range(0, table_size):
            list[i].append(1)
    return list

def sub_pd_counter(pc,dc,p,d):
    pc[p] = pc[p] - 1
    dc[d] = dc[d] - 1
    return pc,dc
def search_counter(pc,dc):
    pcl = len(pc)
    pdl = len(dc)
    for i in range(pcl):
        if pc[i]==1 :
            return 0 , i
        elif dc[i]==1:
            return 1 , i
    return 3,0


def check_colume(p, d,table_choose):
    for i in p:
        flag = 0
        for j in d:
            if table_choose[i][j] == 1:
                flag = flag + 1
                flags = j
        if flag == 1:
            return True, i, flags,table_choose
    return False, 0, 0 ,table_choose


def check_row(p, d,table_choose):
    for i in d:
        flag = 0
        for j in p:
            if table_choose[j][i] == 1:
                flag = flag + 1
                flags = j
        if flag == 1:
            return True, flags, i,table_choose
    return False, 0, 0,table_choose


def remove_pd(p, d, pi, di, pc, dc, table_choose):
    p.remove(pi)
    d.remove(di)
    table_choose[pi][di] = 1
    for i in d:
        if table_choose[pi][i] != 0:
            table_choose[pi][i] = 0
            dc[i]=dc[i]-1
    for i in p:
        if table_choose[i][di] != 0:
            table_choose[i][di] = 0
            pc[i]=pc[i]-1
    pc[pi],dc[di] = 0,0
    return p, d, pc,dc, table_choose

def check_answer(table_choose):

    for i in table_choose:
        sum = 0
        for j in i:
            sum = j+sum
        if sum != 1:
            return False
    return True

    return ff
def 提升優先權(table,table_size,p,d,table_index):
    list = []
    pp = []
    dd = []

    for i in p:
        for j in range(table_size):
            if j not in d:
                list.append([table[i][j],i,j])
                table_index.remove([table[i][j],i,j])
    for i in d:
        for j in range(table_size):
            if j not in p:
                list.append([table[j][i],j,i])
                table_index.remove([table[j][i],j,i])
    for i in p:
        for j in d:
            list.append([table[i][j], i, j])
            table_index.remove([table[i][j], i, j])

    list.sort(reverse=True)
    print(len(list))
    return list,table_index



def pr_list(list):
    for i in range(len(list)):
        print(list[i])

def mapping():
    start = time.time()
    table_size = 4
    len_number = 50
    # 產生範例
    table = create_random_table(table_size, len_number)
    #table = [[9,10,9,10,10],[9,9,9,9,8],[10,7,10,7,10],[10,7,12,7,10],[10,7,10,7,10]]
    #table = [[1,9,9,9,8,8],[3,9,9,9,9,3],[3,9,9,9,9,3],[3,9,9,9,9,6],[1,9,9,9,9,4],[1,1,1,1,2,3]]
    table = [[65,73,55,58],[90,67,87,75],[106,86,94,89],[84,69,79,77]]
    table_len = len(table)
    table_index = create_table_index(table, table_len)
    table_index_o = table_index
    table_index_len = len(table_index)
    table_choose = create_table_choose(table_size)

    p=[0]
    d=[0]
    pc,dc = [],[]
    p, d = create_pd(table_len)
    pc,dc = create_pd_counter(table_size)
    TL = []#存1
    #process = tqdm(total= len(table_index))
    error_flag = True
    re = 0
    while error_flag is True:
        for i in range(table_index_len):
            #process.update(1)
            if (table_index[i][1] in p) and (table_index[i][2] in d):
                table_choose[table_index[i][1]][table_index[i][2]] = 0
                pc,dc = sub_pd_counter(pc,dc,table_index[i][1],table_index[i][2])
                remove_flag = False
                if re == 2:
                    print("去掉",table_index[i][0],table_index[i][1],table_index[i][2])
                    pr_list(table_choose)
                    print('這是PC',pc)
                    print('這是dc',dc)
                    print("pd",p,d)
                    print("這是i",i)

                if pc[table_index[i][1]] == 1 :
                    #print("偵測到PC")
                    remove_flag, pi, di ,table_choose= check_colume(p, d, table_choose)
                    #print("PIDI",pi,di)
                    p, d, pc,dc,table_choose = remove_pd(p, d, pi, di, pc,dc,table_choose)
                    remove_flag=True
                elif dc[table_index[i][2]] == 1:
                    #print("偵測到DC")
                    remove_flag, pi, di ,table_choose= check_row(p, d,table_choose)
                    #print("PIDI", pi, di)
                    p, d, pc,dc,table_choose = remove_pd(p, d,pi, di, pc,dc,table_choose)
                    remove_flag=True

                while remove_flag:
                    flag_pdcounter,count = search_counter(pc,dc)
                    #print('這是PC', pc)
                    #print('這是dc', dc)
                    #pr_list(table_choose)
                    if flag_pdcounter == 0:
                        #print("偵測到PC")
                        remove_flag, pi, di,table_choose = check_colume(p, d,table_choose)
                        #print("PIDI", pi, di)
                        p, d, pc, dc, table_choose = remove_pd(p, d, pi, di, pc, dc, table_choose)
                    elif flag_pdcounter == 1:
                        #print("偵測到DC")
                        remove_flag, pi, di ,table_choose= check_row(p, d,table_choose)
                        #print("PIDI", pi, di)
                        p, d, pc, dc, table_choose = remove_pd(p, d, pi, di, pc, dc, table_choose)
                    else:
                        remove_flag = False

                #pr_list(table_choose)
                #print()




        if check_answer(table_choose) is True:
            error_flag = False
        else:
            print("重來")
            print("多的P",p, d)
            #pr_list(table_choose)
            newtable_index,table_index = 提升優先權(table,table_size,p,d,table_index)
            table_index = newtable_index + table_index
            print("這是長度",len(table_index))
            table_choose = create_table_choose(table_size)
            p, d = create_pd(table_len)
            pc,dc = create_pd_counter(table_size)

            re = re
            if re == 4:
                error_flag = False


    #tqdm.close(process)
    #pr_list(table_choose)
    # 結束測量

    end = time.time()

    print("原始:")
    pr_list(table)
    print("結果:")
    pr_list(table_choose)
    #print(check_answer(table_choose))
    #print(p,d)
    print("done")
    print("執行時間：%f 秒" % (end - start))
    return check_answer(table_choose),end - start


mapping()