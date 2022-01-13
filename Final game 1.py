# This program was written by Joyce Lin on May 5.
# This is a game that is similar to tag.
# Open game and view instructions to see more details.

import pygame, os, random, time

from pygame.locals import *

os.environ['SDL_VIDEODRIVER']='windib'
pygame.init()

# set up the window
WINDOWWIDTH = 1200
WINDOWHEIGHT = 900

# the width and height of all tile blocks
BLOCKWIDTH=60
BLOCKHEIGHT=60

# the top and left corner of maze
MAZETOP=200
MAZELEFT=30

# set up the colours
BLACK = (0, 0, 0)
WHITE=(255, 255, 255)
RED=(255,0,0)

# set up the frame rate
FRAMERATE = 60

def get_image(image):
    return ".\\Resources\\Images\\" + image

def get_sound(sound):
    return ".\\Resources\Sounds\\" + sound

def get_font(font):
    return ".\\Resources\Fonts\\" + font

#set up global button click sound
CLICKSOUND = pygame.mixer.Sound(get_sound('button click.wav'))

def terminate():
    """ This function is called when the user closes the window or presses ESC """
    pygame.quit()
    os._exit(1)

def drawText(text, font, surface, x, y, textcolour):
    """ Draws the text on the surface at the location specified """
    textobj = font.render(text, 1, textcolour)
    textrect = textobj.get_rect(center=(x,y))
    surface.blit(textobj, textrect)

