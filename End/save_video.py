import cv2
cap = cv2.VideoCapture(0)
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480)) 
# We specify the FourCC code then the the number of frames per second(fps) and lastly pass the frame size. 
# FourCC is  4-byte code that specifies the video codec. FourCC - Compresses and decompresses digital video.
# And last one is isColor flag. 
# If it is True, encoder expect color frame, otherwise it works with grayscale frame.
while(cap.isOpened()): # Check that cap is opened using cv2.isOpened(). 
    ret, frame = cap.read()
    if ret is True:
        frame = cv2.flip(frame, 0)
        # write the flipped frame
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
