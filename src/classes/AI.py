class AI:
    window = None
    pad = None

    def __init__(self, window, pad):
        self.window = window
        self.pad = pad
        pad.AI = True
    
    def makeMove(self, balls):
        if (not len(balls)):
            return None

        targetBall = max(balls, key=lambda x: x.gameObject.x)

        if ((targetBall.xSpeed <= 0) or (targetBall.gameObject.x < self.window.width / 2)):
            if ((self.pad.gameObject.y + self.pad.gameObject.height / 2) != self.window.height / 2):
                if ((self.pad.gameObject.y + self.pad.gameObject.height / 2) > self.window.height / 2):
                    self.pad.moveUp()
                else:
                    self.pad.moveDown()
        else:
            if (((targetBall.ySpeed >= 0) and (self.pad.gameObject.y > targetBall.gameObject.y)) and (self.pad.gameObject.y > 0)):
                self.pad.moveUp()
            elif (((targetBall.ySpeed >= 0) and (self.pad.gameObject.y < targetBall.gameObject.y)) and (self.pad.gameObject.y < (self.window.height - self.pad.gameObject.height))):
                self.pad.moveDown()
            elif (((targetBall.ySpeed < 0) and (self.pad.gameObject.y > targetBall.gameObject.y)) and (self.pad.gameObject.y > 0)):
                self.pad.moveUp()
            elif (((targetBall.ySpeed < 0) and (self.pad.gameObject.y < targetBall.gameObject.y)) and (self.pad.gameObject.y < (self.window.height - self.pad.gameObject.height))):
                self.pad.moveDown()