import pygame

pygame.init()


##CONSTANTS##

#COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255 ,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#DISPLAY
display_width = 1024
display_height = 768
DISPLAYSURFACE = pygame.display.set_mode((display_width, display_height))

#CLOCK
clock = pygame.time.Clock()
FPS = 60


class Player(pygame.sprite.Sprites):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("spaceship.jpg")
		self.image=self.image.convert()
		self.rect=self.image.get_rect()
		self.x=display_width/2
		self.y=display_height - 50
		self.dx=50
		self.dy=0

	def update(self):
		keys=pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
		    self.x-=self.dx
		if keys[pygame.K_RIGHT]:
		    self.x+=self.dx
		self.rect.center=(self.x,self.y)

class Enemy(pygame.sprite.Sprites):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("enemy.jpg")
		self.image=self.image.convert()
		self.rect=self.image.get_rect()
		self.x=display_width/2
		self.y=display_height - 50
		self.dx=50
		self.dy=0
