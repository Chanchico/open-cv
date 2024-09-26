import cv2 as cv

if __name__ == "__main__":
    img = cv.imread('Photos/cats.jpg')
    cv.imshow("Cats", img)

    # Averaging
    average = cv.blur(img, (7,7))
    cv.imshow("Average Blur", average)

    # Gaussian Blur
    gauss = cv.GaussianBlur(img, (7,7), 0)
    cv.imshow("GaussianBlur", gauss)

    # Median Blur
    median = cv.medianBlur(img,7)
    cv.imshow("Median", median)

    # Bilateral
    bilateral = cv.bilateralFilter(img, 5, 15, 15)
    cv.imshow("bilateral", bilateral)
    

    cv.waitKey(0)