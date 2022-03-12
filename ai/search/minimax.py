import numpy as np
class minimax():
    def __init__(self, max_depth = None):
        self.max_depth = max_depth

    def __call__(self, game, state):
        self.player = game.to_move()
        self.max_val(game, state)
        pass

    def max_val(self,game, state, depth):
        if game.is_terminal() or depth > self.max_depth:
            return game.utility(state, self.player)
        v = -np.inf
        children = []
        actions = game.actions(state)
        
        for action in actions:
            new_state = game.result(state,action)
            children.append(new_state)
            self.min_val(game, state, depth)

    def min_val(self, game, state, depth):
        if game.is_terminal():
           return game.utility(state, self.player)

        v = np.inf
        children = game.spawm(state)
        
        for child in children:
           self.max_val(game,child,depth+1)

