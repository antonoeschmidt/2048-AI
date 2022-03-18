from ai.search.minimax import Minimax
from game import Game

class Program():
    def __init__(self, problem: Game, search):
        self.problem = problem
        self.search = search

    def __call__(self):
        return self.search(self.problem, self.problem)


    





