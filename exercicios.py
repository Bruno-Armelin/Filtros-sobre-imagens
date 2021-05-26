"""
Bruno Gomes - 2020196556

matriz numpy é equivalente a [[[0] * 3] * width] * height
"""

import cv2 as cv
import numpy as np

def getSize(img):
    return len(img[0]), len(img)

def flipVertical(img):
    width, height = getSize(img)
    imgDest = np.zeros((height, width, 3), np.uint8)
    cHeight = height - 1
    for i in range(height):
        for j in range(width):
            imgDest[i][j][0] = img[cHeight - i][j][0]
            imgDest[i][j][1] = img[cHeight - i][j][1]
            imgDest[i][j][2] = img[cHeight - i][j][2]

    cv.imshow("flipVertical", imgDest)

def mirrorImg(img):
    width, height = getSize(img)
    imgDest = np.zeros((height, width, 3), np.uint8)
    cWidth = width - 1
    for i in range(height):
        for j in range(width):
            imgDest[i][j][0] = img[i][cWidth - j][0]
            imgDest[i][j][1] = img[i][cWidth - j][1]
            imgDest[i][j][2] = img[i][cWidth - j][2]

    cv.imshow("mirroredImg", imgDest)

def transpose(img):
    height, width = getSize(img) #returns invertidos
    imgDest = np.zeros((height, width, 3), np.uint8)

    for i in range(height):
        for j in range(width):
            imgDest[i][j][0] = img[j][i][0]
            imgDest[i][j][1] = img[j][i][1]
            imgDest[i][j][2] = img[j][i][2]

    cv.imshow("transpose", imgDest)

def rotateRight(img):
    height, width = getSize(img) #returns invertidos
    imgDest = np.zeros((height, width, 3), np.uint8)
    cWidth = width - 1
    for i in range(height):
        for j in range(width):
            imgDest[i][j][0] = img[cWidth - j][i][0]
            imgDest[i][j][1] = img[cWidth - j][i][1]
            imgDest[i][j][2] = img[cWidth - j][i][2]

    cv.imshow("rotateRight", imgDest)

def rotateLeft(img):
    height, width = getSize(img)  # returns invertidos
    imgDest = np.zeros((height, width, 3), np.uint8)
    cHeight = height - 1
    for i in range(height):
        for j in range(width):
            imgDest[i][j][0] = img[j][cHeight - i][0]
            imgDest[i][j][1] = img[j][cHeight - i][1]
            imgDest[i][j][2] = img[j][cHeight - i][2]

    cv.imshow("rotateLeft", imgDest)

img = cv.imread('unifafibe.jpg') #

flipVertical(img)
mirrorImg(img)
transpose(img)
rotateRight(img)
rotateLeft(img)

cv.waitKey()
