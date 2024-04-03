import cv2 as cv

img = cv.imread('Photos/park.jpg')
cv.imshow('Cat', img)

# Gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
cany = cv.Canny(blur, 125, 175)
cv.imshow('Canny', cany)

# Dilating the image
dilated = cv.dilate(cany, (7, 7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

# Resize
resize = cv.resize(img, (500, 500), cv.INTER_AREA)
cv.imshow('Resize', resize)
resize2 = cv.resize(img, (500, 500), cv.INTER_CUBIC)
cv.imshow('Resize2', resize2)
resize3 = cv.resize(img, (500, 500), cv.INTER_LINEAR)
cv.imshow('Resize3', resize3)

# Cropping
cropped = img[50:200, 100:300]
cv.imshow('Cropped', cropped)
cv.waitKey(0)
