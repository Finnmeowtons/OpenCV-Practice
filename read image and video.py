import cv2 as cv

# cat_img = cv.imread('Photos/cat_large.jpg')
# cv.imshow('Cat', cat_img)

dog_vid = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = dog_vid.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

dog_vid.release()
cv.destroyAllWindows()

