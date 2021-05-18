import pygame,sys,random

class Mygame():
    def main(self):
        #inital speed
        Xspeed=10
        Yspeed=10
        livesinit=5

        paddlespeed=30
        points=0
        bgcolor=0,0,0 #black
        size=width,height =500,500

        #initalizing the pygame engine
        pygame.init()
        screen=pygame.display.set_mode(size)


        #creating game objects
        paddle=pygame.image.load('bat.png')
        paddlerect=paddle.get_rect()

        ball=pygame.image.load('ball.png')
        ballrect=ball.get_rect()


        sound=pygame.mixer.Sound('interact sound.wav')
        sound.set_volume(10)

        bg=pygame.image.load('bggame1.jpg')

        #arranging the variables for game loop
        paddlerect=paddlerect.move((width/2)-(paddlerect.right/2),height-20)
        ballrect=ballrect.move(width/2,height/2)
        xspeed=Xspeed
        yspeed=Yspeed
        lives=livesinit
        clock=pygame.time.Clock()
        pygame.key.set_repeat(1,30)
        pygame.mouse.set_visible(0)

        #Game loop
        while True:
            clock.tick(40) #40 fps

            #events
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        sys.exit()
                    if event.key==pygame.K_LEFT:
                        paddlerect=paddlerect.move(-paddlespeed,0)
                        if (paddlerect.left<0):
                            paddlerect.left=0
                    if event.key==pygame.K_RIGHT:
                        paddlerect=paddlerect.move(paddlespeed,0)
                        if(paddlerect.right>width):
                            paddlerect.right=width


            #check if paddle hit ball
            if ballrect.bottom>=paddlerect.top and \
               ballrect.bottom<=paddlerect.bottom and \
               ballrect.right>=paddlerect.left and \
               ballrect.left<=paddlerect.right:

                yspeed=-yspeed
                points+=1
                sound.play(0)

                #offset
                offset= ballrect.center[0] - paddlerect.center[0]

                #offset>0 means ball hits the RHS of paddle
                #offset<0 means ball hits the LHS of paddle

                if offset>0:
                    if offset>30:
                        xspeed=7
                    elif offset>23:
                        xspeed=6
                    elif offset>17:
                        xspeed=5
                else:
                    if offset<-30:
                        xspeed=-7
                    elif offset<-23:
                        xspeed=-6
                    elif offset<-17:
                        xspeed=-5
            
            #move the ball around the screen
            ballrect=ballrect.move(xspeed,yspeed)
            if ballrect.left<0 or ballrect.right>width:
                xspeed=-xspeed
                sound.play(0)
            if ballrect.top<0:
                yspeed=-yspeed
                sound.play(0)
            
            #Check the ball has gone past bat 
            if ballrect.top>height:
                lives-=1

                #start a newball
                xspeed=Xspeed
                rand=random.random()
                if random.random()>0.5:
                    xspeed=-xspeed
                yspeed=Yspeed
                ballrect.center=width*random.random(),height/3.5
                #Lives exhausted
                if lives == 0:                    
                    msg = pygame.font.Font(None,70).render("Game Over", True, (0,255,255), bgcolor)
                    msgrect = msg.get_rect()
                    msgrect = msgrect.move(width / 2 - (msgrect.center[0]), height / 3)
                    screen.blit(msg, msgrect)
                    screen.blit(bg,(500,500))
                    pygame.display.flip()

                    #Game restart & Quit loop event.

                    while True:
                        restart = False
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                sys.exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                    	            sys.exit()
                                if not (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):                                    
                                    restart = True      
                        if restart:                   
                            screen.fill(bgcolor)
                            lives = livesinit
                            points = 0
                            break

            #Update every objects in the game
            screen.fill(bgcolor)
            screen.blit(bg,(0,0))

            scoretext = pygame.font.Font(None,40).render(str(points), True, (0,255,255), bgcolor)
            scoretextrect = scoretext.get_rect()
            scoretextrect = scoretextrect.move(width - scoretextrect.right, 0)
            screen.blit(scoretext, scoretextrect)
            screen.blit(ball, ballrect)
            screen.blit(paddle, paddlerect)
            
            pygame.display.flip()
            

if __name__ == '__main__':
    br = Mygame()
    br.main()




