import  numpy as np
import  cv2


def processed_img(img):
    gray=cv2.cvtColor(np.array(img),cv2.COLOR_BGR2GRAY)
    resized=cv2.resize(gray,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_LINEAR)
    processed=cv2.adaptiveThreshold(resized,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,65,15)

    return processed