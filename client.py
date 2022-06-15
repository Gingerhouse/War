import pygame
from player import Player
from network import Network

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Client')

def redrawWindow():
    win.fill((255, 255, 255))
    pygame.display.update()


def main():
    run = True
    n = Network()
    p = n.getP()

    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2 = n.send(p)
        p3 = n.send(p)
        p4 = n.send(p)
        p5 = n.send(p)
        p6 = n.send(p)
        p7 = n.send(p)
        p8 = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        redrawWindow(win, p, p2, p3, p4, p5, p6, p7, p8)
