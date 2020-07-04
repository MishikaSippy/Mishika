import cv2
import numpy as np
img = cv2.imread("quotes.jpg")

img[0:30,:] = 0
img[:,0:30] = 0
img[450:480,:] = 0
img[:,650:680] = 0

wname = 'Drawing'
cv2.namedWindow(wname)
abc= False

def draw_eraser(event,x,y,flags,param):
    global abc
    
    if event == cv2.EVENT_LBUTTONDOWN:
        abc = True
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if (abc ==True):
            blur = img[y:y+30, x:x+30]

            blur = cv2.GaussianBlur(blur,(23, 23), 50)

            img[y:y+blur.shape[0], x:x+blur.shape[1]] = blur
    else:
        abc = False
        
cv2.setMouseCallback(wname,draw_eraser)

while True:
    cv2.imshow(wname,img)
    if cv2.waitKey(1) == ord('m'):
        break
    
cv2.destroyAllWindows()
