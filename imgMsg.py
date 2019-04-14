# -*- coding: UTF-8 -*-

import numpy as np
import cv2
import numpy as np
from queue import Queue, LifoQueue
import time
import copy
from imutils.perspective import four_point_transform
from imutils import contours
import argparse
import imutils
import datetime
from sudoku import *

#image = cv2.imread("pic/p2.jpg")

def magPIC(path):
    image = cv2.imdecode(np.fromfile(path,dtype=np.uint8),-1)
    t1 = time.time()

    data = [[0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    samples = np.load('samples.npy')
    labels = np.load('label.npy')
    print(labels.__len__())
    k = labels.__len__()
    train_label = labels[:k]
    train_input = samples[:k]
    test_input = samples[k:]
    test_label = labels[k:]

    model = cv2.ml.KNearest_create()
    model.train(train_input,cv2.ml.ROW_SAMPLE,train_label)


    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imageBinary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY, 13, 9)
    kernel = cv2.getStructuringElement(cv2.MORPH_OPEN, (3, 3))  # 矩形结构
    imageBinary = cv2.erode(imageBinary, kernel, iterations=1)
    imageBinary = cv2.dilate(imageBinary, kernel, iterations=1)

    cv2.bitwise_not(imageBinary)
    imageBinaryOri = copy.deepcopy(imageBinary)
    edged = cv2.bitwise_not(imageBinary)

    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    docCnt = None

    if len(cnts) > 0:
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
        for c in cnts:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            if len(approx) == 4:
                docCnt = approx
                break

    bkIMG = four_point_transform(image, docCnt.reshape(4, 2))
    output = four_point_transform(imageBinaryOri, docCnt.reshape(4, 2))

    imageBinaryFindNum = copy.deepcopy(cv2.resize(output.copy(),(300, 300), interpolation=cv2.INTER_LINEAR          ))
    bkIMG = cv2.resize(bkIMG.copy(),(350, 350))

    imageBinaryFindNum = copy.deepcopy(output)
    imageBinaryFindNum = cv2.blur(imageBinaryFindNum, (2, 2))
    imageBinaryFindNum= cv2.medianBlur(imageBinaryFindNum, 3)
    imageBinaryFindNum = cv2.adaptiveThreshold(imageBinaryFindNum, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY, 13, 9)

    height,width = imageBinaryFindNum.shape[:2]
    box_h = height/9
    box_w = width/9
    imag, contours, hierarchy = cv2.findContours(imageBinaryFindNum, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    num = 0
    listRec = []

    for i in range(0, len(contours)):
        x, y, w, h = cv2.boundingRect(contours[i])
        dat = float(w) / float(h)
        roi = imageBinaryFindNum[y:y + h, x:x + w]

        if dat < 0.9 and w < 40 and h < 37 and w > 7 and h > 16 and dat>0.3:

            if (x%(box_w))/2< 10 and (y%(box_h))/2 <10:

                num = num + 1
                listTemp = []
                listTemp.append(x)
                listTemp.append(y)
                listTemp.append(w)
                listTemp.append(h)
                listRec.append(listTemp)

    soduko = np.zeros((9, 9),np.int32)
    for i in range(0, len(listRec)):
        x, y, w, h = listRec[i]
        roi = imageBinaryFindNum[y:y + h, x:x + w]
        output = cv2.resize(roi, (20,40), interpolation=cv2.INTER_AREA)
        a, output = cv2.threshold(output, 170, 255, cv2.THRESH_BINARY)

        normalized_roi = output / 255

        sample1 = normalized_roi.reshape((1, 800))
        sample1 = np.array(sample1, np.float32)

        retval, results, neigh_resp, dists = model.findNearest(sample1, 1)
        number = int(results.ravel()[0])

        soduko[int(y / box_h)][int(x / box_w)] = number

    for i in range(0,9):
        for j in range(0, 9):
            data[0][i*9+j] = soduko[i][j]

    sudoku = Sudoku(data[0])
    sudoku.sudo_solve()
    t2 = time.time()

    print(sudoku.value)
    print(u"耗时：%.3fs" % (t2 - t1))

    cv2.imwrite("temp.jpg",bkIMG)
    return bkIMG,soduko,sudoku
