#----------
# Devin Suy
#----------

class BoardCell:
    def __init__(self, cell_num, status=-1, symbol=" "):
        self.cell_num = cell_num
        self.status = status        # -1 : Empty;   0 : Placed by O;   1 : Placed by X
        self.symbol = symbol
    
    def reset_cell(self):
        self.status = -1
        self.symbol = " "

    def set_cell(self, symbol=" "):
        self.symbol = symbol

        if symbol == "X":
            self.status = 1
        elif symbol == "O":
            self.status = 0
        else:
            self.status = -1

    def is_x(self):
        return self.status == 1
    
    def is_y(self):
        return self.status == 0
    
    def is_empty(self):
        return self.status == -1

    def __str__(self):
        output_str = "Cell #" + str(self.cell_num)
        if self.is_empty:
            output_str += " has not been placed"
        else:
            output_str += (" was placed by " + self.symbol)

        return output_str
