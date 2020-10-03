#---------------------------------
# CECS 451 : Devin Suy : 017001983
#---------------------------------

from Algorithm.GameState import GameState

# Human player optimizes for minimal score
# Bot optimizes for maximum score
class MiniMax:
    def __init__(self, game_states):
        self.game_states = game_states
        self.initial_state = game_states[-1]                        # Last state in the list is the initial state

    # Used for scoring leaf nodes
    def score_node(self, state_node):
        t = (len(state_node.game_state.board.avail_cell_nums)+1)    # Remaining empty squares + 1
        human_went_last = not state_node.turn

        if human_went_last:
            human_won = state_node.game_state.game_over(state_node.game_state.human)
            if human_won:
                state_node.state_score = -1 * t
        else:
            bot_won = state_node.game_state.game_over(state_node.game_state.bot)
            if bot_won:
                state_node.state_score = 1 * t
        
        # Neither human nore bot have won in this board configuration
        if state_node.state_score is None:
            state_node.state_score = 0


    # Implement minimax algorithm. Human player is min, Bot is max
    # To reach a leaf node there are 8 moves that follow the initial state before
    # the game board is filled, or we reach an end game before values
    # propagate upward as we backtrack to the given state_node 
    def rank_states(self, state_node):        
        # Base case is reached
        if state_node.leaf_node:
            return state_node.state_score
        
        # It is Human's turn (X), we will minimize
        if state_node.turn:
            min_score = float('inf')

            # Recursively evaluate each "child" state
            for successor_state in state_node.successors:
                backed_score = self.rank_states(successor_state)     
                if backed_score < min_score:
                    min_score = backed_score
            
            # Assign the optimal score at this level
            state_node.state_score = min_score
            print("Assigned MIN @ depth ", state_node.depth, ": ", state_node.state_score)
            return min_score


        # It is Bot's turn (O), we will maximize
        else:
            max_score = float('-inf')

            # Recursively evaluate each "child" state
            for successor_state in state_node.successors:
                backed_score = self.rank_states(successor_state)
                if backed_score > max_score:
                    max_score = backed_score
            
            # Assign the optimal score
            state_node.state_score = max_score
            print("Assigned MAX @ depth ", state_node.depth, ": ", state_node.state_score)
            return max_score

