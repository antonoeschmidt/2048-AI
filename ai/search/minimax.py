import numpy as np
class minimax():
    def __init__(self, max_depth = None):
        self.max_depth = max_depth

    def __call__(self, game, state):
        self.player = game.to_move()
        value,move = self.max_val(game, state)
        return move


    def max_val(self,game, state, depth):
        if game.is_terminal() or depth > self.max_depth:
            return game.utility(state, self.player)

        v, move = -np.inf
        actions = game.actions(state)
        
        for action in actions:
            new_state = game.result(state,action)
            v2,a2 = self.min_val(game, new_state, depth)

            if v2 > v:
                v,move = v2,action

        return v, move


    def min_val(self, game, state, depth):
        if game.is_terminal():
           return game.utility(state, self.player)

        v, move = np.inf
        actions = game.spawm_actions(state)

        for action in actions:
           new_state = game.result(state,action)
           v2, a2 = self.max_val(game,new_state,depth+1)

           if v2 < v:
               v,move = v2,action
        
        return v, move
