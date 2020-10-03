#----------
# Devin Suy
#----------

import copy
import sys

# Human player is min
# Bot is max
class GameState:
    num_states = -1
    game_states = []

    # turn = True : Successor states will add an X (Human)
    # turn = False : Successor states will add a O (Bot)
    def __init__(self, game_state, turn, depth, is_human=None, cell_num=None):
        self.game_state = copy.deepcopy(game_state)

        # Only called for successor constructor
        if is_human is not None:  
            # Add in the change from the parent state
            if is_human:
                player = self.game_state.human
            else:
                player = self.game_state.bot
            self.game_state.board.set_cell(cell_num, player)        
       
        self.turn = turn
        self.depth = depth
        self.successors = []  # Represent "children" states of our current state
        self.state_score = None
        self.leaf_node = False

        if self.has_successors():
            self.generate_succesors()
        else:
            # We have reached the bottom of this subtree
            self.leaf_node = True
            
        # Save states 
        GameState.num_states += 1
        GameState.game_states.append(self)
        print(GameState.num_states)


    def has_successors(self):
        if (
            len(self.game_state.board.avail_cell_nums) > 0 
            and (not self.game_state.game_over(self.game_state.human))
            and (not self.game_state.game_over(self.game_state.bot))
        ):
            return True

        return False

    def generate_succesors(self):
        # Create a successor for placement in every possible square for this turn
        for cell_num in self.game_state.board.avail_cell_nums:
            # Recursively generate successor states
            successor_state = copy.deepcopy(self.game_state)
            self.successors.append(GameState(successor_state, not self.turn, self.depth+1, self.turn, cell_num))
            
        

    
