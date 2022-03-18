from ai.agent import Agent
from ai.program import Program
from board import Board
from ai.search.minimax import Minimax
from ai.search.minimax_ab import MinimaxAB



# while True:
#     print("Input gamemode")
#     gamemode = int(input())

#     if gamemode == 1 or gamemode == 2:
#         break


# if gamemode == 1:
board = Board()
# minimax = Minimax(1)
minimax_ab = MinimaxAB(5)
program = Program(board, minimax_ab)
agent = Agent(program)

agent.program.problem.start_game(agent)



