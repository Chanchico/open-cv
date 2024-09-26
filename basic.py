import cv2 as cv


if __name__ == '__main__':
    img = cv.imread("Photos/park.jpg")
    cv.imshow('Park', img)

    # gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # cv.imshow("Gray", gray)
    #
    blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
    # cv.imshow("Blur", blur)

    canny = cv.Canny(blur, 125, 175)
    cv.imshow("Canny", canny)

    dilated = cv.dilate(canny, (3,3), iterations=3)
    cv.imshow('Dilated', dilated)

    eroded = cv.erode(canny, (7,7), iterations=3)
    cv.imshow('Erode', eroded)


    cv.waitKey(0)