import random
import getch
from getch import *
import color
from color import colors
# import global_vars


def mine_finder(returnvalues):

    # megnézi a megjelölt mező környzetében hány akna van, ha a játékos a
    # table_list valamelyik szélét jelölte meg, akkor sem lép ki a a 2D-s
    # listából
    global table_list
    global gameover
    global mark

    firstcoord = returnvalues['firstcoord']
    secondcoord = returnvalues['secondcoord']
    size = returnvalues['size']
    emptycounter = returnvalues['emptycounter']
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
        emptycounter -= 1
        returnvalues['emptycounter'] = emptycounter
        returnvalues['minesaround'] = minesaround

    return minesaround


def table_print(returnvalues):
    # table list kiprintelése
    global table_list

    size = returnvalues['size']

    for i in range(0, size + 1):
        for j in range(0, size + 1):
            if i == 0 and j != 0:
                print(colors['GREEN'], j, colors['END'], sep='', end=" ")
            elif i != 0 and j == 0:
                print(colors['GREEN'], i, colors['END'], sep='', end=" ")
            elif i == 0 and j == 0:
                print(" ", end=" ")
            else:
                if table_list[i - 1][j - 1] == 0 or table_list[i - 1][j - 1] == 10:
                    print("O", end=" ")
                elif table_list[i - 1][j - 1] == 9:
                    print(" ", end=" ")
                elif table_list[i - 1][j - 1] == 11 or table_list[i - 1][j - 1] == 12:
                    print(colors['RED'] + "X", end=" " + colors['END'])
                elif table_list[i - 1][j - 1] >= 13 and table_list[i - 1][j - 1] <= 20:
                    print("O", end=" ")
                else:
                    print(table_list[i - 1][j - 1], end=' ')
        print("")

    print("")


def mark_gameover_check(returnvalues):
    global table_list
    global gameover
    global mark

    firstcoord = returnvalues['firstcoord']
    secondcoord = returnvalues['secondcoord']
    minecounter = returnvalues['minecounter']
    markcounter = returnvalues['markcounter']

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

        returnvalues['markcounter'] = markcounter
        returnvalues['minecounter'] = minecounter


def input_handler(returnvalues):

    global gameover
    global mark

    firstcoord = 0
    secondcoord = 0
    minecounter = returnvalues['minecounter']
    size = returnvalues['size']

    markcounter = returnvalues['markcounter']

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
    returnvalues['firstcoord'] = firstcoord
    returnvalues['secondcoord'] = secondcoord
    return returnvalues


def table_preview(returnvalues):
    size = returnvalues['size']
    # table felprintelése
    for i in range(0, size):
        for j in range(0, size):
            print("O", end=" ")
        print("")
    print("")


def mine_layer(returnvalues):
    # aknák elhelyezése
    global table_list
    minecounter = returnvalues['minecounter']
    size = returnvalues['size']
    i = 0

    while i < minecounter:

        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)

        if table_list[x][y] == 0:
            table_list[x][y] = 10
            i += 1
        else:
            pass


def mine_counter(returnvalues):
    global table_list
    global mark

    size = returnvalues['size']
    mark = False

    for sor in range(size):
        for oszlop in range(size):
            if table_list[sor][oszlop] != 10:
                returnvalues['firstcoord'] = sor
                returnvalues['secondcoord'] = oszlop
                seged = mine_finder(returnvalues)
                if seged != 0:
                    table_list[sor][oszlop] = seged + 12
    return


def table_build(returnvalues):
    # 0-val táblázat feltöltés
    global table_list
    size = returnvalues['size']
    for i in range(0, size):
        table_list.append([])
        for j in range(0, size):
            table_list[i].append(0)


def set_conditions(returnvalues):

    global gameover

    size = returnvalues['size']
    minecounter = returnvalues['minecounter']
    markcounter = returnvalues['markcounter']
    emptycounter = returnvalues['emptycounter']

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

    while minecounter < 1 or minecounter > size * size:
        try:
            minecounter = int(input(colors[
                'YELLOW'] + "How many mines would you like to have on the minefield? " + colors['END']))
            if minecounter <= 0 or minecounter > size * size:
                raise ValueError
        except ValueError:
            print('wrong input')
            continue

    markcounter = minecounter

    emptycounter = size * size - minecounter

    returnvalues['size'] = size
    returnvalues['markcounter'] = markcounter
    returnvalues['minecounter'] = minecounter
    returnvalues['emptycounter'] = emptycounter
    return returnvalues


