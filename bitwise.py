import cv2 as cv
import numpy as np


if __name__ == '__main__':
    blank = np.zeros((400, 400), dtype="uint8")

    rectangle = cv.rectangle(blank.copy(), (30,30), (370, 370), 255, -1)
    circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

    cv.imshow("Rect", rectangle)
    cv.imshow("Cercle", circle)

    bitwise_and = cv.bitwise_and(rectangle, circle)
    cv.imshow("And", bitwise_and)

    b_or = cv.bitwise_or(rectangle, circle)
    cv.imshow("OR", b_or)

    b_xor = cv.bitwise_xor(rectangle, circle)
    cv.imshow("XOR", b_xor)

    b_not = cv.bitwise_not(rectangle)
    cv.imshow("not rect", b_not)


    cv.waitKey(0)