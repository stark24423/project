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

def create_table_choose(table_size):
    list = []
    for i in range(0, table_size):
        list.append([])
        for j in range(0, table_size):
            list[i].append(0)
    return list
def 看最晚到達時間(table,table_size,table_choose):
    maxnum = 0
    for i in range(table_size):
        for j in range(table_size):
            if table_choose[i][j] == 1:
                if table[i][j]>maxnum:
                    maxnum = table[i][j]
    print("最大值",maxnum)
    return  maxnum
def pr_list(list):
    for i in range(len(list)):
        print(list[i])
def hard_table(table):
    table_size = 3
    len_number = 10
    table_choose = create_table_choose(table_size)
    allmaxnum = 1000
    line1 = [0,1,2]
    line2 = [0,1,2]
    line3 = [0,1,2]

    for i in line1:
        line2.remove(i)
        line3.remove(i)
        table_choose[0][i] = 1
        print(line2)
        for j in line2:
            line3.remove(j)
            table_choose[1][j] = 1
            for k in line3:
                table_choose[2][k] = 1
                pr_list(table_choose)
                maxnum = 看最晚到達時間(table,table_size,table_choose)
                if maxnum<allmaxnum:
                    allmaxnum = maxnum

                table_choose[2][k] = 0
            table_choose[1][j] = 0
            line3.append(j)

        line2 = [0, 1, 2]
        line3 = [0, 1, 2]

        table_choose = create_table_choose(table_size)

    pr_list(table)
    return allmaxnum








