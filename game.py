
class Game():

    def actions(self, state):
        raise NotImplementedError

    def result(self, state, move):
        raise NotImplementedError

    def utility(self, state, player):
        raise NotImplementedError

    def terminal_test(self, state):
        return not self.actions(state)
    
    def chance(self, state):
        return NotImplementedError

    def display(self, state):
        print(state)

    def start_game(self, agent):
        return NotImplementedError
 