import serial
import pygame

# activate the pygame library .
pygame.init()
clock = pygame.time.Clock()
X = 437*2
Y = 250*2

# create the display surface object
# of specific dimension..e(X, Y).
scrn = pygame.display.set_mode((X, Y+(50*2)))
# set the pygame window name
pygame.display.set_caption('golazo')

# load and scale the images for ball and goal
gol = pygame.image.load('goal_graphic.jpg')
gol = pygame.transform.scale(gol, (X, Y))
ball = pygame.image.load('ball.png')
ball = pygame.transform.scale(ball, (50*2,50*2))
# Using blit to display the goal
scrn.blit(gol, (0, 0))

# initial ball position and speed before game loop begins
data = ''
xpos = 0
ypos = Y
speed = 0

# set up font
font = pygame.font.Font('freesansbold.ttf', 30)

# set up serial data
#dweenSerial = serial.Serial('com4', 9600) # replace with port and baudrate being used

# paint screen one time
pygame.display.flip()
status = True
while (status):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False
        # checks for right click to reset the data
        elif i.type == pygame.MOUSEBUTTONDOWN and i.button == 3:
            data = ''

    # refresh the screen with a white background
    scrn.fill((255,255,255))
    # display the goal again
    scrn.blit(gol, (0, 0))

    # read the data from the arduino serial line until we get a string
    #while (data == ''):
        #data = dweenSerial.readline().strip()
    #split_data = data.split(',')
    xpos = 200
    ypos = 250
    speed = 40

    # display the ball at its current position
    #xpos = (xpos/72)*X
    #ypos = Y - (ypos/48)*Y
    scrn.blit(ball, (xpos, ypos))
    
    # display the text
    text = font.render('Your Shot\'s speed: {} mph'.format(speed), True, (0,0,0))
    textRect = text.get_rect()
    textRect.center = (X//2, Y+25*2)
    scrn.blit(text, textRect)
    # update the screen, lock updates at 60 times/second
    pygame.display.update()
    clock.tick(60)
        
# deactivates the pygame library
pygame.quit()
