import cv2 # import opencv

face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
# Get the frontal face cascade
eye_cascade = cv2.CascadeClassifier('cascades/haarcascade_eye.xml')
# Get the eye cascade
img = cv2.imread('images/syra.jpg')
# Read the image you want to detect
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Convert image from BGR to GRAY color space

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
# Find the faces on the image. If faces are found, it returns the positions of the detected
# faces as Rect(x, y, w, h). We then creae a ROI - Region of interest and apply eye detection on it. 
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2) # Get the top-left corner and bottom
    # right corner of the rectangle to plot it. 
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
cv2.imshow('img', img) # Show the final image with face and eye regions 
cv2.waitKey(0) 
cv2.destroyAllWindows()
