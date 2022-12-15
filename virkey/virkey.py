import cv2
from cvzone.HandTrackingModule import HandDetector

dis = cv2.VideoCapture(0)
dis.set(3,1280)
dis.set(4,720)

detector = HandDetector(detectionCon=0.8,maxHands=1)

while True:
    success,img = dis.read()
    hands, img = detector.findHands(img)
    #lmList, bboxInfo = hands[0],hands[1]
    cv2.rectangle(img,(100,100),(200,200),(0,255, 120),cv2.FILLED)
    cv2.putText(img, "Q",(125,175),cv2.FONT_HERSHEY_PLAIN,5,(255,255,255),5)

    cv2.imshow("Virtual KeyBoard", img)
    cv2.waitKey(1)   