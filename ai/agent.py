class Agent():
    def __init__(self, program=None):
        self.program = program 
      

    def make_move(self,percept):
        return self.program(percept)    


