import cv2
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detectionCon=0.8,maxHands=2)

video = cv2.VideoCapture(0)

while True:
    ret,frame = video.read()
    hands,img = detector.findHands(frame)
    #print(hands)
    if hands:
        lmList = hands[0]
        type = hands[-1]
        fingersUp = detector.fingersUp(lmList)
        print(fingersUp)
        print(lmList['type'])
        if fingersUp == [0,0,0,0,0] and type == 'left':
            print("l",fingersUp)
        elif fingersUp == [0,0,0,0,0] and type == 'right':
            print("r",fingersUp)
        else:
            print("none")
    cv2.imshow("Game",frame)
    k = cv2.waitKey(1)
    if k== ord('q'):
        break

video.release()
cv2.destroyAllWindows()