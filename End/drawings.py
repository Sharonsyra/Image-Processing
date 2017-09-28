import numpy as np # Import numpy 
import cv2 # Import OpenCV

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)
# Create a blank image
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
# Pass the starting and ending coordinates of the line, color and the thickness.
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
# Pass the top-left corner and bottom-right corner of the rectangle.
cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)
# Pass the center coordinates and the radius.
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)
# To draw the ellipse, we need to pass several arguments. 
# One argument is the center location (x,y). 
# Next argument is axes lengths (major axis length, minor axis length). 
# angle is the angle of rotation of ellipse in anti-clockwise direction. 
# startAngle and endAngle denotes the starting and ending of ellipse arc 
# measured in clockwise direction from major axis. 
# i.e. giving values 0 and 360 gives the full ellipse.
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))
# To draw a polygon, first you need coordinates of vertices. 
# Make those points into an array of shape ROWSx1x2 where ROWS are number 
# of vertices and it should be of type int32.
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'PyconKE', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)
# Add text data you want to write
# Add the position coordinates, add the bottom-left corner where the data starts
# The font type of the text and Font scale - specify font size 
# regular things like color, thickness, lineType etc. For better look, lineType = cv2.LINE_AA is recommended.
cv2.imshow('image', img)
# It shows the image on the screen. 
# The first argument is for the image title and the second is for the image variable.
cv2.waitKey(0)
cv2.destroyAllWindows()
# simply destroys all the windows we created. If you want to destroy any specific window,
#  use the function cv2.destroyWindow() where you pass the exact window name as the argument.