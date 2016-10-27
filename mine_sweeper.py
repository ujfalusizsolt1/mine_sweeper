import random

PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'

gameover = False

table_list= []

size = 5 #int(input(YELLOW + "Please give us the minefield's size: " + END))

minecounter = 5 #int(input(YELLOW + "How many mines would you like to have on the minefield? " + END))

if minecounter >= size*size:
    gameover = true

markcounter = minecounter

emptycounter = size * size - minecounter

# 0-val táblázat feltöltés
for i in range(0,size):
    table_list.append([])
    for j in range(0,size):
        table_list[i].append(0)

# aknák elhelyezése
i= 0
while i < minecounter:
    x = random.randint(0, size-1)
    y = random.randint(0, size-1)
    if table_list[x][y] == 0:
        table_list[x][y] = 10
        i += 1
    else:
        pass

# table felprintelése
for i in range(0, size):
    for j in range(0, size):
        print("O", end=" ")
    print("")
    




while gameover == False:

    print(YELLOW + "Remaining mines: ", minecounter, "Remaining marks: ", markcounter , END)

    if markcounter > 0:
        mark = "M" #input(YELLOW + "Do you want to mark the the next target (M-mark, C-check, anything else-exit)? " + END)
        if mark == 'M':
            mark = True
        elif mark == 'C':
            mark = False
        else:
            gameover = True
    else:
        mark = False
    
    if gameover == False:
        firstcoord = 1 #int(input(YELLOW + "Please give the number of the row you want to check: " + END))-1

        secondcoord = 1 #int(input(YELLOW + "Please give the number of the column you want to check: " + END))-1



    # gameover feltétel/mark ellenőrzése
    if gameover == False:
        if table_list[firstcoord][secondcoord] == 10:
            if mark == True:
                markcounter -= 1
                minecounter -= 1
                table_list[firstcoord][secondcoord] = 12
            elif mark == False:
                gameover = True
                print(RED + "Aknára léptél és felrobbantál a picsába." + END)
        elif table_list[firstcoord][secondcoord] == 12:
            if mark == False:
                gameover = True
                print(RED + "Aknára léptél és felrobbantál a picsába." + END)
            elif mark == True:
                markcounter += 1
                minecounter += 1
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

        emptycounter -=1                        


    # table list kiprintelése
    for i in range(0, size+1):
        for j in range(0, size+1):
            if i == 0 and j != 0:
                print(GREEN, j, END,sep='', end=" ")
            elif i != 0 and j == 0:
                print(GREEN, i, END,sep='', end=" ")
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
                    print(RED + "X", end=" " + END)
                else:
                    print(table_list[i-1][j-1], end=' ')
        print("")

    print("")

    # aknamező kiprintelése

    for i in range(0,size):
        for j in range(0,size):
            print(table_list[i][j], end= ' ')
        print("")

    if gameover == True:
        print(RED + "GAME OVER. YOU LOST!" + END)

    if minecounter == 0 or emptycounter == 0:
        gameover = True
        print(GREEN + "CONGRATULATIONS! YOU WON!" + END)

    
    
        
            

    

        
            

    

