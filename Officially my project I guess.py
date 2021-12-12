
#from _typeshed import Self
#from typing_extensions import Self
from _typeshed import Self
import pygame, os, random, cv2
from pygame import image
from pygame.display import set_allow_screensaver
from pygame.locals import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, filename, x, y):
        super().__init__()

        self.name = filename.split('.')[0]
        self.original_image = pygame.image.load('.')[0]

        self.original_image = pygame.image.load('images/A set/' + filename)

        self.back_image = pygame.image.load('images/A set/' + filename)

        pygame.draw.rect(self.back_image, White, self.back_image.get_rect())

        self.image = self.back_image

        self.rect = self.image.get_rect(topleft = (x,y))
    
        self.shown = False
    def update(self):
        self.image = self.original_image if self.shown else self.back_image

    def show(self):
        self.shown = True
    def hide(self):
        self.shown = False



 
 
class Game():
    def __init__(self):
        self.level = 1
        self.level_complete = False

        #A_set
        self.A_set = [f for f in os.listdir('images/A set') if os.path.join('images/A set', f)]

        self.img_width, self.img_height = (128, 128)
        self.padding = 20
        self.margin_top = 160
        self.cols = 4
        self.rows = 2
        self.width = 1280

        self.tiles_group = pygame.sprite.Group()

        

        # flipping & timing
        self.flipped = []
        self.frame_count = 0
        self.block_game = False

        #generate first level
        self.generate_level(self.level)

    def check_level_complete(self, event_list):
        if not self.block_game:
            for event in event_list:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for tile in self.tiles_group:
                        if tile.rect.collidepoint(event.pos):
                            self.flipped.append(tile.name)
                            tile.show()
                            if len(self.flipped) == 2:
                                if self.flipped[0] != self.flipped[1]:
                                    self.block_game = True
                                else:
                                    self.flipped = []
                                    for tile in self.tiles_group:
                                        if tile.shown:
                                            self.level_complete = True
                                        else:
                                            self.level_complete = False
                                            break

        else:
            self.frame_count += 1
            if self.frame_count == FPS:
                self.frame_count = 0
                self.block_game = False

                for tile in self.tiles_group:
                    if tile.name in self.flipped:
                        tile.hide()
                self.flipped = []    

        
    
   
   
   
   
   
   
   
   
   
   
    def draw(self):
        screen.fill(Black)





#First
#self.all_first = [f for f in os.listdir('images/first') if os.path.join('images/first',f)]
#print(self.all_first)
        



pygame.init()






#Color label
White = (255, 255, 255)
Red = (255, 0, 0)
Black = (0, 0, 0)


#Create variable
gamewidth = 1280
gameheight = 860
picsize = 128
gamecolumns = 4
gamerows = 4
padding = 10
#leftmargin = (gamewidth - ((picsize + padding) * gamecolumns)) // 2
#rightmargin = leftmargin
#topmargin = (gameheight - ((picsize + padding) * gamerows)) // 2

clock = pygame.time.Clock()
FPS = 60

game = Game()

screen = pygame.display.set_mode((gamewidth, gameheight))

#Fonts 
pygame.font.init()
title_font = pygame.freetype.Font('Challista Script.ttf', 44)
#title_font =  pygame.font.Font('/Library/Fonts/Arial.ttf',44)
#content_font = pygame.font.Font('/Library/Fonts/Arial.ttf', 24)
content_font = pygame.freetype.Font('Challista Script.ttf', 24)
#text

title_text = title_font.render('Suit the suits', True, White)
#title_rect = title_text.get_rect(center = (1280, 50))

#screen = pygame.display.set_mode((gamewidth, gameheight))
#screen.blit(title_text, title_rect)
#The game Screen


screen = pygame.display.set_mode((gamewidth, gameheight))
pygame.display.set_caption('Suit the suits')
gameIcon = pygame.image.load('first/spade1.png')




#The background
Bgimage = pygame.image.load('images/Back1.png')
Bgimage = pygame.transform.scale(Bgimage, (gamewidth, gameheight))
Bgimagerect = Bgimage.get_rect()



#Create list of memory card
cardsuits = []
for item in os.listdir('first/'):
    cardsuits.append(item.split('.')[0])
cardsuitscopy = cardsuits.copy()
cardsuits.extend(cardsuitscopy)
cardsuitscopy.clear()
random.shuffle(cardsuits)

#Load each of the images into python memory
memcardsuits = []
memcardrect= []

#for item in cardsuits:
    #picture = pygame.image.load(f'first/{item}.png')
    #picture = pygame.transform.scale(picsize, picsize)
    #memcardsuits.append(picture)
    

#load music
music = pygame.mixer.Sound('sexy-fashion-beats-11176.mp3')

music.set_volume(3)
music.play(loops = -1)











gameloop = True
while gameloop:
    #Load background
    screen.blit(Bgimage, Bgimagerect)
    
    #Events
    for event in pygame.event.get():
        if event.type == pygame.quit:
            gameloop = False
    game.update(pygame.event.get())
    
    pygame.display.update()
    clock.tick(FPS)



pygame.quit()
    

