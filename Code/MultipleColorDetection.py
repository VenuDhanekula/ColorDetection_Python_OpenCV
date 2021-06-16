import cv2   
import numpy as np

#Capturing video through webcam
cap=cv2.VideoCapture(0)

redColor = (0,0,255)
blueColor = (255,0,0)
yellowColor = (0,255,255)


def detection(img,colorDilate, color, colorText):
    (_,contours,hierarchy)=cv2.findContours(colorDilate,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>300):
            x,y,w,h = cv2.boundingRect(contour)	
            img = cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
            cv2.putText(img,colorText ,(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, color)
            
def colorLimit(lowerLimit, upperLimit):
    return 

def main():
    while True:
        ret, img = cap.read()
        if ret == True:
#converting frame(img i.e BGR) to HSV (hue-saturation-value)
            hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
            
#Defining the Range of Red color BGR Value
            red_lower, red_upper = np.array([136,87,111],np.uint8), np.array([180,255,255],np.uint8)
            
#Defining the Range of Blue color
            blue_lower, blue_upper = np.array([99,115,150],np.uint8), np.array([110,255,255],np.uint8)

#Defining the Range of Yellow color
            yellow_lower, yellow_upper = np.array([22,60,200],np.uint8), np.array([60,255,255],np.uint8)
            
#finding the range of red,blue and yellow color in the image
            red=cv2.inRange(hsv, red_lower, red_upper)
            blue=cv2.inRange(hsv,blue_lower,blue_upper)
            yellow=cv2.inRange(hsv,yellow_lower,yellow_upper)
            
#Morphological transformation, Dilation  	
            kernal = np.ones((5 ,5), "uint8")
            
            red=cv2.dilate(red, kernal)
            
            blue=cv2.dilate(blue,kernal)
            
            yellow=cv2.dilate(yellow,kernal) 
            
#Detecting the Respective Color
            detection(img, red, redColor, "Red Color" )
            detection(img, blue, blueColor, "Blue Color" )
            detection(img, yellow, yellowColor, "Yellow Color" )
                       
            cv2.imshow("Color Detection",img)

#Press Esc for closing the program
            if cv2.waitKey(1) & 0xFF == 27:
                cap.release()
                cv2.destroyAllWindows()
                break


if __name__ == '__main__':
    main()
          

    
