import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

FILENAME = "path_5.txt"

points = []

with open(FILENAME, 'r') as f:

    for line in f.readlines():

        if line == "":
            continue

        res = ""
        print(f"line -> {line}", end="")
        for symbol in line:

            if not symbol.isalpha() and symbol not in ["(", ")"]:
                res += symbol
        print(f"res -> {res}", end="")
        coords = res.split(',')
        try:
            points.append([int(coords[0]), int(coords[1])])
        except:
            print("skipped")

map = cv.imread("map.png")

for point in points:
    map = cv.circle(map, (point[0], point[1]), 1, (45, 22, 33), -1)

cv.imshow("s", map)
cv.waitKey(0)