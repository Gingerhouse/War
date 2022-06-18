class Game:
    def __init__(self, id, max_p, time, max_r):
        self.id = id
        self.max_p = max_p
        self.curr_p = []
        self.max_time = time
        self.curr_time = 0
        self.max_r = max_r
        self.curr_r = 0
        self.actions = [None for i in range(self.max_p)]
        self.went = [False for i in range(self.max_p)]
        self.ready = False

    def addPlayer(self, player):
        self.curr_p.append(player)

    def get_player_actions(self, p):
        """
        :param p: [0,7]
        :return: Actions of Players
        """
        return self.actions[p]

    def player(self, player, action):
        self.actions[player] = action
        if player == 0:
            self.went[0] = True
        elif player == 1:
            self.went[1] = True
        elif player == 2:
            self.went[2] = True
        elif player == 3:
            self.went[3] = True
        elif player == 4:
            self.went[4] = True
        elif player == 5:
            self.went[5] = True
        elif player == 6:
            self.went[6] = True
        elif player == 7:
            self.went[7] = True

    def connected(self):
        return self.ready

    def allWent(self):
        """
        :return: Whether or not all players have gone
        """
        done = 0
        for p in self.went:
            if p == True:
                done += 1

        return done == self.curr_p

    def distribute(self):
        for p in self.actions:
            # defence
            if not p:
                #give points to other nations
                for n in range(self.curr_p - 1):
                    pass
            # attack
            else:
                for n in p:
                    # nation that defended
                    if not self.actions[n]:
                        pass
                    # nation that attacked
                    else:
                        pass

    def resetWent(self):
        self.went = [False for i in range(self.max_p)]
