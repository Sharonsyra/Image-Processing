import cv2 # import opencv

cap = cv2.VideoCapture(0) # Create a video capture object to capture the video. 
# The argument is an index to indicate the camera to use. 
# It can also be the name/path to a video file in your computer. 
# The video is captured frame by frame and at the end the capture has to be released. 
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read() # cap.read returns a boolean value. 
    # It will be true if the frame is read correctly. 
    # Sometimes, cap may not have initialized the capture. 
    # In that case, this code shows error. 
    # You can check whether it is initialized or not by the method cap.isOpened(). 
    # If it is True, OK. Otherwise open it using cap.open().
    # Our operations on the frame come here
    # You can retrieve the height and weight values and set them using cap.get() and cap.set() respectively
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Converts frame to grayscale. 
    # Converts image from one color space to another.
    color = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA) # Converst frame to BGRA color with alpha channel.
    # Display the resulting frame
    cv2.imshow('frame', gray)
    cv2.imshow('syra', color)
    if cv2.waitKey(1) & 0xFF == ord('q'): # Adjust waitkey value to fit for the video. 
    # If too low the video will be too fast and viceversa. 
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
