import numpy as np
class Expectimax():
    def __init__(self, max_depth = None):
        self.max_depth = max_depth
    
    ## Method to start minimax search using DFS
    def __call__(self, game, state):
        value,move = self.max_val(game, state, 0)
        return move

    ## Acts as player
    def max_val(self,game, state, depth):
        
        ## Checks if game is over, or if depth restriction in DFS is met
        if game.is_terminal() or depth > self.max_depth:
            return game.utility(state)

        v, move = -np.inf
        actions = game.actions(state)
        
        ## Generates states for each possible action in current state
        for action in actions:
            new_state = game.result(state,action)
            v2,a2 = self.chance(game, new_state, depth)

            ## Checks if action results in a better outcome
            if v2 > v:
                v,move = v2,action


    def chance(self, game, state, depth):
        if game.is_terminal() or depth > self.max_depth:
            return game.utility(state)
        
        actions, probabilities = game.chance(state)

        v = 0

        for action,prob in actions,probabilities:
            new_state = game.result(state,action)
            v+= self.max_val(game, new_state, depth+1) * prob
        return v
