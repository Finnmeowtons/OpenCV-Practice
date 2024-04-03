import cv2 as cv

cat_img = cv.imread('Photos/cat_large.jpg')


def rescale_frame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


cv.imshow('Cat', rescale_frame(cat_img, .2))
dog_vid = cv.VideoCapture('Videos/dog.mp4')


def change_res(width, height):
    # For Live Video
    dog_vid.set(3, width)
    dog_vid.set(4, height)


while True:
    isTrue, frame = dog_vid.read()

    frame_resized = rescale_frame(frame, scale=.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

dog_vid.release()
cv.destroyAllWindows()
