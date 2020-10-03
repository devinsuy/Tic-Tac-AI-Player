#----------
# Devin Suy
#----------

from Game.Game import Game
from Algorithm.GameState import GameState
from Algorithm.MiniMax import MiniMax
from pathlib import Path
import pickle

# load_path = Path("saved_states")
game = Game()

# (Pre-processing) Example usage for importing an opening game state
# State 0
# game.import_board(["X", " ", " ", " ", " ", " ", " ", " ", " "])
# state_num = 0

# State 1
# game.import_board([" ", "X", " ", " ", " ", " ", " ", " ", " "])
# state_num = 1

# State 2
# game.import_board([" ", " ", "X", " ", " ", " ", " ", " ", " "])
# state_num = 2

# State 3
# game.import_board([" ", " ", " ", "X", " ", " ", " ", " ", " "])
# state_num = 3

# State 4
# game.import_board([" ", " ", " ", " ", "X", " ", " ", " ", " "])
# state_num = 4

# State 5
# game.import_board([" ", " ", " ", " ", " ", "X", " ", " ", " "])
# state_num = 5

# State 6
# game.import_board([" ", " ", " ", " ", " ", " ", "X", " ", " "])
# state_num = 6

# State 7
# game.import_board([" ", " ", " ", " ", " ", " ", " ", "X", " "])
# state_num = 7

# State 8
# game.import_board([" ", " ", " ", " ", " ", " ", " ", " ", "X"])
# state_num = 8

# gs = GameState(game, False, 0)



# Import list of pre-processed states
# in_file = open(load_path.joinpath("states_0.obj"), "rb")
# loaded_states = pickle.load(in_file)
# # for state in loaded_states:
# #     state.state_score = None
# root_node = loaded_states[-1]
# mm = MiniMax(loaded_states)

# mm = MiniMax(GameState.game_states)
# root_node = GameState.game_states[-1]


# # (Pre-processing) Score all leaf nodes
# for state_node in GameState.game_states:
#     if state_node.leaf_node:
#         mm.score_node(state_node)


# # (Pre-processing) Run minimax to assign a score to all nodes
# mm.rank_states(root_node)

# # (Pre-processing) Save states to .obj
# outfile = open(load_path.joinpath("states_" + str(state_num) + ".obj"), "wb")
# pickle.dump(GameState.game_states, outfile)


game.play()
