import numpy as np
class Minimax():
    def __init__(self, max_depth = None):
        self.max_depth = max_depth
    
    ## Method to start minimax search using DFS
    def __call__(self, game, state):
        value, move = self.max_val(game, state, 0)
        return move

    ## Acts as player
    def max_val(self,game, state, depth):
        ## Checks if game is over, or if depth restriction in DFS is met
        if game.is_terminal(state) or depth > self.max_depth:
            return game.utility(state), 'w'

        v = -np.inf
        actions = game.actions(state)
        
        ## Generates states for each possible action in current state
        for action in actions:
            new_state = game.result(state,action)
            v2,a2 = self.min_val(game, new_state, depth)

            ## Checks if action results in a better outcome
            if v2 > v:
                v,move = v2,action

        return v, move

    ## Acts as opponent (the game)
    def min_val(self, game, state, depth):

        ## Checks if game is over
        if game.is_terminal(state):
           return game.utility(state), 'w'

        v = np.inf
        states, _ = game.chance(state)

        ## Generates states for each possible action in current state
        for new_state in states:
    
           v2, a2 = self.max_val(game,new_state,depth+1)
            
            ## Checks if action results in a worse outcome
           if v2 < v:
               v,move = v2, a2
        
        return v, move
