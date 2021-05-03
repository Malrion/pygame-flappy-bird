# Flappy Bird (На PyGame) v1.0
# Powered by MRemushev

import pygame
from random import randint

green = (35,235,60)
blue = (80,200,250)
black = (0,0,0)
grey = (10,105,15)
grey2 = (25,165,35)
grey3 = (250,250,250)
green2 = (160,255,165)
green3 = (85,255,100)
yellow = (255,225,0)
white = (255,255,255)
orange = (255,165,0)
brown = (145,70,0)

pygame.init()

size = 700, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Flappy Bird")

run = True
notJump = False
clock = pygame.time.Clock()

def obstacle(xloc, xsize, yloc, ysize):
    pygame.draw.rect(screen, green, [xloc, yloc, xsize, ysize])
    pygame.draw.rect(screen, green, [xloc, yloc+ysize+space, xsize, ysize+500])
    pygame.draw.rect(screen, black, [xloc+63, yloc, 7, ysize])
    pygame.draw.rect(screen, grey, [xloc+56, yloc, 7, ysize])
    pygame.draw.rect(screen, grey2, [xloc+49, yloc, 7, ysize])
    pygame.draw.rect(screen, green2, [xloc, yloc, 7, ysize])
    pygame.draw.rect(screen, green3, [xloc+7, yloc, 7, ysize])

    pygame.draw.rect(screen, black, [xloc+63, yloc+ysize+space, 7, ysize+500])
    pygame.draw.rect(screen, grey, [xloc+56, yloc+ysize+space, 7, ysize+500])
    pygame.draw.rect(screen, grey2, [xloc+49, yloc+ysize+space, 7, ysize+500])
    pygame.draw.rect(screen, green2, [xloc, yloc+ysize+space, 7, ysize+500])
    pygame.draw.rect(screen, green3, [xloc+7, yloc+ysize+space, 7, ysize+500])


def ball(x, y):
    pygame.draw.circle(screen, yellow, [x, int(y)], 20)
    pygame.draw.circle(screen, white, [int(x+12), int(y-12)], 10)
    pygame.draw.polygon(screen, orange, [(x+12,y+5),(x+12,y-5), (x+25, y)])
    pygame.draw.circle(screen, black, [int(x+12), int(y-12)], 1)
    pygame.draw.circle(screen,black,[int(x-12), int(y+10)], 11)
    pygame.draw.circle(screen, yellow,[int(x-12), int(y+10)], 10)


def Score(score):
    font = pygame.font.Font(None ,50)
    text = font.render(("Score: "+str(score)), True, black)
    screen.blit(text, [0, 0])


def cloud(clx, cly):
    pygame.draw.circle(screen, grey3, [int(clx),int(cly)],20)
    pygame.draw.circle(screen, grey3, [int(clx+15),int(cly-10)],20)
    pygame.draw.circle(screen, grey3, [int(clx+30),int(cly)],20)
    pygame.draw.circle(screen, grey3, [int(clx+15),int(cly+10)],20)

def Ground(ground):
    pygame.draw.rect(screen, brown, [0, ground, 700, 60])

def gameover():
    screen.fill(white)
    print(pygame.font.get_fonts())
    font = pygame.font.SysFont("Calibri", 50)
    text1 = font.render("Game Over!", 2, black)
    text2 = font.render("Ваш счет: " + str(score), 2, black)
    screen.blit(text1, (200, 130))
    screen.blit(text2, (200, 250))
xloc = 700
xsize = 70
yloc = 0
ysize = randint(0, 325)
x = 350
y = 250
yspeed = 0
ground = 495
obspeed = 1
space = 150
limit = -80
score = 0
isJump = False
JumpCount = 9
dontJump = 0


while run:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = True
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                isJump = True

    if isJump == True and notJump == False:
        dontJump = 0
        if JumpCount >= 0:
            y -= JumpCount * 1.5
            JumpCount -= 1
        else:
            isJump = False
            JumpCount = 9

    elif isJump == False and notJump == False:
        y -= dontJump
        dontJump -= 0.25



    screen.fill(blue)

    cloud(45,40)
    cloud(83, 482)
    cloud(383, 39)
    cloud(524, 23)
    cloud(467, 63)
    cloud(623, 424)
    cloud(330, 260)
    cloud(600, 150)
    cloud(150, 150)
    cloud(450, 400)
    obstacle(xloc, xsize, yloc, ysize)
    ball(x, y)
    Score(score)




    if y+15 > ground:
        gameover()
        obspeed = 0
        yspeed = 0
        notJump = True

    else:
        xloc -= obspeed
        y += yspeed

    if x+15 > xloc and y-15 < ysize and x-15 < xsize+xloc:
        gameover()
        obspeed = 0
        yspeed = 0
        notJump = True

    else:
        xloc -= obspeed
        y += yspeed

    if x+20 > xloc and y+20 > ysize+space and x-15 < xsize+xloc:
        gameover()
        obspeed = 0
        yspeed = 0
        notJump = True

    else:
        xloc -= obspeed
        y += yspeed

    if xloc < limit:
        ysize = randint(0, 400)
        xloc = 700

    else:
        xloc -= obspeed
        y += yspeed

    if score >= 5:
        if x > xloc and x < xloc+8:
            score += 1
            obspeed += 0.15
    else:
        if x > xloc and x < xloc+6:
            score += 1
            obspeed += 0.15

    pygame.display.update()

    clock.tick(60)