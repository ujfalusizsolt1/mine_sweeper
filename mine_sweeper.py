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

    minecounter = 15

while gameover == False:

    
    mark=bool(input("Do you want to mark the the next target? "))
    
    firstcoord=int(input("Please give the number of the row you want to check: "))

    secondcoord=int(input("Please give the number of the column you want to check: "))


    if mine_list[firstcoord][secondcoord] == 10:
        if mark == True:
            minecounter -= 1
        elif mark == False:
            gameover = True
            print("Aknára léptél és felrobbantál a picsába.")

    minesaround = 0

    if gameover == False and mark == False:
        if firstcoord == 0:
            for i in range(0,1):
                if secondcoord == 0:
                    for j in range(0,1):
                        if mine_list[firstcoord+i][secondcoord+j] == 10:
                            minesaround += 1
                elif secondcoord == 8:
                    for j in range(-1,0):
                        if mine_list[firstcoord+i][secondcoord+j] == 10:
                            minesaround += 1
                else:
                    for j in range(-1,1):
                        if mine_list[firstcoord+i][secondcoord+j] == 10:
                            minesaround += 1
        elif firstcoord == 8:
            for i in range(-1,0):
                if secondcoord == 0:
                    for j in range(0,1):
                        if mine_list[firstcoord+i][secondcoord+j] == 10:
                            minesaround += 1
                elif secondcoord == 8:
                    for j in range(-1,0):
                        if mine_list[firstcoord+i][secondcoord+j] == 10:
                            minesaround += 1
                else:
                    for j in range(-1,1):
                        if mine_list[firstcoord+i][secondcoord+j] == 10:
                            minesaround += 1
        else:
            for i in range(-1,1):
                if secondcoord == 0:
                    for j in range(0,1):
                        if mine_list[firstcoord+i][secondcoord+j] == 10:
                            minesaround += 1
                elif secondcoord == 8:
                    for j in range(-1,0):
                        if mine_list[firstcoord+i][secondcoord+j] == 10:
                            minesaround += 1
                else:
                    for j in range(-1,1):
                        if mine_list[firstcoord+i][secondcoord+j] == 10:
                            minesaround += 1
        table_list[firstcoord][secondcoord] = minesaround
        minesaround = 0


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

    print("")

    for i in range(0,9):
        for j in range(0,9):
            print(mine_list[i][j], end= ' ')
        print("")
    
        
            

    

