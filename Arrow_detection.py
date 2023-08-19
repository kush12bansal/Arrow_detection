import numpy as np
import cv2
 

cap = cv2.VideoCapture(0) 

while True:
    _, frame = cap.read() 
   
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 

    lower_blue = np.array([90,50,50])
    upper_blue = np.array([150,255,255])

   
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
   

    
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        approx=cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)
        area= cv2.contourArea(cnt)
        n=approx.ravel()
       
        
        if area>3000:
            cv2.drawContours(frame,[approx], -1 , (0,0,255), 3)
            i=0
            TipX=0
            TipY=0
            Sum_Coords_x=0
            Sum_Coords_y=0
            for j in n:
                if(i%2==0):
                    x=n[i]
                    y=n[i+1]

                    
                    if(i == 0):
                    
                        TipX=x
                        TipY=y
                    
                        cv2.putText(frame, "Arrow tip", (x, y),cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0)) 
                    else:
                    # to find centre of six coordinates 
                        Sum_Coords_x+=x
                        Sum_Coords_y+=y
                        
                    i+=1
            Sum_Coords_x/=6
            Sum_Coords_y/=6
            slope=(Sum_Coords_x-TipX)/(Sum_Coords_y-TipY)
            angle=np.degrees(np.arctan(slope))
            
            cv2.putText(frame,str(angle),(150,150),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255))
            
                    
    


    print(contours)
 
    cv2.imshow("Frame", frame)
    cv2.imshow('Mask', mask)
    def detect_corner():
        pass

    key = cv2.waitKey(1)
    if key == 27: 
        break

cap.release() 
cv2.destroyAllWindows() 


    


