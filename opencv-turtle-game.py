import cv2
import turtle
import random
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detectionCon=0.8,maxHands=1)

video = cv2.VideoCapture(0)

score = 0
lives = 5

wn=turtle.Screen()
wn.title('falling objects')
wn.bgcolor('black')
wn.setup(width=600,height=600)
wn.tracer(0)

player=turtle.Turtle()
player.speed(0)
player.shape('square')
player.color('blue')
player.penup()
player.goto(0,-225)
player.direction ='stop'

#create list of good guys
players =[ ]
for _ in range(20):	
	player2=turtle.Turtle()
	player2.speed(0)
	player2.shape('circle')
	player2.color('green')
	player2.penup()
	player2.goto(-100,250)
	player2.speed = random.randint(2,5)
	players.append(player2)

#create list of good guys
playerss=[ ]
for _ in range(10):	
	player3=turtle.Turtle()
	player3.speed(0)
	player3.shape('circle')
	player3.color('red')
	player3.penup()
	player3.goto(100,250)
	player3.speed = random.randint(2,5)
	playerss.append(player3)

#make pen
pen=turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.goto(0,260)
font=('courier',9,'normal')
pen.write('score : {} lives:{}'.format(score,lives),align='center',font=font)


#functions
def go_left():
	player.direction = 'left'

def go_right():
	player.direction = 'right'

while True:
    ret,frame = video.read()
    hands,img = detector.findHands(frame)
    if hands:
        lmList = hands[0]
        fingersUp = detector.fingersUp(lmList)

        if fingersUp == [0,0,0,0,0]:
            go_left()
        else:
            go_right()
    text = ["Score: ",str(score)]
    text2 = ["Lives: ",str(lives)]
    cv2.putText(frame,''.join(text),(20,460),cv2.FONT_HERSHEY_COMPLEX,1, (255,255,0), 1, cv2.LINE_AA)
    cv2.putText(frame,''.join(text2),(420,460),cv2.FONT_HERSHEY_COMPLEX,1, (255,255,0), 1, cv2.LINE_AA)
    cv2.imshow("Game",frame)
    wn.update()	
    if player.direction == 'left':
        x = player.xcor()
        x-=3
        player.setx(x)
        
    if player.direction == 'right':
        x = player.xcor()
        x+=3
        player.setx(x)
            
    for player2 in players:
        y=player2.ycor()
        y-=player2.speed
        player2.sety(y)
    
        if y<-300:
            x=random.randint(-380,380)
            y = random.randint(300,400)
            player2.goto(x,y)
        
    #check collision
        if player2.distance(player)<30:
            x=random.randint(-380,380)
            y = random.randint(300,400)
            player2.goto(x,y)
            score += 20
            pen.clear()
            pen.write('score : {} lives:{}'.format(score,lives),align='center',font=font)
        
    for player3 in playerss:
        y=player3.ycor()
        y-=player3.speed
        player3.sety(y)
        if y<-300:
            x=random.randint(-380,380)
            y = random.randint(300,400)
            player3.goto(x,y)
        
    #check collision
        if player3.distance(player)<20:
            x=random.randint(-380,380)
            y = random.randint(300,400)
            player3.goto(x,y)
            score -=9
            lives -= 1
            pen.clear()
            pen.write('score : {} lives:{}'.format(score,lives),align='center',font=font)

    k = cv2.waitKey(1)
    if k== ord('q'):
        break

wn.mainloop()
video.release()
cv2.destroyAllWindows()