class Scoreboard:
    window = None
    leftScore = None
    rightScore = None

    def __init__(self, window):
        self.window = window
        self.leftScore = 0
        self.rightScore = 0

    def countPoint(self, side):
        if (side == "left"):
            self.leftScore += 1
        elif (side == "right"):
            self.rightScore += 1
    
    def drawScoreboard(self):
        self.window.draw_text(str(self.leftScore) + " x " + str(self.rightScore), (self.window.width / 2) - 20, 10, 20, (255, 255, 255), "Arial", True, False)
