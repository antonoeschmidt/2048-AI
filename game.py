
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
 
    # def play_game(self, players):
    #     state = self.initial
    #     while True:
    #         for player in players:
    #             move = player.make_move(self, state)
    #             state = self.result(state, move)
    #             if self.terminal_test(state):
    #                 self.display(state)
    #                 return self.utility(state, self.to_move(self.initial))