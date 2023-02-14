# Imports
from src.pplay.sprite import *
from src.pplay.window import *
from src.classes.Ball import *
from src.classes.Pad import *
from src.classes.AI import *
from src.classes.Scoreboard import *

# Game Window Initialization
gameWindow = Window(1200,800)
gameWindow.set_title("Pong")

# Keyboard Initialization
keyboard = gameWindow.get_keyboard()

# Scoreboard Initialization
scoreboard = Scoreboard(gameWindow)

# Pads Initialization
leftPad = Pad(gameWindow, keyboard, "./assets/images/pad.png", 400, "left")
rightPad = Pad(gameWindow, keyboard,"./assets/images/pad.png", 400, "right")

# AI
padAI = AI(gameWindow, rightPad)

# Ball Initialization
ball = Ball(gameWindow, "./assets/images/ball.png", 450, 20)
extraBall = Ball(gameWindow, "./assets/images/ball.png", -450, 20)
ballsArray = [ball]

# Game Loop
while (gameWindow):
    # Clean Background
    gameWindow.set_background_color((0, 0, 0))

    if (not len(ballsArray)):
        ball.rallyCount = 0
        ballsArray.append(ball)
    
    if (len(ballsArray) == 1 and ball.rallyCount == 6):
        ballsArray.append(extraBall)

    for ballInstance in ballsArray:
        # Ball X Axis Collision
        ballInstance.xAxisCollisionCheck()

        # Ball Y Axis Collision and Point Counting
        collisionResult = ballInstance.yAxisCollisionCheck(leftPad, rightPad)

        if (collisionResult):
            scoreboard.countPoint(collisionResult)
            ballsArray.remove(ballInstance)

        # Ball Movement
        ballInstance.move()

    # AI Movement
    padAI.makeMove(ballsArray)

    #Pads Movement
    leftPad.controlMove()
    rightPad.controlMove()
    
    # Draw Game Objects
    scoreboard.drawScoreboard()
    
    for ballInstance in ballsArray:
        ballInstance.gameObject.draw()

    leftPad.gameObject.draw()
    rightPad.gameObject.draw()

    # Update Window
    gameWindow.update()
