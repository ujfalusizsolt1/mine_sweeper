gameover = False

import random

table_list= []

mine_list=[]

for i in range(0,9):
    table_list.append([])
    mine_list.append([])
    for j in range(0,9):
        table_list[i].append(0)
        mine_list[i].append(0)

for i in range(0,15):
    mine_list[random.randint(0, 8)][random.randint(0, 8)] = 10


for i in range(0, 9):
    for j in range(0, 9):
        if table_list[i][j] == 0:
            print("O", end=" ")
        elif table_list[i][j] == 10:
            print("#", end=" ")
        elif table_list[i][j] == 9:
            print("", end=" ")
        else:
            print(table_list[i][j], end=' ')
    print("")


#while gameover = False:
    

