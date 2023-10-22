import time

import pygame, sys, random


def ball_animation():
    global ball_speed_x, ball_speed_y
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 :
        ball_restart(1)
    if ball.right >= screen_width:
        ball_restart(0)
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
        ball_speed_x+=1


def player_animation():
    global ball_speed_x, ball_speed_y
    player.y += player_speed
    if player.bottom >= screen_height:
        player.bottom = screen_height
    if player.top <= 0:
        player.top = 0

def opponent_animation():
    global ball_speed_x, ball_speed_y
    if opponent.top < ball.center[1]:
        opponent.top += opponent_speed
    if opponent.bottom > ball.center[1]:
        opponent.top -= opponent_speed


def ball_restart(side):
    global ball_speed_x, ball_speed_y
    if side==1:
        screen.blit(you_won,you_won_rect)
    else:
        screen.blit(you_lose,you_lose_rect)
    pygame.display.update()
    time.sleep(3)
    ball.center = (screen_width / 2, screen_height / 2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))
    ball_speed_x=7


# General setup
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

# Setting up the main window
pygame.mixer.music.load('music/strioThingy.mpeg')
#pygame.mixer.music.set_volume(0.3)
#pygame.mixer.music.play(-1)
screen_width = 960
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PONGY PONG")
font=pygame.font.Font("Pixeltype.ttf",125)
fontsmall=pygame.font.Font("Pixeltype.ttf",75)
you_won=font.render("YOU WON",False,"Green")
you_lose=font.render("YOU LOST",False,"RED")
you_won_rect=you_won.get_rect(center=(screen_width/2,screen_height/2))
you_lose_rect=you_lose.get_rect(center=(screen_width/2,screen_height/2))
choosedifficulty=font.render("Choose difficulty:",False,"Cyan")
choosedifficulty_rect=choosedifficulty.get_rect(center=(screen_width/2,screen_height/2-150))
easy=fontsmall.render("eazy mode",True,"Orange")
hard=fontsmall.render("HARD AF",True,"Orange")
easy_rect=easy.get_rect(center=(screen_width/2,screen_height/2))
hard_rect=hard.get_rect(center=(screen_width/2,screen_height/2+125))

ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 140)

ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7

needStartingScreen=True
screen.fill((200, 100, 200))

while needStartingScreen:
    # print(pygame.mixer.music.get_volume()) # 0.9921875
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.MOUSEMOTION:
            mousePos=event.pos
            if easy_rect.collidepoint(mousePos):
                pygame.draw.ellipse(screen,"Cyan",pygame.Rect(screen_width / 2 - 150, screen_height / 2 -20, 30, 30))
            elif hard_rect.collidepoint(mousePos):
                pygame.draw.ellipse(screen,"Cyan",pygame.Rect(screen_width / 2 - 150, screen_height / 2 +105, 30, 30))
            else:
                pygame.draw.rect(screen, (200, 100, 200), pygame.Rect(screen_width / 2 - 150, screen_height / 2 - 20, 30, 30))
                pygame.draw.rect(screen, (200, 100, 200), pygame.Rect(screen_width / 2 - 150, screen_height / 2 + 105, 30, 30))
        if event.type==pygame.MOUSEBUTTONDOWN:
            if easy_rect.collidepoint(mousePos):
                needStartingScreen =False
            if hard_rect.collidepoint(mousePos):
                needStartingScreen=False
                opponent_speed=10
            #if
            #    if pygame
            #        pygame.mixer.music.set_volume(0)

    screen.blit(choosedifficulty,choosedifficulty_rect)
    screen.blit(easy,easy_rect)
    screen.blit(hard,hard_rect)

    pygame.display.update()
    clock.tick(60)

# Game loop
while True:
    # Handling inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    ball_animation()
    player_animation()
    opponent_animation()

    screen.fill("grey12")
    pygame.draw.rect(screen, (200, 200, 200), player)
    pygame.draw.rect(screen, (200, 200, 200), opponent)
    pygame.draw.ellipse(screen, (200, 200, 200), ball)
    pygame.draw.aaline(screen, (200, 200, 200), (screen_width / 2, 0), (screen_width / 2, screen_height))

    pygame.display.update()
    clock.tick(60)
