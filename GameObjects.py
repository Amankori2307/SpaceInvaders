import pyglet
import random
from random import randint
def preload_image(image):
    img = pyglet.image.load(image)
    return img
class GameObject:
    def __init__(self,posx,posy,image = None):
        self.posx = posx
        self.posy = posy
        self.velx = 0
        self.vely = 0
        if image is not None:
            self.sprite = image
            self.sprite.x = self.posx
            self.sprite.y = self.posy
    def draw(self):
        self.sprite.draw()
    def update(self,dt):
        if self.sprite.x >= 0 and self.sprite.x <= 1100:
            self.sprite.x += self.velx*dt
            
        if self.sprite.x <= 0:
            self.sprite.x = 1
        if self.sprite.x >= 1100:
            self.sprite.x = 1099
            
            
        self.sprite.y += self.vely*dt
        self.posx = self.sprite.x
        self.posy = self.sprite.y
