import cv2
import time
import keyboard

cap = cv2.VideoCapture(0)
count=0
sign_name = input("Enter sign name:")
while True:
    ret, img = cap.read()
    cv2.startWindowThread()
    cv2.namedWindow("image")
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        ret, img = cap.read()
        count += 1
        print(str(count)+" "+sign_name)
        cv2.imwrite("data/"+sign_name+'.'+str(count)+'.png',img)
    
    

    
