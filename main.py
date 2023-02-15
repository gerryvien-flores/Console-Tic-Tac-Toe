#!/usr/bin/python3

import time
import random
from tabulate import tabulate

def placeMarks(row, column, mark):
    if grid[row - 1][column - 1] == " ":
        grid[row - 1][column -1] = mark
    else:
        print("Tile is already occupied.")

def isBlank(row, column):
    if grid[row - 1][column - 1] == " ":
        blank = True
    else:
        blank = False

    return blank

def showCell():
    print(tabulate(grid, headers, showindex = headers, tablefmt = "fancy_grid"))

def didWin(mark, counterMark):
    won = False
    #Diagonal, Horizontal, Vertical
    if grid[0][0] == mark and grid[0][0] != counterMark:
        if grid[1][1] == mark and grid[1][1] != counterMark:
            if grid[2][2] == mark and grid[2][2] != counterMark: #Diag
                won = True

    if grid[2][0] == mark and grid[2][0] != counterMark:
        if grid[1][1] == 1 and grid[1][1] != counterMark:
            if grid[0][2] == 1 and grid[0][2] != counterMark:
                won = True

    if grid[0][0] == mark and grid[0][0] != counterMark:
        if grid[0][1] == mark and grid[0][1] != counterMark:
            if grid[0][2] == mark and grid[0][2] != counterMark: #Hori
                won = True

    if grid[1][0] == mark and grid[1][0] != counterMark:
        if grid[1][1] == mark and grid[1][1] != counterMark:
            if grid[1][2] == mark and grid[1][2] != counterMark:
                won = True

    if grid[2][0] == mark and grid[2][0] != counterMark:
        if grid[2][1] == mark and grid[2][1] != counterMark:
            if grid[2][2] == mark and grid[2][2] != counterMark:
                won = True

    if grid[0][0] == mark and grid[0][0] != counterMark:
        if grid[1][0] == mark and grid[1][0] != counterMark:
            if grid[2][0] == mark and grid[2][0] != counterMark: #Verti
                won = True

    if grid[0][1] == mark and grid[0][1] != counterMark:
        if grid[1][1] == mark and grid[1][1] != counterMark:
            if grid[2][1] == mark and grid[2][1] != counterMark:
                won = True

    if grid[0][2] == mark and grid[0][2] != counterMark:
        if grid[1][2] == mark and grid[1][2] != counterMark:
            if grid[2][2] == mark and grid[2][2] != counterMark:
                won = True

    return won

def isDraw():
    draw = False
    if not any(" " in x for x in grid):
        draw = True

    return draw


def tictactoe():
    while True:
        while True:
            try:
                showCell()
                print("Where do you want to place you mark \'O\'?")
                rowInput = input("Row: ")
                colInput = input("Column: ")
                if isBlank(int(rowInput), int(colInput)):
                    placeMarks(int(rowInput), int(colInput), "O")
                    break
                else:
                    print("Tile is occupied")
            except (IndexError, ValueError):
                print("Unknown Input: Please refer to the row and column guide.")

        if didWin("O", "X"):
            showCell()
            print("You Win")
            break
        elif isDraw():
            showCell()
            print("Game is Draw")
            break

        while True:
            showCell()
            print("Computer's Turn...")
            time.sleep(2)
            rowInput = random.randint(0,2)
            colInput = random.randint(0,2)
            if isBlank(int(rowInput), int(colInput)):
                placeMarks(int(rowInput), int(colInput), "X")
                break
            else:
                print("Computer is thinking...")

        if didWin("X", "O"):
            showCell()
            print("CPU Win")
            break
        elif isDraw():
            showCell()
            print("Game is Draw")
            break

grid = [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]]

headers = [1,2,3]

query = input("Do you want to play?[Y/n]: ").casefold()
isPlaying = True

while isPlaying:
    if query == "y":
        tictactoe()
        break
    elif query == "n":
        print("Thank you! Have a nice day.")
        break
    else:
        print("Unknown Option.")

