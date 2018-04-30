import pygame
import random
import time

pygame.init()

##CONSTANTS##

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# DISPLAY
display_width = 960
display_height = 960
DISPLAYSURFACE = pygame.display.set_mode((display_width, display_height))

# CLOCK
clock = pygame.time.Clock()
FPS = 60



class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # call Sprite initializer
        self.image = pygame.image.load("images/spaceship.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.score = 0
        self.rect.x = display_width / 2
        self.rect.y = display_height - 65
        self.rect.center = (self.rect.x, self.rect.y)
        self.dx = 15
        self.dy = 15
        self.lives = 3
        self.gun = Gun()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.dx
            pygame.transform.rotate(self.image, 270)
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.dx
        if keys[pygame.K_UP]:
            self.rect.y -= self.dy
        if keys[pygame.K_DOWN]:
            self.rect.y += self.dy
        if keys[pygame.K_SPACE]:
            self.gun.shoot(58, 34) #left gun
            self.gun.shoot(91, 34) #right gun


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # call Sprite initializer
        self.image = pygame.image.load("images/enemy.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.x = display_width / 2
        self.rect.y = display_height - 100
        self.dx = 50
        self.dy = 0


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/laser.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.dx = 25 #speed on x
        self.dy = 25 #speed on y

    def update(self):
        self.rect.y -= self.dy
        if self.rect.y > display_height:
            pass

        elif self.rect.y < 0:
            pass

        if self.rect.x > display_width:
            pass

        elif self.rect.x < 0:
            pass

class Gun(pygame.sprite.Sprite):
    def __init__(self):
        self.shot_start_x = 4
        self.shot_start_y = 13

    def shoot(self, x_pos_on_sprite, y_pos_on_sprite):
        bullet = Bullet()
        bullet.rect.x = player.rect.x + x_pos_on_sprite - self.shot_start_x
        bullet.rect.y = player.rect.y + y_pos_on_sprite - self.shot_start_y
        all_sprites_list.add(bullet)
        bullet_list.add(bullet)


class Wall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


BackGround = Background('images/spacepic.png', [0,0])
player = Player()

#SPRITE LISTS

# contains all sprites except background
all_sprites_list = pygame.sprite.Group()

#contains all enemies
enemy_list = pygame.sprite.Group()

#contains all bullets
bullet_list = pygame.sprite.Group()

enemies_hit_list = pygame.sprite.Group()
#contains all enemies that have been hit by a bullet(/player?)

all_sprites_list.add(player)


def main():
    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        all_sprites_list.update()
        DISPLAYSURFACE.fill(WHITE)
        DISPLAYSURFACE.blit(BackGround.image, BackGround.rect)
        all_sprites_list.draw(DISPLAYSURFACE)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()