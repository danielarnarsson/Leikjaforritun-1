import pygame
import random

pygame.init()

colors = {
    'WHITE': (255,255,255),
    'BLUE': (0, 0, 255),
    'GREEN': (0,255,0),
    'RED': (255, 0, 0),
    'BLACK': (0, 0, 0)
}


clock = pygame.time.Clock()
display_width = 1024
display_height = 768
FPS = 60

font = pygame.font.SysFont("calibri", 32, bold=True)

border = {
    'LEFT': 25,
    'RIGHT': display_width - 25,
    'TOP': 0,
    'BOTTOM': display_height
}

gameDisplay = pygame.display.set_mode((display_width, display_height))

def main():

    gameover = False
    gamewin = False
    gamepause = False


    bucket_x = display_width / 2 - 50
    bucket_y = display_height - 50
    bucket_x_change = 0
    bucket_width = 100
    bucket_height = 25
    bucket_width_change = 18
    speed = 30
    balls_missed = 0
    ball_speed = 10
    score = 0
    ball_radius = 25
    rand_ball_x = random.randrange(25, display_width - 75)
    ball_y = - ball_radius
    ball_color = colors['GREEN']
    print(ball_color)

    gameDisplay.fill(colors['WHITE'])

    pygame.display.set_caption('Bucket')

    running = True
    while running:
        while gameover:
            gameDisplay.fill(colors['WHITE'])
            center_msg_to_screen("You Lost :( Do you want to play again? (y/n)", colors['RED'])
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        gameover = False
                        running = True
                        bucket_x = display_width / 2 - 50
                        bucket_y = display_height - 50
                        bucket_x_change = 0
                        bucket_width = 100
                        bucket_height = 25
                        ball_speed = 10
                        score = 0
                    elif event.key == pygame.K_n:
                        gameover = False
                        running = False
            pygame.display.update()
        
        while gamepause:
            gameDisplay.fill(colors['WHITE'])
            center_msg_to_screen("Do you want to quit the game? (y/n)", colors['BLUE'])
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y or pygame.K_ESCAPE:
                        running = False
                        gamepause = False
                    elif event.key == pygame.K_n:
                        gamepause = False
            pygame.display.update()

        while gamewin:
            gameDisplay.fill(colors['WHITE'])
            center_msg_to_screen("You Win! Do you want to play again (y/n)?", colors['GREEN'])
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        gamewin = False
                        running = True
                        bucket_x = display_width / 2 - 50
                        bucket_y = display_height - 50
                        bucket_x_change = 0
                        bucket_width = 100
                        bucket_height = 25
                        ball_speed = 10
                        score = 0
                    elif event.key == pygame.K_n:
                        gamewin = False
                        running = False
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    bucket_x_change = - speed
                if event.key == pygame.K_RIGHT:
                    bucket_x_change = speed
                if event.key == pygame.K_ESCAPE:
                    gamepause = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    bucket_x_change = 0


        if (bucket_x + bucket_x_change) < border['LEFT']:
            bucket_x = border['LEFT']
            bucket_x_change = 0

        elif (bucket_x + bucket_x_change + bucket_width) > border['RIGHT']:
            bucket_x = border['RIGHT'] - bucket_width
            bucket_x_change = 0


        if bucket_x <= (rand_ball_x + ball_radius) and (bucket_x + bucket_width) >= (rand_ball_x - ball_radius): #something wrong here?
            if bucket_y <= (ball_y + ball_radius): #something wrong here?
                score += 1
                rand_ball_x = random.randrange(50, display_width - 50)
                ball_y = - ball_radius
                bucket_width += bucket_width_change
                bucket_x += - bucket_width_change/2
                balls_missed = 0
                ball_speed += 1

        elif ball_y > display_height:
            balls_missed += 1
            rand_ball_x = random.randrange(50, display_width - 50)
            ball_y = - ball_radius
            score += -2
            if balls_missed == 3 or score < 0:
                gameover = True


        if bucket_width >= display_width - 50:
            gamewin = True

        bucket_x += bucket_x_change
        ball_y += ball_speed

        gameDisplay.fill(colors['BLACK'])
        draw_circle(ball_color, rand_ball_x, ball_y, ball_radius)
        draw_rectangle(colors['WHITE'], bucket_x, bucket_y, bucket_width, bucket_height)
        msg_to_screen("Score: " + str(score), colors['WHITE'], 5, 10)
        pygame.display.update()


        clock.tick(FPS)
    pygame.quit()
    quit()

def msg_to_screen(msg, color, x_pos, y_pos):
    text = font.render(msg, True, color)
    gameDisplay.blit(text, (x_pos, y_pos))
    # gameDisplay.blit(screen_text, [display_width/2 - screen_text.get_width()/2, display_height/2 - screen_text.get_height()/2])﻿


def center_msg_to_screen(msg, color):
    text = font.render(msg, True, color)
    gameDisplay.blit(text, [display_width/2 - text.get_width()/2, display_height/2 - text.get_height()/2])

def draw_circle(color, x_pos, y_pos, size):
    pygame.draw.circle(gameDisplay, color, (x_pos,y_pos), size)


def draw_rectangle(color, x_pos, y_pos, width, height):
    pygame.draw.rect(gameDisplay, color, [x_pos,y_pos,width,height])


def get_mouse_pos():
    pos = pygame.mouse.get_pos()
    return pos


if __name__ == '__main__':
    main()