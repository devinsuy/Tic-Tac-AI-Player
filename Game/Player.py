#----------
# Devin Suy
#----------

class Player:
    def __init__(self, is_bot=False):
        self.is_bot = is_bot
        if is_bot:
            self.symbol = "O"
            self.name = "Computer"
        else:
            self.symbol = "X"
            self.name = "Human"
        self.placements = set([])       # Set of cell numbers the player has made a move into
    
    def add_placement(self, cell_num):
        self.placements.add(cell_num)
    
    def remove_placement(self, cell_num):
        self.placements.remove(cell_num)
    
    def reset_player(self):
        self.placements.clear()
