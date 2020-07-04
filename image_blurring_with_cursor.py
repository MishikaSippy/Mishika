import cv2
import numpy as np

img=cv2.imread('quotes.jpg')
wname='Mishika'
cv2.namedWindow(wname)

abc=False

def draw_eraser(event,x,y,flags,param):
    global abc
    if event==cv2.EVENT_LBUTTONDOWN:
        abc = True
        #cv2.circle(img,(x,y),30,(255,255,255),-1)
    elif event==cv2.EVENT_MOUSEMOVE:
        if abc==True:
           sub_face =img[y:y+30,x:x+30]
           sub_face =cv2.GaussianBlur(sub_face,(23,23),30)
           img[y:y+sub_face.shape[0],x:x+sub_face.shape[1]]=sub_face
        else :
            abc=False
cv2.setMouseCallback(wname,draw_eraser)

img[0:30,:]=0
img[:,0:30]=0
img[450:480,:]=0
img[:,650:680]=0



while True:
    cv2.imshow(wname,img)
    if cv2.waitKey(1)==ord('q'):
        break

cv2.destroyAllWindows()