def reveal(returnvalues):
    global table_list
    firstcoord = returnvalues['firstcoord']
    secondcoord = returnvalues['secondcoord']
    size = returnvalues['size']
    edge = False
    sor = 0
    oszlop = 0

    # DOWN
    while edge is False:
        edge = False
        basesor = firstcoord + sor
        baseoszlop = secondcoord
        while edge is False:
            if table_list[basesor][baseoszlop + oszlop] == 0 or table_list[basesor][baseoszlop + oszlop] == 9:
                table_list[basesor][baseoszlop + oszlop] = 9
            elif table_list[basesor][baseoszlop + oszlop] >= 13 and table_list[basesor][baseoszlop + oszlop] <= 20:
                table_list[basesor][baseoszlop + oszlop] -= 12
            else:
                edge = True
            if baseoszlop + oszlop >= size - 1:
                edge = True
            oszlop += 1

        oszlop = 0
        edge = False
        while edge is False:
            if table_list[basesor][baseoszlop + oszlop] == 0 or table_list[basesor][baseoszlop + oszlop] == 9:
                table_list[basesor][baseoszlop + oszlop] = 9
            elif table_list[basesor][baseoszlop + oszlop] >= 13 and table_list[basesor][baseoszlop + oszlop] <= 20:
                table_list[basesor][baseoszlop + oszlop] -= 12
                edge = True
            else:
                edge = True
            if baseoszlop + oszlop <= 0:
                edge = True
                basesor += 1
            oszlop -= 1
        oszlop = 0
        if basesor + sor >= size - 1:
            edge = True
        sor += 1
    sor = 0
    edge = False

    # UP
    while edge is False:
        edge = False
        basesor = firstcoord + sor
        baseoszlop = secondcoord
        while edge is False:
            if table_list[basesor][baseoszlop + oszlop] == 0 or table_list[basesor][baseoszlop + oszlop] == 9:
                table_list[basesor][baseoszlop + oszlop] = 9
            elif table_list[basesor][baseoszlop + oszlop] >= 13 and table_list[basesor][baseoszlop + oszlop] <= 20:
                table_list[basesor][baseoszlop + oszlop] -= 12
                edge = True
            else:
                edge = True
            if baseoszlop + oszlop >= size - 1:
                edge = True
            oszlop += 1

        oszlop = 0
        edge = False
        while edge is False:
            if table_list[basesor][baseoszlop + oszlop] == 0 or table_list[basesor][baseoszlop + oszlop] == 9:
                table_list[basesor][baseoszlop + oszlop] = 9
            elif table_list[basesor][baseoszlop + oszlop] >= 13 and table_list[basesor][baseoszlop + oszlop] <= 20:
                table_list[basesor][baseoszlop + oszlop] -= 12
            else:
                edge = True
            if baseoszlop + oszlop <= 0:
                edge = True
                basesor -= 1
            oszlop -= 1
        oszlop = 0
        if basesor + sor <= 0:
            edge = True
        sor -= 1
    sor = 0
    edge = False

    # RIGHT
    while edge is False:
        edge = False
        basesor = firstcoord
        baseoszlop = secondcoord + oszlop
        while edge is False:
            if table_list[basesor + sor][baseoszlop] == 0 or table_list[basesor + sor][baseoszlop] == 9:
                table_list[basesor + sor][baseoszlop] = 9
            elif table_list[basesor + sor][baseoszlop] >= 13 and table_list[basesor + sor][baseoszlop] <= 20:
                table_list[basesor + sor][baseoszlop] -= 12
            else:
                edge = True
            if basesor + sor >= 1:
                edge = True
            sor += 1

        sor = 0
        edge = False
        while edge is False:
            if table_list[basesor + sor][baseoszlop] == 0 or table_list[basesor + sor][baseoszlop] == 9:
                table_list[basesor + sor][baseoszlop] = 9
            elif table_list[basesor + sor][baseoszlop] >= 13 and table_list[basesor + sor][baseoszlop] <= 20:
                table_list[basesor + sor][baseoszlop] -= 12
                edge = True
            else:
                edge = True
            if basesor + sor <= 0:
                edge = True
                baseoszlop += 1
            sor -= 1
        sor = 0
        if baseoszlop + oszlop >= size - 1:
            edge = True
        oszlop += 1
    oszlop = 0

    # LEFT
    while edge is False:
        edge = False
        basesor = firstcoord
        baseoszlop = secondcoord + oszlop
        while edge is False:
            if table_list[basesor + sor][baseoszlop] == 0 or table_list[basesor + sor][baseoszlop] == 9:
                table_list[basesor + sor][baseoszlop] = 9
            elif table_list[basesor + sor][baseoszlop] >= 13 and table_list[basesor + sor][baseoszlop] <= 20:
                table_list[basesor + sor][baseoszlop] -= 12
                edge = True
            else:
                edge = True
            if basesor + sor >= size - 1:
                edge = True
            sor += 1

        sor = 0
        edge = False
        while edge is False:
            if table_list[basesor + sor][baseoszlop] == 0 or table_list[basesor + sor][baseoszlop] == 9:
                table_list[basesor + sor][baseoszlop] = 9
            elif table_list[basesor + sor][baseoszlop] >= 13 and table_list[basesor + sor][baseoszlop] <= 20:
                table_list[basesor + sor][baseoszlop] -= 12
            else:
                edge = True
            if basesor + sor <= 0:
                edge = True
                baseoszlop -= 1
            sor -= 1
        sor = 0
        if baseoszlop + oszlop <= 0:
            edge = True
        oszlop -= 1
    oszlop = 0
    edge = False

    return


def main():

    global table_list
    global gameover
    global mark

    returnvalues = {'size': 0, 'minecounter': 0, 'firstcoord': 0,
                    'secondcoord': 0, 'markcounter': 0, 'emptycounter': 0, 'minesaround': 0}

    table_list = []
    firstcoord = 0
    secondcoord = 0
    minecounter = 0
    size = 0
    gameover = False
    mark = ""

    returnvalues = set_conditions(returnvalues)
    table_build(returnvalues)

    mine_layer(returnvalues)

    mine_counter(returnvalues)

    table_preview(returnvalues)

    while not gameover:

        input_handler(returnvalues)
        mark_gameover_check(returnvalues)
        mine_finder(returnvalues)
        firstcoord = returnvalues['firstcoord']
        secondcoord = returnvalues['secondcoord']
        if table_list[firstcoord][secondcoord] == 9 or table_list[firstcoord][secondcoord] == 0:
            reveal(returnvalues)
        table_print(returnvalues)
        print(table_list)
        minecounter = returnvalues['minecounter']
        emptycounter = returnvalues['emptycounter']
        if gameover is True:
            print(colors['RED'] + "GAME OVER. YOU LOST!" + colors['END'])

        if minecounter == 0 or emptycounter == 0:
            gameover = True
            print(colors['GREEN'] +
                  "CONGRATULATIONS! YOU WON!" + colors['END'])


main()
