from ai.program import Program

class Agent():
    def __init__(self, program: Program):
        self.program = program
      

    def make_move(self):
        return self.program()
        # self.strategy(self.program.percept)  



