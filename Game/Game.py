#---------------------------------
# CECS 451 : Devin Suy : 017001983
#---------------------------------

from Game.Board import Board 
from Game.Player import Player
from Algorithm.MiniMax import MiniMax
from pathlib import Path
import pickle
import sys

class Game:
    def __init__(self):
        # Enumerate all possible 3 in a row positions
        self.win_positions = [[0,4,8], [2,4,6], [0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8]]
        self.board = Board()
        self.human = Player()
        self.bot = Player(True)        
        self.opening_move = True

    def reset_game(self):
        self.board.reset_board()
        self.human.reset_player()
        self.bot.reset_player()
        self.opening_move = True

    # Takes in a list of the symbols in each cell and 
    # sets the game to this state
    # EX: board[0] corresponds to what symbol may be in the top left cell "X" or "O" or " "
    def import_board(self, board):
        self.reset_game()
        for cell_num, symbol in enumerate(board):
            if symbol == " ":
                continue
            elif symbol == "X":
                player = self.human
            else:
                player = self.bot

            self.board.set_cell(cell_num, player)
        
        # print("Imported board")
        # self.board.draw()
        # print("Human (X): ", self.human.placements)
        # print("Bot (O): ", self.bot.placements)
        # print("Avail: ", self.board.avail_cell_nums)
        # print("Placed: ", self.board.placed_cell_nums)
        

    def board_is_full(self):
        return len(self.board.placed_cell_nums) == 9

    def get_cell(self, cell_num):
        return self.board.get_cell(cell_num)

    def game_over(self, player):
        for win_position in self.win_positions:
            # The player has placed 3 pieces in a win position
            if set(win_position).issubset(player.placements):
                return True

        return False

    # Function only called to prompt human player
    def select_move(self):
        try:
            selected_cell = int(input("\n   Human player select your move: "))
            if selected_cell < 0 or selected_cell > 8 or selected_cell in self.board.placed_cell_nums:
                raise ValueError()
        except ValueError:
            # Input validation
            while True:
                try:
                    selected_cell = int(input("   ERROR, please select a valid cell: "))
                    if selected_cell >= 0 and selected_cell < 9 and selected_cell in self.board.avail_cell_nums:
                        break
                except:
                    continue

        return selected_cell

    # Have the Human player select an available cell
    def make_move(self, player):
        selected_cell_num = self.select_move()              
        self.board.set_cell(selected_cell_num, player)
        self.board.draw()
        print("\n  ", player.name, "places an", player.symbol, "@ position", selected_cell_num)

        # Load the appropiate pre-processed states corresponding
        # to the opening move
        if self.opening_move:
            print("\nEvaluating . . .")
            load_path = Path("saved_states")
            in_file = open(load_path.joinpath("states_" + str(selected_cell_num) + ".obj"), "rb")
            self.loaded_states = pickle.load(in_file)
            self.mm = MiniMax(self.loaded_states)
            self.current_state = self.loaded_states[-1]
            self.opening_move = False
        
        # Locate the successor state that corresponds to the move
        # that the human player just made and set that to our current state
        else:
            for succesor_state in self.current_state.successors:
                if succesor_state.game_state.board.avail_cell_nums == self.board.avail_cell_nums:
                    self.current_state = succesor_state
                    break


    # Bot is always maximizer
    def bot_make_move(self):
        optimal_score = self.current_state.state_score
        optimal_state = None
        
        # Find the successor of our current state that is the optimal move
        for successor_state in self.current_state.successors:
            if successor_state.state_score == optimal_score:
                optimal_state = successor_state

                # Our most recently added cell_num between the optimal successor state and our
                # current state is the is the Set difference of the placed_cell_nums of the two
                cache_utilized = False
                selected_cell_num = (optimal_state.game_state.board.placed_cell_nums - self.current_state.game_state.board.placed_cell_nums).pop()
                if selected_cell_num in self.board.avail_cell_nums:
                    self.current_state = successor_state        # Update pointer
                    break

        
        self.board.set_cell(selected_cell_num, self.bot)
        self.board.draw()
        print("\n   Predicted State Value: ", optimal_score)
        print("   Bot places an O @ position", selected_cell_num)


    def validate_input(self, upper_bound):
        try:
            menu_selection = int(input("Enter your selection: "))           
            if menu_selection < 1 or menu_selection > upper_bound:
                raise ValueError()
        except ValueError:
            while True:
                try:
                    menu_selection = int(input("   ERROR, please select a valid option: "))
                    if menu_selection > 0 and menu_selection <= upper_bound:
                        break
                except:
                    continue

        return menu_selection 

    def play(self):
        print("Tic-Tac-Toe\n-----------")
        print("   Welcome Human! You are player X")
        self.board.draw_display_board()

        # Human player always makes opening move and is designated (X)
        human_turn = game_tied = True
         
        while not self.board_is_full():
            if human_turn:
                self.make_move(self.human)
                if self.game_over(self.human):
                    game_tied = False
                    print("\nHuman Player Has Won!!")
                    break
            else:
                self.bot_make_move()
                if self.game_over(self.bot):
                    game_tied = False
                    print("\nComputer Player Has Won!!")
                    break

            human_turn = not human_turn                     # Turn taking

        if game_tied:
            print("\nHuman and Computer have tied!!")

        # Menu system
        print("\nGame Over\n---------")
        print("   1. Play Again")
        print("   2. Exit\n")
        menu_selection = self.validate_input(2)

        if menu_selection == 1:
            print("\nStarting New Game . . .\n")
            self.reset_game()
            self.play()
        else:
            print("\nTerminating . . . Goodbye!")

            


    