def game_intro(windowSurface):
    """ The game menu page that allows user
        to view instructions or start the game"""
    
    startbuttonpic1,startbuttonrect=load_image(get_image('button_start.png'))  #non-hover button pic
    startbuttonpic2=pygame.image.load(get_image('button_start2.png'))          #hover button pic
    startbuttonrect.midtop=(WINDOWWIDTH/2,330)
    
    instructbuttonpic1,instructbuttonrect=load_image(get_image('button_instructions.png')) #non-hover button pic
    instructbuttonpic2=pygame.image.load(get_image('button_instructions2.png'))            #hover button pic
    instructbuttonrect.midtop=(WINDOWWIDTH/2,420)
    
    # a list of button pics used for hover effect
    buttonpics=[[startbuttonpic1,startbuttonpic2],
             [instructbuttonpic1,instructbuttonpic2]]
    # a list of buttons to display
    buttons=[[startbuttonpic1,startbuttonrect],
             [instructbuttonpic1,instructbuttonrect]]
    
    coverpic,coverrect=load_image(get_image('cover.png'))
    
    while True:
        windowSurface.blit(coverpic,coverrect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEMOTION:
                for index in range(len(buttons)):
                    # If mouse hovers over button, button will change colour
                    if buttons[index][1].collidepoint(event.pos):
                        # Set the button's picture to the hover picture.
                        buttons[index][0] = buttonpics[index][1]
                    else:
                        # Otherwise reset the picture to original button picture.
                        buttons[index][0] = buttonpics[index][0]
            elif event.type == pygame.MOUSEBUTTONUP:
                if buttons[0][1].collidepoint(event.pos):
                    # if user clicks on the start button,
                    # the game will start
                    CLICKSOUND.play()
                    return
                elif buttons[1][1].collidepoint(event.pos):
                    # if user clicks on the instructions button,
                    # the instructions page will show up
                    CLICKSOUND.play()
                    instructions(windowSurface)

        for button in buttons:
            windowSurface.blit(button[0],button[1])
        
        pygame.display.update()

def instructions(windowSurface):
    """ The instructions page """
    drawPic(get_image('instructions page.jpg'),windowSurface,WINDOWWIDTH/2,WINDOWHEIGHT/2)
    backbuttonpic1,backbuttonrect=load_image(get_image('button_back-to-menu.png')) #non-hover button pic
    backbuttonpic2=pygame.image.load(get_image('button_back-to-menu 2.png'))       #hover button pic
    backbuttonrect.midtop=(130,30)
    buttonpics=[backbuttonpic1,backbuttonpic2]
    buttons=[backbuttonpic1,backbuttonrect]
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEMOTION:
                # If mouse hovers over button, button will change colour
                if buttons[1].collidepoint(event.pos):
                    buttons[0] = buttonpics[1]
                else:
                    buttons[0] = buttonpics[0]
            
            elif event.type == pygame.MOUSEBUTTONUP:
                if buttons[1].collidepoint(event.pos):
                    # If user clicks the back button, user will return back to menu
                    CLICKSOUND.play()
                    return
    
        windowSurface.blit(buttons[0],buttons[1])
        pygame.display.update()

def choose_character(windowSurface, name):
    """ Allows the user to choose their own chracter"""
    Font = pygame.font.Font(get_font("Arcade N.ttf"), 20)
    # a list of dictionaries containing charater profile image, spritesheet, and full body picture
    characters=[{'profile':get_image('profile1.png'),'sprite':get_image('charasprite1.png'),'body':pygame.image.load(get_image('chara1.png'))},
                {'profile':get_image('profile2.png'),'sprite':get_image('charasprite2.png'),'body':pygame.image.load(get_image('chara2.png'))},
                {'profile':get_image('profile3.jpg'),'sprite':get_image('charasprite3.png'),'body':pygame.image.load(get_image('chara3.png'))},
                {'profile':get_image('profile4.jpg'),'sprite':get_image('charasprite4.png'),'body':pygame.image.load(get_image('chara4.png'))},
                {'profile':get_image('profile5.jpg'),'sprite':get_image('charasprite5.png'),'body':pygame.image.load(get_image('chara5.png'))},
                {'profile':get_image('profile6.png'),'sprite':get_image('charasprite6.png'),'body':pygame.image.load(get_image('chara6.png'))},
                {'profile':get_image('profile7.png'),'sprite':get_image('charasprite7.png'),'body':pygame.image.load(get_image('chara7.png'))},
                {'profile':get_image('profile8.jpg'),'sprite':get_image('charasprite8.png'),'body':pygame.image.load(get_image('chara8.png'))},
                {'profile':get_image('profile9.jpg'),'sprite':get_image('charasprite9.png'),'body':pygame.image.load(get_image('chara9.png'))},
                {'profile':get_image('profile10.jpg'),'sprite':get_image('charasprite10.png'),'body':pygame.image.load(get_image('chara10.png'))},
                {'profile':get_image('profile11.jpg'),'sprite':get_image('charasprite11.png'),'body':pygame.image.load(get_image('chara11.png'))},
                {'profile':get_image('profile12.png'),'sprite':get_image('charasprite12.png'),'body':pygame.image.load(get_image('chara12.png'))}]
    background,bgrect=load_image(get_image('lab background.jpg'))
    transbg,transbgrect=load_image(get_image('translucent background.png'))
    rects=[]
    pics=[]
    body_midtop=900,100     #the location where the full body image will be displayed
    x,y=150,200             #the top left corner of where the charater sprite images are diaplayed
    colx,rowy=x,y
    transbgrect.center=x+150,y+280
    
    charaiter=iter(characters)
    # Store the character images and rects inside individual lists
    # to keep track of the display location
    for row in range(int(len(characters)/3)):
        for col in range(3):
            try:
                spritesheet,rect=load_image((next(charaiter))['sprite'])
                sprite=spritesheet.subsurface(pygame.Rect(0,0,rect.width/4,rect.height/4))
                # The sprite displayed on the display page will be bigger than actual sprite image
                enlargedsprite=pygame.transform.scale(sprite,(100,100))
                spriterect=enlargedsprite.get_rect()
                spriterect.midtop=(colx,rowy)
                pics.append(enlargedsprite)
                rects.append(spriterect)
                colx+=150
            except StopIteration:
                pass
        colx=x
        rowy+=spriterect.height*1.5

    #The default character will be the first character in characters list
    display=characters[0]['body']
    select_border,selectrect=load_image(get_image('select border.png'))
    selectrect.center=rects[0].centerx,rects[0].centery
    
    while True:
        windowSurface.blit(background,bgrect)
        windowSurface.blit(transbg,transbgrect)
        drawText(name+" CHOOSE YOUR CHARACTER", Font, windowSurface, 330, 80, WHITE)
        
        # Display the wide selection of characters
        for i in range(len(characters)):
            windowSurface.blit(pics[i],rects[i])
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEMOTION:
                for index in range(len(rects)):
                    # When mouse hovers over a charater sprite,
                    # the character's full body will appear on the right side
                    # to get an overview of the character
                    if rects[index].collidepoint(event.pos):
                        selectrect.centerx,selectrect.centery=rects[index].centerx,rects[index].centery
                        display=characters[index]['body']
                        
            elif event.type == pygame.MOUSEBUTTONUP:
                for index in range(len(rects)):
                    if rects[index].collidepoint(event.pos):
                        #The player's character will be the one chosen by the user
                        CLICKSOUND.play()
                        return characters[index]

        windowSurface.blit(select_border,selectrect)               
        windowSurface.blit(display,display.get_rect(midtop=body_midtop))                
        pygame.display.update()

def choosetagger(windowSurface):
    """ Allows the user to choose the first tagger"""
    Font = pygame.font.Font(get_font("Arcade N.ttf"), 30)
    player1text = Font.render("PLAYER 1", 1, WHITE)     #non-hover image
    subplayer1text = Font.render("PLAYER 1", 1, RED)    #hover image
    player2text = Font.render("PLAYER 2", 1, WHITE)     #non-hover image
    subplayer2text = Font.render("PLAYER 2", 1, RED)    #hover image
    textrect1 = player1text.get_rect(center=(WINDOWWIDTH/2-200,450))
    textrect2 = player2text.get_rect(center=(WINDOWWIDTH/2+200,450))

    # a list of coloured text used for hover effect
    textobj=[[player1text,subplayer1text],
             [player2text,subplayer2text]]
    # a list of displayed text
    texts=[[player1text,textrect1],
             [player2text,textrect2]]
    
    while True:
        windowSurface.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
                
            elif event.type == pygame.MOUSEMOTION:
                for index in range(len(texts)):
                    # if mouse hovers over an option,
                    # option text colour will change to hover colour
                    if texts[index][1].collidepoint(event.pos):
                        texts[index][0]=textobj[index][1]
                    else:
                        texts[index][0]=textobj[index][0]
                    
            elif event.type == pygame.MOUSEBUTTONUP:
                # Once the first tagger is chosen, game will start
                if textrect1.collidepoint(event.pos):
                    CLICKSOUND.play()
                    return True
                elif textrect2.collidepoint(event.pos):
                    CLICKSOUND.play()
                    return False
        
        drawText("WHO IS THE FIRST TAGGER?", Font, windowSurface, WINDOWWIDTH/2, 350, WHITE)
        for text in texts:
            windowSurface.blit(text[0], text[1])
        pygame.display.update()
        
def drawPic(filename,surface,x,y):
    """ Draws the picture on the surface at the location specified """
    pic,rect=load_image(filename)
    rect.center=x,y
    surface.blit(pic, rect)
    
def load_image(filename):
    """ Load an image from a file. Return the image and corresponding rectangle """
    image = pygame.image.load(filename)
    image = image.convert_alpha()   #For faster screen updating
    return image, image.get_rect()

def display_stats(windowSurface,stats,x,y,profile,left):
    """ Displays the player's statistics such as lives"""
    
    Font = pygame.font.Font(None, 30)
    heartpic,heartrect=load_image(get_image('heart.png'))
    telepic,telerect=load_image(get_image('teleporter.png'))
    profilepic,profilerect=load_image(profile)
    
    # player 1 stat will have left alignment
    # player 2 stat will have right alignment
    if left:
        profilerect.topleft=(x,y)
    else:
        profilerect.topright=(x,y)
        
    frame,framerect=load_image(get_image('profile frame.png'))
    framerect.center=profilerect.centerx,profilerect.centery

    if left:
        col=x+framerect.width
    else:
        col=x-framerect.width

    # diaplay number of lives player has
    for live in range(stats[0]):
        if left:
            heartrect.topleft=(col,y)
            col+=heartrect.width
        else:
            heartrect.topright=(col,y)
            col-=heartrect.width
        
        windowSurface.blit(heartpic,heartrect)

    if left:
        telerect.topleft=(x+framerect.width,y+heartrect.height+10)
    else:
        telerect.topleft=(x-framerect.width-telerect.width*2.2,y+heartrect.height+10)

    # display the stats such as number of teleporter available, profile pic, etc.
    windowSurface.blit(frame,framerect)
    windowSurface.blit(profilepic, profilerect)
    windowSurface.blit(telepic,telerect)
    drawText("x "+str(stats[1]),Font,windowSurface,telerect.right+20,telerect.centery,WHITE)
    
def game_over_page(windowSurface,winner):
    """ Displays the game over page with the winner's name displayed """
    windowSurface.fill(BLACK)
    Font = pygame.font.Font(get_font("Arcade N.ttf"), 50)
    menutext = ['Game Over', winner+" wins","Press space to restart"]   #a list of game over message
    height = 300
    # Display the game over message
    for i in range(len(menutext)):
        drawText(menutext[i], Font, windowSurface, WINDOWWIDTH/2, height, WHITE)
        height += 100
    pygame.display.update()

def generatecoordinate(mazelist):
    """ Generates random coordinates that is on the floor"""
    row=random.randint(0,len(mazelist)-1)
    col=random.randint(0,len(mazelist[0])-1)
    
    while mazelist[row][col]!=" ":
        row=random.randint(0,len(mazelist)-1)
        col=random.randint(0,len(mazelist[0])-1)
        
    return MAZELEFT+BLOCKWIDTH*col+BLOCKWIDTH/2, MAZETOP+BLOCKHEIGHT*row+BLOCKHEIGHT/2

def addfood(item,spritegroup,foodgroup):
    """ Adds item to spritegroup and foodgroup"""
    spritegroup.add(item)
    foodgroup.add(item)

def timetoadd(starttime,elapsedtime):
    """ Determines if it is time to add item"""
    return (time.time()-starttime>=elapsedtime)
    
def strip_from_sheet(file_name,cols,rows):
    """ Generates a list of the sprites
    that will be used for animation"""
    
    sheet,sheetrect = load_image(file_name)
    frames=[]   # a list containing sprites from spritesheet
    w=sheetrect.width/cols
    h=sheetrect.height/rows
    # spritesheet will be divided into equal size sprites
    for row in range(rows):
        for col in range(cols):
            frames.append(sheet.subsurface(pygame.Rect(w*col,h*row,w,h)))
                                                  
    return frames
    
class Player(pygame.sprite.Sprite):
    """ The player controlled by the user """
    def __init__(self,stats,name,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.frames=strip_from_sheet(stats['sprite'],4,4)   # a list of sprites used to create player animation
        self.profile=stats['profile']
        self.name=name

        self.smallestrect()     #generates the smallest rect possible for the character images
        self.image=self.frames[0]
        self.originalimage=self.image #this is needed when player is flashing after getting struck by lightning
        self.rect=pygame.Rect(self.extremeleft,self.extremetop,self.extremeright-self.extremeleft,self.extremebottom-self.extremetop)

        self.walkCount=0        #keeps track of the steps walked to create animation effect

        #Position the player at the indicated location
        self.rect.center=x,y

        #Set up default stats of player
        self.lives=3
        self.teleport=0
        self.getstriked=False
        self.immune=False
        self.tagger=False
        
        # set up movement variables
        self.moveLeft = False
        self.moveRight = False
        self.moveUp = False
        self.moveDown = False
        self.movespeed = 4

        self.hitspeeder=False   #set to true when player hits a speeder

    def smallestrect(self):
        """ Resizes frames according to the smallest possible rect to fit all frames
            which is determined by comparing the extreme points of every frame. This
            is used for a perfect collision effect"""
        leftlist=[]     # a list containing the left most point of each sprite in self.frames
        rightlist=[]    # a list containing the right most point of each sprite in self.frames
        toplist=[]      # a list containing the top most point of each sprite in self.frames
        bottomlist=[]   # a list containing the bottom most point of each sprite in self.frames
        
        for frame in self.frames:
            #the extreme points of each frame will be determined through the outline of the masks
            mask=pygame.mask.from_surface(frame)
            outlines=mask.outline()
            left=(min(outlines))[0]
            right=(max(outlines))[0]
            top= (min(outlines, key=lambda x: x[1]))[1]
            bottom=(max(outlines, key=lambda x: x[1]))[1]
            leftlist.append(left)
            rightlist.append(right)
            toplist.append(top)
            bottomlist.append(bottom)

        #the most extreme point in each list will be the right, left, top, and bottom
        #of the smallest rect possible
        self.extremetop=min(toplist)
        self.extremebottom=max(bottomlist)
        self.extremeleft=min(leftlist)
        self.extremeright=max(rightlist)
        
        for index in range(len(self.frames)):
            self.frames[index]=self.frames[index].subsurface(pygame.Rect(self.extremeleft,self.extremetop,self.extremeright-self.extremeleft,self.extremebottom-self.extremetop))      

    def colorize(self):
        """ Create a white copy of a surface
        (replaces RGB values with the given color, preserving the per-pixel alphas of original). """
        self.image1 = self.image.copy()

        # zero out RGB values
        self.image1.fill((0, 0, 0, 255), None, pygame.BLEND_RGBA_MULT)
        # add in new RGB values (white)
        self.image1.fill((255,255,255) + (0,), None, pygame.BLEND_RGBA_ADD)

    def update(self,maze):
        """ Update the stats of the player, such as position and lives """
        
        # Once walkcount reaches 20,it will be reset to zero
        # for the player image to cycle to create animation
        if self.walkCount+1>=20:
            self.walkCount=0

        #Change the position of the player's rectangle
        #and change the player's image depending on walkCount
        if self.moveDown:
            self.rect.top += self.movespeed
            self.walkCount+=1
            self.image=self.frames[self.walkCount//5]
            self.originalimage=self.image
        elif self.moveUp:
            self.rect.top -= self.movespeed
            self.walkCount+=1
            self.image=self.frames[(len(self.frames)//4)*3+self.walkCount//5]
            self.originalimage=self.image
        elif self.moveLeft:
            self.rect.left -= self.movespeed
            self.walkCount+=1
            self.image=self.frames[(len(self.frames)//4)+self.walkCount//5]
            self.originalimage=self.image
        elif self.moveRight:
            self.rect.right += self.movespeed
            self.walkCount+=1
            self.image=self.frames[(len(self.frames)//4)*2+self.walkCount//5]
            self.originalimage=self.image            
        
        wall_hit_list=pygame.sprite.spritecollide(self, maze.walls, False)
        #Player cannot move past the wall
        for wall in wall_hit_list:
            if self.moveDown:
                self.rect.bottom=wall.rect.top
            elif self.moveUp:
                self.rect.top=wall.rect.bottom
            elif self.moveRight:
                self.rect.right=wall.rect.left
            elif self.moveLeft:
                self.rect.left=wall.rect.right

        # If player gets struck by lightning,
        # player's live will decrease by one and be immune
        if self.getstriked:
            self.lives-=1
            self.movespeed-=1
            self.collidetime=time.time()
            self.immune=True
            self.getstriked=False
       
        if self.immune:
            # player be immune for 2 s after being struck
            if time.time() - self.collidetime> 2:
                self.immune=False

            # The player will flash when immune 
            if(int((time.time() - self.collidetime)*10))%2==1:
                self.colorize()
                self.image=self.image1
            else:
                self.image= self.originalimage

        # after player eats speeder and enjoys speed increase for 10s,
        # player's speed will return back to original speed
        if self.hitspeeder:
            if time.time()-self.hitspeedertime>10:
                self.movespeed-=1
                self.hitspeeder=False
            
            
    def keycontrol(self,event,leftkey,rightkey,upkey,downkey,teleportkey,mazelist):
        """ Process keyboard events to control the movement of the player"""
        if event.type == KEYDOWN:
            if event.key == leftkey:
                self.moveRight = False
                self.moveLeft = True
            elif event.key == rightkey:
                self.moveLeft = False
                self.moveRight = True
            elif event.key == upkey:
                self.moveDown = False
                self.moveUp = True
            elif event.key == downkey:
                self.moveUp = False
                self.moveDown = True
                
        elif event.type == KEYUP:
            if event.key == leftkey:
                self.moveLeft = False
            elif event.key == rightkey:
                self.moveRight = False
            elif event.key == upkey:
                self.moveUp = False
            elif event.key == downkey:
                self.moveDown = False
            elif event.key == teleportkey:
                #If player has teleporters available,
                #the player will be moved to a random location and
                #the teleporter available will decrease by 1
                if self.teleport>0:
                    self.rect.centerx,self.rect.centery=generatecoordinate(mazelist)
                    self.teleport-=1

class Hourglass(pygame.sprite.Sprite):
    """ The hourglass animation showing the elapsed time of the tagger"""
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.frames=strip_from_sheet(get_image('hourglass.png'),67,1)
        self.image=self.frames[0]
        self.rect=self.image.get_rect()
        self.rect.midtop=(x,y)
    def changeframe(self,timediff,switchtime):
        """ Changes the image of hourglass according to elapsed time of the tagger
            to create animation effect"""
        self.image=self.frames[(int(timediff//(switchtime/len(self.frames)))-1)%len(self.frames)]
        
class tile(pygame.sprite.Sprite):
    """ The tile to be used to construct the maze"""
    def __init__(self,tilepic,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect=load_image(tilepic)
        #tile will be placed at indicated location
        self.rect.topleft=(x,y)

class Speeder(pygame.sprite.Sprite):
    """ This item can increase the player's speed"""
    def __init__(self,mazelist):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(get_image("speeder.png"))
        # Set the position to a randomly generated location
        self.rect.center=generatecoordinate(mazelist)
        self.starttime=time.time()  #the time placed will be used to determine when sprite disappears
        
class Clock(pygame.sprite.Sprite):
    """ This item can increase or decrease the tagger's time
        depending on who gets it"""
    def __init__(self,mazelist):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(get_image("clock.png"))
        # Set the position to a randomly generated location
        self.rect.center=generatecoordinate(mazelist)
        self.starttime=time.time()  #the time placed will be used to determine when sprite disappears

class Teleporter(pygame.sprite.Sprite):
    """ This item allows the player to teleport"""
    def __init__(self,mazelist):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(get_image("teleporter.png"))
        # Set the position to a randomly generated location
        self.rect.center=generatecoordinate(mazelist)
        self.starttime=time.time()  #the time placed will be used to determine when sprite disappears
    
class Danger(pygame.sprite.Sprite):
    """ This cautions the user of upcoming lightning"""
    def __init__(self,mazelist):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(get_image("danger.png"))
        # Set the position to a randomly generated location
        self.rect.center=generatecoordinate(mazelist)

class Lightning(pygame.sprite.Sprite):
    """ If player gets struck by lightning,
        player's live will decrease by one"""
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.lights=strip_from_sheet(get_image('lightning.png'),2,2)
        self.rect=self.lights[0].get_rect()
        self.starttime=time.time()
        self.rect.centerx=x
        self.rect.bottom=y+10
        
class DangerZone(pygame.sprite.Sprite):
    """ A group of dangerous zones"""
    def __init__(self,mazelist):
        pygame.sprite.Sprite.__init__(self)
        self.zones=pygame.sprite.Group()
        # 10 danger spots will be randomly generated
        for x in range(10):
            self.zones.add(Danger(mazelist))
            
        self.starttime=time.time()  #time when danger zones are added
        self.countdown=5            #the amount of time danger zone will appear for

class Lightnings(pygame.sprite.Sprite):
    """ A group of lightnings """
    def __init__(self,dangerzones,dangertime):
        self.zones=pygame.sprite.Group()
        self.starttime=time.time()+dangertime-1     #when the lightnings will appear
        #lightnings will be located where the danger zones are at
        for danger in dangerzones:
            self.zones.add(Lightning(danger.rect.centerx,danger.rect.centery))

    def changeframe(self,totaltime):
        """ change the image of lightning according to starttime
            to create animation effect"""
        for lightning in self.zones:
            timediff=time.time()-self.starttime
            lightning.image=lightning.lights[(int(timediff//(totaltime/len(lightning.lights))))%len(lightning.lights)]
                
            
class Maze(pygame.sprite.Sprite):
    """ The maze and its components consisted of walls and floors"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # The map design
        # ' ' represent floor, '#' represent wall
        self.mazelist=[['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
                       ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                       ['#',' ',' ',' ',' ',' ',' ','#',' ',' ',' ',' ',' ',' ','#',' ',' ',' ','#'],
                       ['#',' ','#','#','#',' ','#','#','#','#',' ',' ','#','#','#','#','#',' ','#'],
                       ['#',' ',' ','#',' ',' ',' ','#',' ','#',' ',' ',' ',' ','#',' ',' ',' ','#'],
                       ['#',' ',' ','#',' ',' ','#',' ',' ','#',' ',' ','#','#','#','#','#',' ','#'],
                       ['#',' ',' ','#',' ',' ','#',' ',' ','#',' ',' ',' ',' ','#',' ',' ',' ','#'],
                       ['#',' ',' ','#',' ',' ','#',' ',' ','#',' ',' ',' ','#',' ','#',' ',' ','#'],
                       ['#',' ','#','#','#',' ','#',' ','#','#',' ',' ','#',' ',' ',' ','#',' ','#'],
                       ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                       ['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']]

    def construct(self):
        """ Construct the maze based on the design from self.mazelist
        using wall blocks and floor blocks"""
        row=MAZELEFT    #the row that the tiles will be placed
        col=MAZETOP     #the column that the tiles will be placed
        self.walls= pygame.sprite.Group()   #a group of walls
        self.floors= pygame.sprite.Group()  #a group of floors

        #construct the maze
        for x in range(len(self.mazelist)):
            for y in range(len(self.mazelist[0])):
                
                if self.mazelist[x][y]=='#':
                    self.walls.add(tile(get_image('block 2.png'),row,col))
                else:
                    self.floors.add(tile(get_image('floor.png'),row,col))
                row+=BLOCKWIDTH
            col+=BLOCKHEIGHT
            row=MAZELEFT
    
class Game():
    """ This class represents an instance of the game. If we need to
        reset the game we'd just need to create a new instance of this
        class. """
    def __init__(self,player1stat,player2stat,player1tagger):
        """ Constructor. Create all our attributes and initialize
        the game. """

        # Set to True when tagger tags the runner or
        # when one of the player's live is 0
        self.game_over=False

        self.switchtime=30  # The amount of time given to the tagger to tag
        self.starttagtime=time.time()   # Controls when to switch taggers

        self.all_sprites = pygame.sprite.Group() # A group of sprites to be displayed

        self.timer=Hourglass(WINDOWWIDTH/2+8,20) # The sprite of the timer
        self.all_sprites.add(self.timer)

        # Set up and construct the maze
        self.maze=Maze()    
        self.maze.construct()
        self.all_sprites.add(self.maze.walls,self.maze.floors)
        
        # Set up the players
        self.players = pygame.sprite.Group()
        self.player1=Player(player1stat,'PLAYER 1',120,530)
        self.player2=Player(player2stat,'PLAYER 2',1080,530)
        self.players.add(self.player1,self.player2)

        # first tagger will be the tagger chosen by user
        if player1tagger:
            self.player1.tagger=True
        else:
            self.player2.tagger=True

        # Set up the item groups and boolean variables
        # to control the timing of placement
        self.items=[{'type':'speeder','add':True,'min':15,'range':10},
                    {'type':'clock','add':True,'min':10,'range':20},
                    {'type':'teleporter','add':True,'min':15,'range':20}]
        self.foods=pygame.sprite.Group()
        self.speeders = pygame.sprite.Group()
        self.clocks = pygame.sprite.Group()
        self.teleporters = pygame.sprite.Group()

        # boolean variables to control timing to add danger zones
        self.indanger=False
        self.adddanger=True

        # Set up music
        pygame.mixer.music.load(get_sound('theme music.mp3'))
        self.beginning_count_down_sound=pygame.mixer.Sound(get_sound('countdown.wav'))
        self.pickUpSound = pygame.mixer.Sound(get_sound('pickup.wav'))
        self.thundersound=pygame.mixer.Sound(get_sound('biu.wav'))
        self.switchbell=pygame.mixer.Sound(get_sound('Bell.wav'))
        self.GameOverSound=pygame.mixer.Sound(get_sound('game over.wav'))
        

        # set up the music boolean varibles
        self.musicPlaying=True
        self.playoversound=True #set to false when game over sound is played
        # set up the button to control the setting such as music
        self.settingbuttons()

        # Set up the font used to display text such as the time remaining
        self.Font = pygame.font.Font(get_font("Arcade N.ttf"), 15)

        self.firsttime=True     #This variable is only true in the beginning of game for countdown
        self.startgametime=time.time()  #time when game starts
        self.beginning_count_down=4     #the time in seconds of count down

    def settingbuttons(self):
        """ The buttons on the game that is able to change the settings """
        self.playmusicbutton,self.musicrect=load_image(get_image('music button.png'))
        self.musicrect.centerx,self.musicrect.centery=1130,35
        self.mutebutton=pygame.image.load(get_image('mute button.png'))
        self.musicbutton=self.playmusicbutton   #default is playing music, so default button is playmusicbutton

    def countdown(self,windowSurface):
        """ The countdown before the game starts """
        # The countdown will only occur one time in the start of the game
        if self.firsttime:
            self.beginning_count_down_sound.play()
            num3,num3rect=load_image(get_image('3.png'))
            num2,num2rect=load_image(get_image('2.png'))
            num1,num1rect=load_image(get_image('1.png'))
            go,gorect=load_image(get_image('go.png'))
            piclist=[num3,num2,num1,go]
            rectlist=[num3rect,num2rect,num1rect,gorect]
            
            for rect in rectlist:
                rect.center=WINDOWWIDTH/2,500
                
            while time.time()-self.startgametime<=self.beginning_count_down:
                self.all_sprites.draw(windowSurface)
                for player in self.players:
                    windowSurface.blit(player.image,player.rect)

                # Display the countdown number pictures
                if int(self.beginning_count_down-(time.time()-self.startgametime))>=3:
                    windowSurface.blit(piclist[0],rectlist[0])
                elif int(self.beginning_count_down-(time.time()-self.startgametime))==2:
                    windowSurface.blit(piclist[1],rectlist[1])
                elif int(self.beginning_count_down-(time.time()-self.startgametime))==1:
                    windowSurface.blit(piclist[2],rectlist[2])
                else:
                    windowSurface.blit(piclist[3],rectlist[3])
                    
                pygame.display.update()
                
            self.firsttime=False
            #background music will start playing when count down is finished
            pygame.mixer.music.play(-1, 0.0)
            #self.starttagtime will be when the count down is finished
            self.starttagtime+=self.beginning_count_down
        
    def process_events(self,windowSurface):
        """ Process all of the keyboard and mouse events. """
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    terminate()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    # The user presses space to restart the game when it is over
                    if self.game_over:
                        # Display the menu, choose characters and tagger,
                        # then start a new game
                        game_intro(windowSurface)
                        player1_stats=choose_character(windowSurface,"PLAYER 1")
                        player2_stats=choose_character(windowSurface,"PLAYER 2")
                        player1tagger=choosetagger(windowSurface)
                        self.__init__(player1_stats,player2_stats,player1tagger)
            elif event.type == pygame.MOUSEBUTTONUP:
                if self.musicrect.collidepoint(event.pos):
                    # if user clicks the music setting button
                    # music will either mute or play
                    if self.musicPlaying:
                        pygame.mixer.music.stop()
                        self.musicbutton=self.mutebutton
                    else:
                        pygame.mixer.music.play(-1, 0.0)
                        self.musicbutton=self.playmusicbutton
                    self.musicPlaying = not self.musicPlaying  
                

            # Player 1 and player 2 have different controls for movement and teleport.
            self.player1.keycontrol(event,ord('a'),ord('d'),ord('w'),ord('s'),ord('h'),self.maze.mazelist)
            self.player2.keycontrol(event,K_LEFT,K_RIGHT,K_UP,K_DOWN,ord('l'),self.maze.mazelist)

    def run_logic(self):
        """ This method is run each time through the frame. It
        updates player stats, positions and checks for collisions. """
        if not self.game_over:
            self.timediff=time.time()-self.starttagtime
            # Every 30s, the players will switch roles as a tagger and runner
            if int(self.timediff)>=self.switchtime:
                self.player1.tagger=not self.player1.tagger
                self.player2.tagger=not self.player2.tagger
                self.switchbell.play()
                self.starttagtime=time.time()
            if self.player1.tagger:
                self.tagger=self.player1
            else:
                self.tagger=self.player2

            # Update the player's position
            self.player1.update(self.maze)
            self.player2.update(self.maze)

            # If one player tags the other, the game ends
            if self.player1.rect.colliderect(self.player2.rect):
                self.game_over=True
            
            # Controlling the time to add items
            for item in self.items:
                if item['add']:
                    item['add']=False
                    item['start']=time.time()
                    item['new']=item['min']+random.randint(0,item['range'])
                if timetoadd(item['start'],item['new']):
                    if item['type']=='speeder':
                        addfood(Speeder(self.maze.mazelist),self.speeders,self.foods)
                    elif item['type']=='clock':
                        addfood(Clock(self.maze.mazelist),self.clocks,self.foods)
                    elif item['type']=='teleporter':
                        addfood(Teleporter(self.maze.mazelist),self.teleporters,self.foods)
                    item['add']=True
            
            for player in self.players:
                # Game will be over when player's live is 0
                if player.lives==0:
                    self.game_over=True
                    
                speeder_hit_list=pygame.sprite.spritecollide(player, self.speeders, True)
                # If player "eats" a speeder, the player's speed will increase
                if speeder_hit_list!=[]:
                    player.movespeed+=1
                    player.hitspeeder=True
                    player.hitspeedertime=time.time()

                clock_hit_list=pygame.sprite.spritecollide(player, self.clocks, True)
                # If tagger "eats" a clock, their time as tagger increases
                # If runner "eats" a clock, the tagger's time as tagger decreases
                if clock_hit_list!=[]:
                    if player.tagger:
                        self.starttagtime+=10
                        #tagger's time cannot exceed 30s
                        if time.time()-self.starttagtime<0:
                            self.starttagtime=time.time()
                    else:
                        self.starttagtime-=10

                tele_hit_list=pygame.sprite.spritecollide(player, self.teleporters, True)
                if tele_hit_list!=[]:
                    # If player "eats" a teleporter, the player gains an ability to teleport
                    player.teleport+=1

                # Play the pickup sound for each food eaten
                if speeder_hit_list!=[] or clock_hit_list!=[] or tele_hit_list!=[]:
                    self.pickUpSound.play()

            # Controlling the time to add danger
            if self.adddanger==True:
                self.startdangertime=time.time()
                self.adddanger=False
                self.newzone=5+random.randint(0,10)
            if timetoadd(self.startdangertime,self.newzone):
                self.dangerzone=DangerZone(self.maze.mazelist)
                self.adddanger=True
                self.indanger=True
                
            # Once dangerzones are added,
            # lightning will be generated at the same locations as the zones
            if self.adddanger:
                self.lightnings=Lightnings(self.dangerzone.zones,self.dangerzone.countdown)
                # thunder sound will play when lightning strikes
                self.thundersound.play()

            if self.indanger:
                # If player is in the danger zone during the last second of the danger zones,
                # the player will get striked by lightning
                if int(time.time()-self.dangerzone.starttime)==self.dangerzone.countdown-1:
                    for player in self.players:
                        ondangerlist = pygame.sprite.spritecollide(player, self.dangerzone.zones, False)
                        for hit in ondangerlist:
                            if not player.immune:
                                player.getstriked=True

            for food in self.foods:
                # After the foods appear for 5s, it will disappear
                if int(time.time()-food.starttime)>=5:
                    food.kill()
        else:
            # When the game is over, the gameover sound will be played once
            pygame.mixer.music.stop()
            if self.playoversound==True:
                self.GameOverSound.play()
                self.playoversound=False
                
                
    def display_frame(self, windowSurface):
        """ Display everything to the screen for the game. """
        
        # draw the black background onto the surface
        windowSurface.fill(BLACK)
        if self.game_over:
            # If game is over, the game over page will display the winner's name
            # The winner is determined through the different winning cases below
            if self.player1.lives==0 and self.player2.lives==0:
                game_over_page(windowSurface,"No One")
            elif self.player1.lives>0 and self.player2.lives>0:
                game_over_page(windowSurface,self.tagger.name)
            else:
                if self.player1.lives==0:
                    game_over_page(windowSurface,self.player2.name)
                else:
                    game_over_page(windowSurface,self.player1.name)
        else:
            # The image of the timer will change according to
            # the time remaining for the tagger to create an animation effect
            self.timer.changeframe(self.timediff,self.switchtime)
 
            windowSurface.blit(self.musicbutton,self.musicrect)

            # draw the most of the sprites onto the surface
            self.all_sprites.draw(windowSurface)

            if self.indanger:
                # danger zones will be displayed when it is indanger
                if int(time.time()-self.dangerzone.starttime)<self.dangerzone.countdown:
                    self.dangerzone.zones.draw(windowSurface)
                else:
                    self.indanger=False

            # After the food appears for 3.5s, it will start flashing
            # to signify that it is going to disappear
            for food in self.foods:
                if time.time()-food.starttime<=3.5:
                    windowSurface.blit(food.image,food.rect)
                elif (int((time.time()-food.starttime)*10))%2==0:
                    windowSurface.blit(food.image,food.rect)

            # Display the players
            for player in self.players:
                windowSurface.blit(player.image,player.rect)
                
            if self.indanger:
                # lightning will strike during the last second of dangerzone
                if int(time.time()-self.dangerzone.starttime)==self.dangerzone.countdown-1:
                    #lightning image will change according to time to create animation
                    self.lightnings.changeframe(1)
                    self.lightnings.zones.draw(windowSurface)
                    
            #Display the time remaining for tagger
            drawText("TIME REMAINING: "+str(int(self.switchtime-self.timediff)+1), self.Font, windowSurface, WINDOWWIDTH/2, 140, WHITE)
            drawText('TAGGER: '+self.tagger.name, self.Font, windowSurface, WINDOWWIDTH/2, 170, WHITE)
            
            # Display the stats of the players such as number of lives, etc
            display_stats(windowSurface,[self.player1.lives,self.player1.teleport],40,90,self.player1.profile,True)
            display_stats(windowSurface,[self.player2.lives,self.player2.teleport],1160,90,self.player2.profile,False)

        # This function is called for count down in the beginning
        self.countdown(windowSurface)

        # draw the window onto the screen
        pygame.display.update()
        
            
def main():
    """ Mainline for the program """
    
    mainClock = pygame.time.Clock()
    
    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
    pygame.display.set_caption('Catch Me If You Can!')

    # Display the menu, choose the characters for player 1 and 2,
    # choose first tagger, then instantiate a game
    game_intro(windowSurface)
    player1_stats=choose_character(windowSurface,"PLAYER 1")
    player2_stats=choose_character(windowSurface,"PLAYER 2")
    player1tagger=choosetagger(windowSurface)
    game=Game(player1_stats,player2_stats,player1tagger)

    # run the game loop until the user quits
    while True:
        # Process events (keystrokes, mouse clicks, etc)
        game.process_events(windowSurface)

        # Update object positions, check for collisions, etc
        game.run_logic()

        # Draw the current frame
        game.display_frame(windowSurface)
        
        mainClock.tick(FRAMERATE)
    
main()
