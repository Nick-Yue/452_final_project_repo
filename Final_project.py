# Game of Life
# Stage 1: Initialize the board
# There are mainly two goals of the board:
#  a. the board should be of right size
#  b. each cell should be randomly initialized(either 1 or 0, dead or alive)
import random
import time
def random_state(width, height):
    # the board is a list of lists
    state = []
    for x in range(width):
        row = []
        for y in range(height):
            #use the random function to generate random number from 0 to 1.0
            random_number = random.random()
            # 0 for dead, 1 for alive
            if random_number >= 0.5:
                cell_state = 0
            else:
                cell_state = 1
            row.append(cell_state)
        state.append(row)
    return state


#Statge 2: Print the state/board in the terminal. 

# define a function that can return the width of the state.
def state_width(statename):
    return len(statename)

#define a function that can return the height of the state.
def state_height(statename):
    return len(statename[0])

#define a render function that can print the board int the terminal.
def render(state):
    board = ''
    for y in state:
        row = ''
        for x in y:
            status = ''
            if x == 0:
                status = u"\u2591"
            else:
                status = u"\u2588"
            row =row + status
        board = board + row +'\n'
    print (board)


#Stage 3: Calculate the next state of the board

#define a function that can calculate the next value of a cell in a state.
def next_cell_value(cell_coords, state):
    width = state_width(state) #get the width of the state.
    height = state_height(state) # get the height of the state.
    x = cell_coords[0]
    y = cell_coords[1] # cell_coords is a (x, y) tuple pair of a cell. 
    num_of_live_neighbors = 0 # number of live neighbors of each cell.
    #iterate over the neighbor cells.
    for x1 in range(x-1,(x+1)+1):
        if x1-1 <0 or x1>=width: continue # make sure we dont go off eadge cells.
        for y1 in range(y-1, (y+1)+1):
            if y1-1<0 or y1>=height:continue
            if x1==x and y1==y: continue # make sure we dont go off the cell itself.
            if state[x1][y1] ==1:
                num_of_live_neighbors +=1
    if state[x][y] ==1:
        if num_of_live_neighbors <=1:
            return int(0)
        elif num_of_live_neighbors <=3:
            return int(1)
        else:
            return int(0)
    else:
        if num_of_live_neighbors ==3:
            return int(1)
        else:
            return int(0)

# define a function that can create a new board that stores all the new values of cells.
def next_board_state(initial_state):
    width = state_width(initial_state)
    height = state_height(initial_state)
    next_state = random_state(width, height)
    for x in range(0,width):
        for y in range(0,height):
            next_state[x][y] = next_cell_value((x,y),initial_state)
    return next_state 


def run_forever(initial_state):
    next_state = initial_state
    while True:
        render(next_state)
        next_state = next_board_state(next_state)
        time.sleep(0.03)

if __name__ == "__main__":
    initial_state = random_state(100, 50)
    # init_state = load_board_state('./toad.txt')
    run_forever(initial_state)          

# state1 = random_state(60,30)
# print(state1)
# print(state_height(state1))
# print(state_width(state1))
# print(render(state1))