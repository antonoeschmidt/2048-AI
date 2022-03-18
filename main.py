from ai.agent import Agent
from ai.program import Program
from board import Board
from ai.search.minimax import Minimax
from ai.search.minimax_ab import MinimaxAB
from ai.search.expectimax import Expectimax



# while True:
#     print("Input gamemode")
#     gamemode = int(input())

#     if gamemode == 1 or gamemode == 2:
#         break


# if gamemode == 1:
board = Board()
# minimax = Minimax(1)
# minimax_ab = MinimaxAB(2)
expectimax = Expectimax(1)
program = Program(board, expectimax)
agent = Agent(program)

agent.program.problem.start_game(agent)



