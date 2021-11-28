
import pygame, os, random, cv2


class Game():
    def __init__(self):
        self.level = 1
        self.level_complete = False
    
    def update(self, event_list):
        self.draw()

    def draw(self):
        screen.fill(Black)
        



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

#Fonts 
pygame.font.init()
#title_font = pygame.freetype.Font('fonts/Challista Script.ttf', 44)
#title_font =  pygame.font.Font('/Library/Fonts/Arial.ttf',44)
#content_font = pygame.font.Font('/Library/Fonts/Arial.ttf', 24)
#content_font = pygame.freetype.Font('fonts/Challista Script.ttf', 24)
#text

#title_text = title_font.render('Suit the suits', True, White)
#title_rect = title_text.get_rect(midtop = (gamewidth// 2, 10))

#screen = pygame.display.set_mode((gamewidth, gameheight))
#screen.blit(title_text, title_rect)
#The game Screen


screen = pygame.display.set_mode((gamewidth, gameheight))
pygame.display.set_caption('Suit the suits')
gameIcon = pygame.image.load('images/spade1.png')




#The background
Bgimage = pygame.image.load('images/Back1.png')
Bgimage = pygame.transform.scale(Bgimage, (gamewidth, gameheight))
Bgimagerect = Bgimage.get_rect()



#Create list of memory card
cardsuits = []
for item in os.listdir('images/'):
    cardsuits.append(item.split('.')[0])
cardsuitscopy = cardsuits.copy()
cardsuits.extend(cardsuitscopy)
cardsuitscopy.clear()
random.shuffle(cardsuits)

#Load each of the images into python memory
memcardsuits = []
memcardrect= []

#load music
#pygame.mixer.music.load('sounds/sexy-fashion-beats-11176.mp3')
#pygame.mixer.music.play()










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
    

