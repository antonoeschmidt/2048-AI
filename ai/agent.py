class Agent():
    def __init__(self, program=None, strategy = None):
        self.program = program
        self.strategy = strategy
      

    def make_move(self):
        return self.strategy(self.program.percept)  



