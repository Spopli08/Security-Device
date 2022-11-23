class SecurityDevice:
    #unlock code = 883371
    #lock code = 883374

    def __init__(self):
        self.Dict = {}
        self.state = 0 #this is the intial state of FSM

        for i in range(10):
            self.Dict[(0,i)] = 0
        self.Dict[(0,8)] = 1

        for i in range(10):
            self.Dict[(1, i)] = 0
        self.Dict[(1, 8)] = 2

        for i in range(10):
            self.Dict[(2, i)] = 0
        self.Dict[(2, 8)] = 2
        self.Dict[(2, 3)] = 3

        for i in range(10):
            self.Dict[(3, i)] = 0
        self.Dict[(3, 3)] = 4
        self.Dict[(3, 8)] = 1

        for i in range(10):
            self.Dict[(4, i)] = 0
        self.Dict[(4, 7)] = 5
        self.Dict[(4, 8)] = 1

        for i in range(10):
            self.Dict[(5, i)] = 0
        self.Dict[(5, 8)] = 1
        self.Dict[(5, 1)] = 6
        self.Dict[(5, 4)] = 7

        for i in range(10):
            self.Dict[(6, i)] = 0
            self.Dict[(6, 8)] = 1

        for i in range(10):
            self.Dict[(7, i)] = 0
            self.Dict[(7, 8)] = 1

    def enterval(self, val):
        try:
            val = int(val)
            if val > 9 or val < 0:
                self.state = 0
            else:
                self.state = self.Dict[(self.state, val)]
                if self.state == 6:
                    print('Unlock')
                elif self.state == 7:
                    print('Lock')
        except:
            self.state = 0