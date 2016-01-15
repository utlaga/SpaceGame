import pygame
import random

pygame.init()

myFont = pygame.font.SysFont("helvetica", 15)

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
blue =  (0,0,255)
green = (0,255,0)
red =   (255,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Spaeceshup Gaems')
clock = pygame.time.Clock()

carImg = pygame.image.load('ship.png')

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def bullet(bulposx, bulposy):
    pygame.draw.line(gameDisplay, red, [bulposx+32, bulposy+32], [bulposx+32, bulposy +52], 3 )

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0
    y_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 30
    thing_width = 3
    thing_height = 3

    thing2_startx = random.randrange(0, display_width)
    thing2_starty = -600
    thing2_speed = 15
    thing2_width = 3
    thing2_height = 3

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5

                elif event.key == pygame.K_RIGHT:
                    x_change = 5

                if event.key == pygame.K_UP:
                    y_change = -5

                elif event.key == pygame.K_DOWN:
                    y_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0


        if y >= 540:
            y = 539
        elif y <= 540:
            y += y_change
        if y <= 0:
            y = 1
        elif y >= 0:
            y += y_change

        if x >= 740:
            x = 739
        elif x <= 740:
            x += x_change
        if x <= 0:
            x = 1
        elif x >= 0:
            x += x_change


        gameDisplay.fill(black)

        things(thing_startx, thing_starty, thing_width, thing_height, white)
        thing_starty += thing_speed

        things(thing2_startx, thing2_starty, thing2_width, thing2_height, white)
        thing2_starty += thing2_speed

        car(x,y)

        bullet(x, y)


        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)

        if thing2_starty > display_height:
            thing2_starty = 0 - thing2_height
            thing2_startx = random.randrange(0,display_width)

        label = myFont.render("x = %d y = %d " %(x,y), 1, (255,255,0))
        gameDisplay.blit(label, (50, 50))

        pygame.display.update()

        clock.tick(60)



game_loop()
pygame.quit()
quit()