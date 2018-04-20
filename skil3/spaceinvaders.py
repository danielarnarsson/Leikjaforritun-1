import pygame
import random

pygame.init()

##CONSTANTS##

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# DISPLAY
display_width = 1280
display_height = 720
DISPLAYSURFACE = pygame.display.set_mode((display_width, display_height))

# CLOCK
clock = pygame.time.Clock()
FPS = 60


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("spaceship.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.score = 0
        self.x = display_width / 2
        self.y = display_height - 75
        self.dx = 20
        self.dy = 20

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.dx
        if keys[pygame.K_RIGHT]:
            self.x += self.dx
        self.rect.center = (self.x, self.y)
        if keys[pygame.K_UP]:
            self.y -= self.dy
        if keys[pygame.K_DOWN]:
            self.y += self.dy


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("enemy.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.x = display_width / 2
        self.y = display_height - 50
        self.dx = 50
        self.dy = 0


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Missile(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("missile.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.x = player.x
        self.y = player.y
        self.dx = 25
        self.dy = 25

    def update(self):
        self.y = self.dy


BackGround = Background('spacepic.jpg', [0,0])

player = Player()

def main():
    game = True
    while game:
        pygame.event.get()
        player.update()
        DISPLAYSURFACE.fill([255, 255, 255])
        DISPLAYSURFACE.blit(BackGround.image, BackGround.rect)
        DISPLAYSURFACE.blit(player.image, player.rect)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()