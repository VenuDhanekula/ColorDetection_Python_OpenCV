import cv2   
import numpy as np

#Capturing video through webcam
cap=cv2.VideoCapture(0)

#BGR value of the RedColor
redColor = (0,0,255)


def detection(img,colorDilate, color, colorText):
    (_,contours,hierarchy)=cv2.findContours(colorDilate,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300):
            x,y,w,h = cv2.boundingRect(contour)	
            img = cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
            cv2.putText(img,colorText ,(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, color)

def main():
    while True:
        ret, img = cap.read()
        if ret == True:
#converting frame(img i.e BGR) to HSV (hue-saturation-value)
            hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
            
#Defining the Range of Red color
            red_lower=np.array([136,87,111],np.uint8)
            red_upper=np.array([180,255,255],np.uint8)
            
#finding the range of red,blue and yellow color in the image
            red=cv2.inRange(hsv, red_lower, red_upper)
            
#Morphological transformation, Dilation  	
            kernal = np.ones((5 ,5), "uint8")
            
            red=cv2.dilate(red, kernal)
            redRes=cv2.bitwise_and(img, img, mask = red)

#Detecting the Respective Color
            detection(img, red, redColor, "Red Color" )
            
            cv2.imshow("Color Detection",img)
            cv2.imshow("Color",redRes)
            cv2.imshow("Mask On Color",red)
            if cv2.waitKey(1) & (0xFF == 27):
                cap.release()
                cv2.destroyAllWindows()
                break

if __name__ == '__main__':
    main()
