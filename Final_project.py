# Game of Life
# Stage 1: Initialize the board
# There are mainly two goals of the board:
#  a. the board should be of right size
#  b. each cell should be randomly initialized(either 1 or 0, dead or alive)
import random
def dead_state(width, height):
    # the board is a list of lists
    column = []
    for h in range(height):
        row = []
        for w in range(width):
            #use the random function to generate random number from 0 to 1.0
            random_number = random.random()
            # 0 for dead, 1 for alive
            if random_number >= 0.5:
                cell_state = 0
            else:
                cell_state = 1
            row.append(cell_state)
        column.append(row)
    return column

print(dead_state(5,5))