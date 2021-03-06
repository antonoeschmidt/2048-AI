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
        
        if self.max_depth > 1 and depth > 1:
            if game.fill_rate(state) > 3:
                depth += self.max_depth    

        ## Checks if game is over, or if depth restriction in DFS is met
        if game.is_terminal(state) or depth > self.max_depth:
            return game.utility(state), 'w'

        v, move = -np.inf, 'w'
        actions = game.actions(state)
        
        ## Generates states for each possible action in current state
        for action in actions:
            new_state = game.result(state,action)

            
            v2,a2 = self.chance(game, new_state, depth)

            ## Checks if action results in a better outcome
            if v2 > v:
                v,move = v2,action
        return v,move


    def chance(self, game, state, depth):
        if game.is_terminal(state) or depth > self.max_depth:
            return game.utility(state), 'w'
        
        states, probabilities = game.chance(state)

        v = 0

        for new_state, prob in zip(states, probabilities):
            val, _ = self.max_val(game, new_state, depth+1)
            v+= float(val) * prob
        return v, 'w'
