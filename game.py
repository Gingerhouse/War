class game:
    def __init__(self, max_p, time, max_r):
        self.max_p = max_p
        self.curr_p = []
        self.max_time = time
        self.curr_time = 0
        self.max_r = max_r
        self.curr_r = 0

    def add_player(self):
        pass

    def check_actions(self):
        for p in self.curr_p:
            if len(p.action) != 0:
                pass



    def end_round(self):
        if(self.curr_time == 0 or self.check_actions()):
            for p in self.curr_p:
                print(p.action)


