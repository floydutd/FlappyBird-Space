import pygame
from random import randint

## Background music##

pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(1,30.0)


##############################################
# Defining RGB colors that will be used.     #
##############################################

black=(0,0,0)
white=(255,255,255)
green=(0,255,0)
red=(255,0,0)
yellow=(255,255,0)
brown=(139,69,19)
gray=(128,128,128)
brown1=(204,102,0)
brown2=(160,82,45)
brown3=(205,133,63)

##Initializing the importe pygame modules##

pygame.init()

## Setting the Screen Size and Giving the caption name##
screen = pygame.display.set_mode((858,536),0,32)
pygame.display.set_caption("Flappy Bird Space")
screenWidth = 858

## Importing images for the background and for the bird##
bird_sprite="bird.png"
b1 = "space.jpg"
b2="space1.jpg"
b3="space2.jpg"
b4="space3.jpg"
b5="space4.jpg"
back = pygame.image.load(b1).convert()
back2 = pygame.image.load(b2).convert()
back3=pygame.image.load(b3).convert()
back4=pygame.image.load(b4).convert()
back5=pygame.image.load(b5).convert()


#background=pygame.image.load(background_sprite)

done=False

## initial setup##
clock=pygame.time.Clock()
x=350
y=250
birdx_vel=0
birdy_vel=0
boundary=515
space_x=700
space_y=0
t_width=70
t_height=randint(0,350)
space1=150
limit=200
tunnel_vel=0
score=0
b = 0

  

 ###################
#Defining Functions #
 ###################

def tunnels(space_x,space_y,t_width,t_height):
    pygame.draw.rect(screen, brown, [space_x,space_y,t_width,t_height])
    pygame.draw.rect(screen, brown, [space_x,space_y+t_height+space1,t_width,t_height+500])
    
    pygame.draw.rect(screen,black,[space_x+63,space_y,7,t_height])
    pygame.draw.rect(screen,black,[space_x+63,space_y+t_height+space1,7,t_height+500])

    pygame.draw.rect(screen,gray,[space_x+56,space_y,7,t_height])
    pygame.draw.rect(screen,gray,[space_x+56,space_y+t_height+space1,7,t_height+500])

    pygame.draw.rect(screen,brown1,[space_x+49,space_y,7,t_height])
    pygame.draw.rect(screen,brown1,[space_x+49,space_y+t_height+space1,7,t_height+500])
    
    pygame.draw.rect(screen,brown2,[space_x,space_y,7,t_height])
    pygame.draw.rect(screen,brown2,[space_x,space_y+t_height+space1,7,t_height+500])
    
    pygame.draw.rect(screen,brown3,[space_x+7,space_y,7,t_height])
    pygame.draw.rect(screen,brown3,[space_x+7,space_y+t_height+space1,7,t_height+500])

def bird(x,y):
    bird=pygame.image.load(bird_sprite)
    screen.blit(bird,(x,y))

def Score(score):
    font=pygame.font.Font(None,50)
    text=font.render(("Score: "+str(score)),True,red)
    screen.blit(text,[0,0])

def gameover():
      
    font=pygame.font.SysFont('Arial',35,italic=True, bold=True)
    text=font.render("Game Over!",True,yellow)
    screen.blit(text,[250,150])
    text=font.render("You Scored: "+str(score),True,yellow)
    screen.blit(text,[250,250])

    text=font.render("Press Enter to restart the game...", True, yellow)
    screen.blit(text,[200,350])
    
    pygame.display.flip()

def restart():
    
    gameover()
    birdy_vel=0
    tunnel_vel=0

    waitingResponse=True
    while waitingResponse:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_RETURN:
                     waitingResponse=False
                     playagain()
                     done=False
                else:
                     waitingResponse=False
                     done=True

def playagain():
    
    global x,y,b,birdx_vel,birdy_vel,space_x,space_y,t_widh,t_height,boundary,tunnel_vel,space1,score
    x=350
    y=250
    birdx_vel=0
    birdy_vel=0
    boundary=515
    space_x=700
    space_y=0
    t_width=70
    t_height=randint(0,350)
    space1=150
    limit=200
    tunnel_vel=0
    score=0
    b=0
    pygame.mixer.music.rewind()

##main loop##
while not done:
    ###Scrolling background##
    screen.blit(back, (b,0))    
    screen.blit(back2,(b+screenWidth,0))
    screen.blit(back3,(b+2*screenWidth,0))
    screen.blit(back4,(b+3*screenWidth,0))
    screen.blit(back5,(b+4*screenWidth,0))

    b= b - 1
    if b == screenWidth:
        b = 0

    msElapsed = clock.tick(100)
    ##

    ##keyboard input
       
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                birdy_vel=-3
                tunnel_vel=1
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_SPACE:
                birdy_vel=1
                  

    bird(x,y)
    tunnels(space_x,space_y,t_width,t_height)
    Score(score)

    if y+20>boundary:
        restart()

    else:
        space_x -= tunnel_vel
        y+=birdy_vel
        
    if x+20 > space_x and y-20 < t_height and x-15 < t_width+space_x:
        restart()

    else:
        space_x -= tunnel_vel
        y+=birdy_vel

    if x+20 > space_x and y+20 > t_height+space1 and x-15 < t_width+space_x:
        restart()

    else:
        space_x -= tunnel_vel
        y+=birdy_vel
    
    if space_x < limit:
        t_height = randint(0, 400)
        space_x = 700

    else:
        space_x -= tunnel_vel
        y+=birdy_vel

    if x > space_x and x < space_x+3:
        score = (score + 1)
        

    pygame.display.update()

    clock.tick(60)

pygame.quit()    
        
    
                     




