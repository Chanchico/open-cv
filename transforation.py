import cv2 as cv
import numpy as np


def translate(img, x, y):
    trans_mat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, trans_mat, dimensions)


def rotate(img, angle, rot_point=None):
    (height, width) = img.shape[:2]
    if rot_point is None:
        rot_point = (width // 2, height // 2)

    rot_mat = cv.getRotationMatrix2D(rot_point, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rot_mat, dimensions)


if __name__ == "__main__":
    img = cv.imread('Photos/park.jpg')
    cv.imshow("Park", img)

    translated = translate(img, 100, 100)
    cv.imshow("Translated", translated)

    rotated = rotate(img, 45)
    cv.imshow("Rotated", rotated)

    cv.waitKey(0)
