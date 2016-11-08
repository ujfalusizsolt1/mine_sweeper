import random
import getch
from getch import *

# színek printeléshez
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

table_list = []

# játékfeltételek beállítása

size = int(input(YELLOW + "Please give us the minefield's size: " + END))

minecounter = int(
    input(YELLOW + "How many mines would you like to have on the minefield? " + END))

if minecounter >= size * size:
    gameover = true

markcounter = minecounter

emptycounter = size * size - minecounter

# 0-val táblázat feltöltés
for i in range(0, size):
    table_list.append([])
    for j in range(0, size):
        table_list[i].append(0)

# aknák elhelyezése
i = 0
while i < minecounter:
    x = random.randint(0, size - 1)
    y = random.randint(0, size - 1)
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


while gameover is False:
    # input
    print(YELLOW + "Remaining mines: ", minecounter,
          "Remaining marks: ", markcounter, END)

    if markcounter > 0:
        print(YELLOW + "Do you want to mark the the next target (M-mark, C-check, anything else-exit)? " + END)
        mark = getch()
        if mark == 'm':
            mark = True
        elif mark == 'c':
            mark = False
        else:
            gameover = True
    else:
        mark = False
    wrong_input = True

    if gameover is False:
        while wrong_input is True:

            try:
                firstcoord = int(input(
                    YELLOW + "Please give the number of the row you want to check: " + END)) - 1
                secondcoord = int(input(
                    YELLOW + "Please give the number of the column you want to check: " + END)) - 1

                if firstcoord >= 0 and secondcoord >= 0 and firstcoord <= size - 1 and secondcoord <= size - 1:
                    wrong_input = False
                else:
                    print(RED + "Wrong input, please taget an existing field!" + END)

            except(ValueError):
                print(RED + "Wrong input, please taget an existing field!" + END)

    print("")

    # gameover feltétel/mark ellenőrzése
    if gameover is False:
        if table_list[firstcoord][secondcoord] == 10:
            if mark is True:
                markcounter -= 1
                minecounter -= 1
                table_list[firstcoord][secondcoord] = 12
            elif mark is False:
                gameover = True
                print(RED + "Aknára léptél és felrobbantál a picsába." + END)
                print("")
        elif table_list[firstcoord][secondcoord] == 12:
            if mark is False:
                gameover = True
                print(RED + "Aknára léptél és felrobbantál a picsába." + END)
                print("")
            elif mark is True:
                markcounter += 1
                minecounter += 1
                table_list[firstcoord][secondcoord] = 10
        elif table_list[firstcoord][secondcoord] == 11:
            if mark is True:
                markcounter += 1
                table_list[firstcoord][secondcoord] = 0
        elif table_list[firstcoord][secondcoord] == 0:
            if mark is True:
                markcounter -= 1
                table_list[firstcoord][secondcoord] = 11

    minesaround = 0

    # megnézi a megjelölt mező környzetében hány akna van, ha a játékos a
    # table_list valamelyik szélét jelölte meg, akkor sem lép ki a a 2D-s
    # listából
    if gameover is False and mark is False:
        if firstcoord == 0:
            for i in range(0, 2):
                if secondcoord == 0:
                    for j in range(0, 2):
                        if table_list[firstcoord + i][secondcoord + j] == 10 or table_list[firstcoord + i][secondcoord + j] == 12:
                            minesaround += 1
                elif secondcoord == size - 1:
                    for j in range(-1, 1):
                        if table_list[firstcoord + i][secondcoord + j] == 10 or table_list[firstcoord + i][secondcoord + j] == 12:
                            minesaround += 1
                else:
                    for j in range(-1, 2):
                        if table_list[firstcoord + i][secondcoord + j] == 10 or table_list[firstcoord + i][secondcoord + j] == 12:
                            minesaround += 1
        elif firstcoord == size - 1:
            for i in range(-1, 1):
                if secondcoord == 0:
                    for j in range(0, 2):
                        if table_list[firstcoord + i][secondcoord + j] == 10 or table_list[firstcoord + i][secondcoord + j] == 12:
                            minesaround += 1
                elif secondcoord == size - 1:
                    for j in range(-1, 1):
                        if table_list[firstcoord + i][secondcoord + j] == 10 or table_list[firstcoord + i][secondcoord + j] == 12:
                            minesaround += 1
                else:
                    for j in range(-1, 2):
                        if table_list[firstcoord + i][secondcoord + j] == 10 or table_list[firstcoord + i][secondcoord + j] == 12:
                            minesaround += 1
        else:
            for i in range(-1, 2):
                if secondcoord == 0:
                    for j in range(0, 2):
                        if table_list[firstcoord + i][secondcoord + j] == 10 or table_list[firstcoord + i][secondcoord + j] == 12:
                            minesaround += 1
                elif secondcoord == size - 1:
                    for j in range(-1, 1):
                        if table_list[firstcoord + i][secondcoord + j] == 10 or table_list[firstcoord + i][secondcoord + j] == 12:
                            minesaround += 1
                else:
                    for j in range(-1, 2):
                        if table_list[firstcoord + i][secondcoord + j] == 10 or table_list[firstcoord + i][secondcoord + j] == 12:
                            minesaround += 1
        table_list[firstcoord][secondcoord] = minesaround
        minesaround = 0
        emptycounter -= 1

    # table list kiprintelése
    for i in range(0, size + 1):
        for j in range(0, size + 1):
            if i == 0 and j != 0:
                print(GREEN, j, END, sep='', end=" ")
            elif i != 0 and j == 0:
                print(GREEN, i, END, sep='', end=" ")
            elif i == 0 and j == 0:
                print(" ", end=" ")
            else:
                if table_list[i - 1][j - 1] == 0:
                    print("O", end=" ")
                elif table_list[i - 1][j - 1] == 10:
                    print("O", end=" ")
                elif table_list[i - 1][j - 1] == 9:
                    print(" ", end=" ")
                elif table_list[i - 1][j - 1] == 11 or table_list[i - 1][j - 1] == 12:
                    print(RED + "X", end=" " + END)
                else:
                    print(table_list[i - 1][j - 1], end=' ')
        print("")

    print("")

    if gameover is True:
        print(RED + "GAME OVER. YOU LOST!" + END)

    if minecounter == 0 or emptycounter == 0:
        gameover = True
        print(GREEN + "CONGRATULATIONS! YOU WON!" + END)
