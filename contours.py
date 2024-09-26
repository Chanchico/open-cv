import cv2 as cv
import numpy as np

if __name__ == "__main__":
    img = cv.imread("Photos/cats.jpg")

    cv.imshow("Cats", img)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow("Gray", gray)

    blank = np.zeros(img.shape, dtype="uint8")
    cv.imshow("Blank", blank)

    # blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
    # cv.imshow("Blur",blur)

    # canny = cv.Canny(blur, 125, 175)
    # canny1 = cv.Canny(img, 300, 175)
    # canny2 = cv.Canny(img, 125, 300)
    # canny3 = cv.Canny(img, 300, 300)
    # cv.imshow('Canny Edges', canny)
    # cv.imshow('Canny Edges 300, 175', canny1)
    # cv.imshow('Canny Edges 125, 300', canny2)
    # cv.imshow('Canny Edges 300, 300', canny3)

    ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
    cv.imshow('Threshold', thresh)
    contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

    print(len(contours))
    cv.drawContours(blank, contours, -1, (0,0,255), 1)
    cv.imshow("Contours Drawn", blank)

    cv.waitKey(0)

