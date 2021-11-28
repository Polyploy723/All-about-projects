import pygame
pygame.int()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Game testing")
bread = pygame.image.load("icon.jpg")
pygame.display.set_bread(bread)


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit()
