import pygame

class Player:
    def __init__(self, name, nation, pos):
        self.name = name
        self.nation = nation
        self.pos = pos
        self.points = 0
        self.action = []
        self.requests = []

    def make_action(self):
        pass

    def make_request(self, pos, action):
        pass

    def answer(self, pos, ans):
        pass

    def end_round(self):
        #points

        self.action = []
        self.requests = []

    def rename(self, name, nation):
        self.name = name
        self.nation = nation