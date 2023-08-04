#This code has been made by Timur Hromek, please don't copy without my mention.

#Dear programer:
#when I wrote this code, only God and
#I knew how it worked.
#Now only God knows it!

#Therfore, don't touch the code otherwise you will break it.

#Total hours wasted on this code: 5h25

import math
import numpy as np
M = 10
N = 10

mPixels = []

def initPixels(M, N):
    mPixels = [[0] * N for _ in range(M)]
    return mPixels


def drawPicture(mPicture, M, N):
    print('    ', end='')
    for j in range(N):
        print(f'{j:2}', end=' ')
    print('\n')

    for i in range(M):
        print(f'{i:2} |', end='')
        for j in range(N):
            if mPicture[i][j] == 1:
                print('x ', end='')
            else:
                print('  ', end='')
        print('')


def drawSquare(mPicture, M, N, x, y, size):
    for i in range(y, y + size):
        for j in range(x, x + size):
            if 0 <= i < M and 0 <= j < N:
                mPicture[i][j] = 1
              


def drawCircle(mPicture, M, N, x_center, y_center, radius):
    for i in range(M):
        for j in range(N):
            distance = math.sqrt((i - y_center) ** 2 + (j - x_center) ** 2)
            if distance <= radius:
                if 0 <= i < M and 0 <= j < N:
                    mPicture[i][j] = 1


def detectObject(mPicture, M, N):
    objects = []
    topRow = -1
    topCol = -1
    foundTop = False
    for i in range(M):
        for j in range(N):
            if mPicture[i][j] == 1:
                topRow = i
                topCol = j
                foundTop = True
                break
        if foundTop:
            break
    if topRow == -1:
        return []
    print(topRow, topCol)

    if mPicture[topRow][topCol+1] == 1:
        return ["square"]
    else:
        return ["circle"]




mPixels = initPixels(M, N)

while True:
    print('\n')
    print('Picture:')
    drawPicture(mPixels, M, N)
    op = input("\nInsert 1 to draw a square or 2 to draw a circle. Enter any other key to exit: ")

    if op == "1":
        x = int(input("Enter the x-coordinate of the top-left corner: "))
        y = int(input("Enter the y-coordinate of the top-left corner: "))
        size = int(input("Enter the size of the square: "))
        drawSquare(mPixels, M, N, x, y, size)
    elif op == "2":
        x_center = int(input("Enter the x-coordinate of the center: "))
        y_center = int(input("Enter the y-coordinate of the center: "))
        radius = int(input("Enter the radius of the circle: "))
        drawCircle(mPixels, M, N, x_center, y_center, radius)
    else:
        break

detected_objects = detectObject(mPixels, M, N)
print("\nDetected objects:")
if len(detected_objects) > 0:
    #shape = recognizeShape(detected_objects)
    print(detected_objects[0])
else:
    print("No recognizable shape detected.")
