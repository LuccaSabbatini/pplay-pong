from src.pplay.sprite import *

class Pad:
    window = None
    keyboard = None
    gameObject = None
    absoluteSpeed = None
    xSpeed = None
    ySpeed = None
    moveUpKeybind = None
    moveDownKeybind = None
    AI = False

    def __init__(self, window, keyboard, spritePath, initialSpeed, side):
        self.window = window
        self.keyboard = keyboard
        self.gameObject = Sprite(spritePath, 1)

        if (side == "left"):
            self.gameObject.x = 0
            self.gameObject.y = (self.window.height / 2) - (self.gameObject.height / 2)

            self.moveUpKeybind = "w"
            self.moveDownKeybind = "s"
        else:
            self.gameObject.x = self.window.width - self.gameObject.width
            self.gameObject.y = (self.window.height / 2) - (self.gameObject.height / 2)

            self.moveUpKeybind = "UP"
            self.moveDownKeybind = "DOWN"

        self.absoluteSpeed = initialSpeed
        self.xSpeed = self.absoluteSpeed
        self.ySpeed = self.absoluteSpeed

    def controlMove(self):
        if (not self.AI):
            if (self.keyboard.key_pressed(self.moveUpKeybind) and self.gameObject.y > 0):
                self.moveUp()

            if (self.keyboard.key_pressed(self.moveDownKeybind) and self.gameObject.y < (self.window.height - self.gameObject.height)):
                self.moveDown()


    def moveUp(self):
        self.gameObject.y -= self.ySpeed * self.window.delta_time()
        if (self.gameObject.y < 0):
            self.gameObject.y = 0

    def moveDown(self):
        self.gameObject.y += self.ySpeed * self.window.delta_time()
        if (self.gameObject.y < 0):
            self.gameObject.y = 0