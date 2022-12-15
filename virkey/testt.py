import cv2
from cvzone.HandTrackingModule import HandDetector
detector = HandDetector(detectionCon=0.8,maxHands=1)
cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    img= detector.findHands(img)
    lmlist,_=detector.findHands(img)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()