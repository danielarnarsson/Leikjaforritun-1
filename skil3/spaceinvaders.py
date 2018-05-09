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
display_width = 960
display_height = 960
DISPLAYSURFACE = pygame.display.set_mode((display_width, display_height))

# CLOCK
clock = pygame.time.Clock()
FPS = 60

# FONT
smallfont = pygame.font.SysFont("calibri", 32, bold=True)
bigfont= pygame.font.SysFont("calibri", 42, bold=True)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) # call Sprite initializer
        self.image = pygame.image.load("images/spaceship.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.score = 0
        self.rect.x = display_width / 2
        self.rect.y = display_height - 75
        self.rect.center = (self.rect.x, self.rect.y)
        self.dx = 15
        self.dy = 15
        self.lives = 3
        self.last = pygame.time.get_ticks()
        self.gun = Gun()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.dx
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.dx
        if keys[pygame.K_UP]:
            self.rect.y -= self.dy
        if keys[pygame.K_DOWN]:
            self.rect.y += self.dy
        if self.rect.x + 150 >= display_width:
            self.rect.x = display_width - 150
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y + 120 >= display_height:
            self.rect.y = display_height - 120
        if keys[pygame.K_SPACE]:
            now = pygame.time.get_ticks()
            if now - self.last >= 200:
                self.last = now
                self.gun.shoot(58, 34)  # left gun
                self.gun.shoot(91, 34)  # right gun
                if self.score > 0:
                    self.score = self.score - 10

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load("images/asteroid.png")
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = -160
        self.rect.x = random.randint(1, display_width - 160)
        self.dx = 50
        self.dy = random.randint(5,9)

    def update(self):
        self.rect.y += self.dy
        if self.rect.y >= display_height:
            self.kill()


class AsteroidSpawner:
    def __init__(self):
        self.delay = 2500
        self.time = 0

    def spawn_asteroid(self):
        new_time = pygame.time.get_ticks()
        time_delay = self.time + self.delay
        if time_delay <= new_time and self.delay > 1000:
            amount = random.randint(2,4)
            for x in range(amount):
                asteroid = Asteroid()
                asteroid_list.add(asteroid)
                all_sprites_list.add(asteroid)
            self.delay -= 35
            self.time = new_time



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
        self.dx = 25  # speed on x
        self.dy = 25  # speed on y

    def update(self):
        self.rect.y -= self.dy
        if self.rect.y + 19 < 0:
            self.kill()


class Gun(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.shot_start_x = 4
        self.shot_start_y = 13

    def shoot(self, x_pos_on_sprite, y_pos_on_sprite):
        self.bullet = Bullet()
        self.bullet.rect.x = player.rect.x + x_pos_on_sprite - self.shot_start_x
        self.bullet.rect.y = player.rect.y + y_pos_on_sprite - self.shot_start_y
        all_sprites_list.add(self.bullet)
        bullet_list.add(self.bullet)


def msg_to_screen(font, msg, color, x_pos, y_pos, fromright=False):
    text = font.render(msg, True, color)
    if not fromright:
        DISPLAYSURFACE.blit(text, (x_pos, y_pos))
    else:
        DISPLAYSURFACE.blit(text, (display_width - text.get_width() - x_pos, y_pos))


def center_msg_to_screen(font, msg, color):
    text = font.render(msg, True, color)
    DISPLAYSURFACE.blit(text, [display_width/2 - text.get_width()/2, display_height/2 - text.get_height()/2])


all_sprites_list = pygame.sprite.Group()
asteroid_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
BackGround = Background('images/spacepic.png', [0, 0])
player = Player()
asteroidspawner = AsteroidSpawner()
all_sprites_list.add(player)


def main():
    running = True
    game = True
    gamepause = False
    gamewin = False
    gameover = False
    while running:
        while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        gamepause = True
                        game = False
            if player.lives <= 0:
                gamepause=True
                game=False
            asteroidspawner.spawn_asteroid()
            collided = pygame.sprite.groupcollide(bullet_list, asteroid_list, True, True)
            if collided:
                for bullet in collided:
                    player.score += 100
            collided = pygame.sprite.spritecollide(player, asteroid_list, True)
            if collided:
                player.lives -= 1
            all_sprites_list.update()
            DISPLAYSURFACE.fill(WHITE)
            DISPLAYSURFACE.blit(BackGround.image, BackGround.rect)
            bullet_list.draw(DISPLAYSURFACE)
            player.draw(DISPLAYSURFACE)
            asteroid_list.draw(DISPLAYSURFACE)
            msg_to_screen(smallfont, "score: " + str(player.score), WHITE, 20, 20)
            msg_to_screen(smallfont, "lives: " + str(player.lives), WHITE, 20, 20, fromright=True)
            pygame.display.update()
            clock.tick(FPS)

        while gamepause:
            DISPLAYSURFACE.fill(BLACK)
            center_msg_to_screen(smallfont, "Do you want to quit the game? (y/n)", WHITE)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        running = False
                        gamepause = False
                    elif event.key == pygame.K_n or pygame.K_ESCAPE:
                        gamepause = False
                        game = True
            pygame.display.update()
            clock.tick(FPS)

        while gamewin:
            DISPLAYSURFACE.fill(BLACK)
            center_msg_to_screen(bigfont, "You win!", WHITE)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        running = False
                        gamepause = False
                    elif event.key == pygame.K_n or pygame.K_ESCAPE:
                        gamepause = False
                        game = True
            pygame.display.update()
            clock.tick(FPS)

        while gameover:
            pass
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()