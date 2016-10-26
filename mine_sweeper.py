gameover = False

import random

table_list= []

mine_list=[]

# 0-val táblázat feltöltés
for i in range(0,9):
    table_list.append([])
    mine_list.append([])
    for j in range(0,9):
        table_list[i].append(0)
        mine_list[i].append(0)

# aknák elhelyezése
for i in range(0,15):
    table_list[random.randint(0, 8)][random.randint(0, 8)] = 10

for i in range(0,9):
    for j in range(0,9):
        if table_list[i][j] == 10:
            mine_list[i][j] = "X"


# table felprintelése
for i in range(0, 9):
    for j in range(0, 9):
        print("O", end=" ")
    print("")

    minecounter = 14

while gameover == False:

    
    mark= False #bool(input("Do you want to mark the the next target? "))
    
    firstcoord=1  #int(input("Please give the number of the row you want to check: "))

    secondcoord=2  #int(input("Please give the number of the column you want to check: "))



    # gameover/check ellenőrzése
    if table_list[firstcoord][secondcoord] == 10:
        if mark == True:
            minecounter -= 1
            table_list[firstcoord][secondcoord] = 12
        elif mark == False:
            gameover = True
            print("Aknára léptél és felrobbantál a picsába.")

    minesaround = 0



    # megnézi a megjelölt mező környzetében hány akna van
    if gameover == False and mark == False:
        if firstcoord == 0:
            for i in range(0,1):
                if secondcoord == 0:
                    for j in range(0,1):
                        if table_list[firstcoord+i][secondcoord+j] == 10 or table_list[firstcoord+i][secondcoord+j] == 12:
                            minesaround += 1
                elif secondcoord == 8:
                    for j in range(-1,0):
                        if table_list[firstcoord+i][secondcoord+j] == 10 or table_list[firstcoord+i][secondcoord+j] == 12:
                            minesaround += 1
                else:
                    for j in range(-1,1):
                        if table_list[firstcoord+i][secondcoord+j] == 10 or table_list[firstcoord+i][secondcoord+j] == 12:
                            minesaround += 1
        elif firstcoord == 8:
            for i in range(-1,0):
                if secondcoord == 0:
                    for j in range(0,1):
                        if table_list[firstcoord+i][secondcoord+j] == 10 or table_list[firstcoord+i][secondcoord+j] == 12:
                            minesaround += 1
                elif secondcoord == 8:
                    for j in range(-1,0):
                        if table_list[firstcoord+i][secondcoord+j] == 10 or table_list[firstcoord+i][secondcoord+j] == 12:
                            minesaround += 1
                else:
                    for j in range(-1,1):
                        if table_list[firstcoord+i][secondcoord+j] == 10 or table_list[firstcoord+i][secondcoord+j] == 12:
                            minesaround += 1
        else:
            for i in range(-1,1):
                if secondcoord == 0:
                    for j in range(0,1):
                        if table_list[firstcoord+i][secondcoord+j] == 10 or table_list[firstcoord+i][secondcoord+j] == 12:
                            minesaround += 1
                elif secondcoord == 8:
                    for j in range(-1,0):
                        if table_list[firstcoord+i][secondcoord+j] == 10 or table_list[firstcoord+i][secondcoord+j] == 12:
                            minesaround += 1
                else:
                    for j in range(-1,1):
                        if table_list[firstcoord+i][secondcoord+j] == 10 or table_list[firstcoord+i][secondcoord+j] == 12:
                            minesaround += 1
        table_list[firstcoord][secondcoord] = minesaround
        minesaround = 0

    # table list kiprintelése
    for i in range(0, 9):
            for j in range(0, 9):
                if table_list[i][j] == 0:
                    print("O", end=" ")
                elif table_list[i][j] == 10:
                    print("O", end=" ")
                elif table_list[i][j] == 9:
                    print("", end=" ")
                elif table_list[i][j] == 11 or table_list[i][j] == 12:
                    print("X", end=" ")
                else:
                    print(table_list[i][j], end=' ')
            print("")

    print("")

    # aknamező kiprintelése

    for i in range(0,9):
        for j in range(0,9):
            print(table_list[i][j], end= ' ')
        print("")


        
            

    

