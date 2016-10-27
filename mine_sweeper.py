import random

gameover = False

table_list= []

mine_list=[]

size = int(input("Please give us the minefield's size: "))

minecounter = int(input("How many mines would you like to have on the minefield? "))

if minecounter >= size*size:
    gameover = true

markcounter = minecounter

# 0-val táblázat feltöltés
for i in range(0,size):
    table_list.append([])
    mine_list.append([])
    for j in range(0,size):
        table_list[i].append(0)
        mine_list[i].append(0)

# aknák elhelyezése
for i in range(0,minecounter):
    if table_list[random.randint(0, size-1)][random.randint(0, size-1)] == 0:
        table_list[random.randint(0, size-1)][random.randint(0, size-1)] = 10
    else:
        i -= 1

for i in range(0,size):
    for j in range(0,size):
        if table_list[i][j] == 10:
            mine_list[i][j] = "X"


# table felprintelése
for i in range(0, size):
    for j in range(0, size):
        print("O", end=" ")
    print("")
    




while gameover == False:

    print("Remaining mines: ", minecounter, "Remaining marks: ", markcounter)

    if markcounter > 0:
        mark = input("Do you want to mark the the next target (M-mark, C-check, anything else-exit)? ")
        if mark == 'M':
            mark = True
        elif mark == 'C':
            mark = False
        else:
            gameover = True
    else:
        mark = False
    
    if gameover == False:
        firstcoord = int(input("Please give the number of the row you want to check: "))-1

        secondcoord = int(input("Please give the number of the column you want to check: "))-1



    # gameover feltétel/mark ellenőrzése
    if gameover == False:
        if table_list[firstcoord][secondcoord] == 10:
            if mark == True:
                markcounter -= 1
                minecounter -= 1
                table_list[firstcoord][secondcoord] = 12
            elif mark == False:
                gameover = True
                print("Aknára léptél és felrobbantál a picsába.")
        elif table_list[firstcoord][secondcoord] == 12:
            if mark == False:
                gameover = True
                print("Aknára léptél és felrobbantál a picsába.")
            elif mark == True:
                markcounter += 1
                table_list[firstcoord][secondcoord] = 10
        elif table_list[firstcoord][secondcoord] == 11:
            if mark == True:
                markcounter += 1
                table_list[firstcoord][secondcoord] = 0
        elif table_list[firstcoord][secondcoord] == 0:
            if mark == True:
                markcounter -= 1
        table_list[firstcoord][secondcoord] = 11


    minesaround = 0


    if gameover == False and mark == False:
        # megnézi a megjelölt mező környzetében hány akna van
        for i in range(-1,2):
            for j in range(-1,2):
                try:
                    if table_list[firstcoord+i][secondcoord+j] == 10 or table_list[firstcoord+i][secondcoord+j] == 12:
                            minesaround += 1
                except IndexError:
                    pass

        if minesaround == 0:
            table_list[firstcoord][secondcoord] = 9
        else:
            table_list[firstcoord][secondcoord] = minesaround
        minesaround = 0
                        


    # table list kiprintelése
    for i in range(0, size+1):
        for j in range(0, size+1):
            if i == 0 and j != 0:
                print(j, end=" ")
            elif i != 0 and j == 0:
                print(i, end=" ")
            elif i == 0 and j ==0:
                print(" ",end=" ")
            else:
                if table_list[i-1][j-1] == 0:
                    print("O", end=" ")
                elif table_list[i-1][j-1] == 10:
                    print("O", end=" ")
                elif table_list[i-1][j-1] == 9:
                    print(" ", end=" ")
                elif table_list[i-1][j-1] == 11 or table_list[i-1][j-1] == 12:
                    print("X", end=" ")
                else:
                    print(table_list[i-1][j-1], end=' ')
        print("")

    print("")

    # aknamező kiprintelése

    for i in range(0,size):
        for j in range(0,size):
            print(table_list[i][j], end= ' ')
        print("")

    if minecounter == 0:
        gameover = True
        print("CONGRATULATIONS! YOU WON!")
    
        
            

    

