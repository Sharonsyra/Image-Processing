import cv2

img = cv2.imread('../images/cat.jpg') 
# It reads the image using the imread function and stores it in the variable, img.
# The first argument will contain the path to the image while the second contains the image color.
# The default color argument is 1/IMREAD_COLOR so if you have no second. 
# It loads a color image where any transparency on the image is nneglected 
# The other flags are IMREAD_GRAYSCALE/0 which loads images in grayscale
# and IMREAD_UNCHANGED/-1 which leaves the image unchanged. It considers the alpha channel. 
cv2.imshow('image', img)
# It shows the image on the screen. 
# The first argument is for the image title and the second is for the image variable.
k = cv2.waitKey(0)
# It waits for x milliseconds for a key press on a OpenCV window. 
# It then does the following action after the keypress
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
    # simply destroys all the windows we created. If you want to destroy any specific window, 
    # use the function cv2.destroyWindow() where you pass the exact window name as the argument.
elif k == ord('s'): 	# wait for 's' key to save and exit
    cv2.imwrite('savedimage.png', img) # It saves the image. and names it as you specify. 
    cv2.destroyAllWindows()
