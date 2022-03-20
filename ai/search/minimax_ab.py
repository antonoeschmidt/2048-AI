import numpy as np
class MinimaxAB():
    def __init__(self, max_depth = None):
        self.max_depth = max_depth
    
    ## Method to start minimax search using DFS
    def __call__(self, game, state):
        value,move = self.max_val(game, state, 0, -np.inf, np.inf)
        return move

    ## Acts as player
    def max_val(self,game, state, depth, a, b):
        
        ## Checks if game is over, or if depth restriction in DFS is met
        if game.is_terminal(state) or depth > self.max_depth:
            return game.utility(state), 'w'

        v = a
        actions = game.actions(state)
        
        ## Generates states for each possible action in current state
        for action in actions:
            new_state = game.result(state,action)
            v2,a2 = self.min_val(game, new_state, depth, a, b)

            ## Checks if action results in a better outcome
            if v2 > v:
                v,move = v2,action
                a = max(a,v)
            if v >= a:
                break
        
        return v, move

    ## Acts as opponent (the game)
    def min_val(self, game, state, depth, a, b):

        ## Checks if game is over
        if game.is_terminal(state):
           return game.utility(state), 'w'

        v, move = b, 'w'
        states, _ = game.chance(state)  

        #print(state.fill_rate(state))

        fill_value = state.fill_rate(state)    

        ## Generates states for each possible action in current state
        for index, new_state in enumerate(states):


            # if index > depth + 1:
            #     break

            # if fill_value < 0.45:
            #     # print(fill_value)
            #     if index > depth + 1:
            #         break
            
            v2, a2 = self.max_val(game,new_state,depth+1, a, b)
            
            ## Checks if action results in a worse outcome
            if v2 < v:
               v, move = v2, a2
               b = min(b,v)
            
            if v <= a:
                break
        
        return v, move
