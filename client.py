import pygame
from player import Player
from network import Network

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Client')

clientNumber = 0

def read_pos(str):
    pass

def make_pos(tup):
    pass

def read_request(str):
    str = str.split
    pass

def make_request(tup):
    pass

def redrawWindow():
    win.fill((255, 255, 255))
    pygame.display.update()

def main():
    run = True

    n = Network()
    startPos = read_pos(n.getPos())
    p = Player('Player1', 'A', startPos)
    p2 = Player('Player2', 'B', 1)
    p3 = Player('Player3', 'C', 2)

    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        p2Pos = read_pos(n.send(make_pos((p.pos))))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

