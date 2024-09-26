import cv2 as cv


def rescale_frame(frame, scale=0.75):
    #Work with video
    widht = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (widht, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def change_resolution(widht, height):
    # Work with live video
    capture.set(3, widht)
    capture.set(4, height)

if __name__ == '__main__':
    # img = cv.imread("Photos/cat_large.jpg")
    # cv.imshow("Cat", img)

    capture = cv.VideoCapture('Videos/dog.mp4')

    while True:
        isTrue, frame = capture.read()

        frame_resized = rescale_frame(frame)

        cv.imshow("Video", frame)
        cv.imshow("Video Resized", frame_resized)

        if cv.waitKey(20) & 0xFF == ord("d"):
            break

    cv.waitKey(0)
    cv.destroyAllWindows()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
