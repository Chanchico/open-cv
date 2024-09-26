import cv2 as cv
import matplotlib.pyplot as plt


if __name__ == "__main__":
    img = cv.imread("Photos/park.jpg")
    cv.imshow("Park", img)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY )
    cv.imshow("Gray", gray)

    #BGR to HSV
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    cv.imshow("hsv",  hsv )

    #BGR to L*a*b
    lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
    cv.imshow("LAB", lab)

    plt.imshow(img)
    plt.show()

    rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    cv.imshow("rgb", rgb)

    cv.waitKey(0)