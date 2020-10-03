#----------
# Devin Suy
#----------

from Game.BoardCell import BoardCell
from Game.Player import Player

class Board:
    def __init__(self):
        self.cells = []                                 # Corresponds to the cells on the game board with top left being (0) and bottom right (8)
        for cell_num in range(9):                       # Initialize all cells of the board as empty
            self.cells.append(BoardCell(cell_num))
        self.avail_cell_nums = set([0,1,2,3,4,5,6,7,8])
        self.placed_cell_nums = set([])    

    def reset_board(self):
        for cell in self.cells:
            cell.reset_cell()
        self.avail_cell_nums = set([0,1,2,3,4,5,6,7,8])
        self.placed_cell_nums = set([])    

    
    def set_cell(self, cell_num, player):
        current_cell = self.cells[cell_num]
        current_cell.set_cell(player.symbol)           # Mark the cell with either an X or O

        # Update our sets
        self.avail_cell_nums.remove(cell_num)
        self.placed_cell_nums.add(cell_num)
        player.add_placement(cell_num)
    
    def unset_cell(self, cell_num, player):
        current_cell = self.cells[cell_num]
        current_cell.set_cell()                        # Unmark the cell

        # Update our sets
        self.avail_cell_nums.add(cell_num)
        self.placed_cell_nums.remove(cell_num)
        player.remove_placement(cell_num)

    def get_cell(self, cell_num):
        return self.cells[cell_num]

    def draw_display_board(self):
        print("   Below are the different possible move placement numbers:")
        for row in range(3):
            output_line = "      |  "
            for column in range(3):
                current_cell = self.get_cell(column + (3*row))
                output_line += (str(column + 3*row) + "  |  ")          
            print(output_line) 

    def draw(self):
        print("\nDisplaying Board\n----------------\n")
        for row in range(3):
            output_line = "   |  "
            for column in range(3):
                current_cell = self.get_cell(column + (3*row))
                output_line += (current_cell.symbol + "  |  ")          
            print(output_line) 
    
    def __str__(self):
        self.draw()
        print("Avail Cells: ", self.avail_cell_nums)
        return "Placed Cells: " + str(self.placed_cell_nums)


