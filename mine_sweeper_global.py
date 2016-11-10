import random
import getch
from getch import *
import color
from color import colors
#import global_vars


def mine_finder():

    # megnézi a megjelölt mező környzetében hány akna van, ha a játékos a
    # table_list valamelyik szélét jelölte meg, akkor sem lép ki a a 2D-s
    # listából
    global table_list
    global firstcoord
    global secondcoord
    global size
    global gameover
    global mark
    global emptycounter

    minesaround = 0
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


def table_print():
    # table list kiprintelése
    global table_list
    global size
    for i in range(0, size + 1):
        for j in range(0, size + 1):
            if i == 0 and j != 0:
                print(colors['GREEN'], j, colors['END'], sep='', end=" ")
            elif i != 0 and j == 0:
                print(colors['GREEN'], i, colors['END'], sep='', end=" ")
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
                    print(colors['RED'] + "X", end=" " + colors['END'])
                else:
                    print(table_list[i - 1][j - 1], end=' ')
        print("")

    print("")


def mark_gameover_check():
    global table_list
    global firstcoord
    global secondcoord
    global minecounter
    global gameover
    global mark
    global markcounter
    # gameover feltétel/mark ellenőrzése

    if gameover is False:
        if table_list[firstcoord][secondcoord] == 10:
            if mark:
                markcounter -= 1
                minecounter -= 1
                table_list[firstcoord][secondcoord] = 12
            elif mark is False:
                gameover = True
                print(
                    colors['RED'] + "Aknára léptél és felrobbantál a picsába." + colors['END'])
                print("")
        elif table_list[firstcoord][secondcoord] == 12:
            if mark is False:
                gameover = True
                print(
                    colors['RED'] + "Aknára léptél és felrobbantál a picsába." + colors['END'])
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


def input_handler():
    global firstcoord
    global secondcoord
    global minecounter
    global size
    global gameover
    global mark
    global markcounter

    # input

    print(colors['YELLOW'] + "Remaining mines: ", minecounter,
          "Remaining marks: ", markcounter, colors['END'])

    if markcounter > 0:
        print(colors[
              'YELLOW'] + "Do you want to mark the the next target (M-mark, C-check, anything else-exit)? " + colors['END'])
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
                    colors['YELLOW'] + "Please give the number of the row you want to check: " + colors['END'])) - 1
                secondcoord = int(input(
                    colors['YELLOW'] + "Please give the number of the column you want to check: " + colors['END'])) - 1

                if firstcoord >= 0 and secondcoord >= 0 and firstcoord <= size - 1 and secondcoord <= size - 1:
                    wrong_input = False
                else:
                    print(
                        colors['RED'] + "Wrong input, please taget an existing field!" + colors['END'])

            except(ValueError):
                print(
                    colors['RED'] + "Wrong input, please taget an existing field!" + colors['END'])

    print("")


def table_preview():
    global size
    # table felprintelése
    for i in range(0, size):
        for j in range(0, size):
            print("O", end=" ")
        print("")
    print("")


def mine_layer():
    # aknák elhelyezése
    global table_list
    global minecounter
    global size

    i = 0

    while i < minecounter:

        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)

        if table_list[x][y] == 0:
            table_list[x][y] = 10
            i += 1
        else:
            pass
    return table_list


def table_build():
    # 0-val táblázat feltöltés
    global table_list
    global size
    for i in range(0, size):
        table_list.append([])
        for j in range(0, size):
            table_list[i].append(0)
    return table_list


def set_conditions():
    global minecounter
    global size
    global gameover
    global markcounter
    global emptycounter

    # játékfeltételek beállítása
    while size <= 1:
        try:
            size = int(input(
                colors['YELLOW'] + "Please give us the minefield's size: " + colors['END']))
            if size <= 1:
                raise ValueError
        except ValueError:
            print('wrong input')
            continue
        else:
            break
    while minecounter < 1:
        try:
            minecounter = int(input(colors[
                'YELLOW'] + "How many mines would you like to have on the minefield? " + colors['END']))
            if minecounter <= 0:
                raise ValueError
        except ValueError:
            print('wrong input')
            continue
        else:
            break
    if minecounter >= size * size:
        gameover = True

    markcounter = minecounter

    emptycounter = size * size - minecounter
    return markcounter


def main():

    global table_list
    global firstcoord
    global secondcoord
    global minecounter
    global size
    global gameover
    global mark
    global markcounter
    global emptycounter

    table_list = []
    firstcoord = 0
    secondcoord = 0
    minecounter = 0
    size = 0
    gameover = False
    mark = ""

    markcounter = set_conditions()

    emptycounter = size * size - minecounter

    table_list.append(table_build())

    table_list = mine_layer()

    table_preview()

    while not gameover:

        input_handler()
        mark_gameover_check()
        mine_finder()
        table_print()
        if gameover is True:
            print(colors['RED'] + "GAME OVER. YOU LOST!" + colors['END'])

        if minecounter == 0 or emptycounter == 0:
            gameover = True
            print(colors['GREEN'] +
                  "CONGRATULATIONS! YOU WON!" + colors['END'])


def global_vars():
    # global stuff
    global table_list
    global firstcoord
    global secondcoord
    global minecounter
    global size
    global gameover
    global mark

    table_list = []
    firstcoord = 3
    secondcoord = 3
    minecounter = 3
    size = 3
    gameover = False
    mark = "c"

main()
