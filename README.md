# 452_final_project_repo

How to run the program?

Just download the py file on moodle and run it.

Test_code.ipynb file is a file with testing codes.  


Project Abstract



My final project would be a programming project, the name of which is Game of Life(Or just “Life”). This is a game that creates a 2D world where all cells live in a grid of squares,  according to some given rules, they may live, die and evolve.  The initial status of cells are either “alive” or “dead”.  Each cell has a life circle, during which the status of a cell may change. The number of  8 immediate neighbors that are alive have impact on the change. 
There are 4 rules that control the updates of cell liveness: 
1.	Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
2.	Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
3.	Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
4.	Any dead cell with exactly 3 live neighbors becomes alive, by reproduction

Expected Deliverables
1.	Analyze the project. Understand the final goals, have an overall thought about how to do the work and come up with some specific methods that can be used to solve the problem. 
2.	Write draft code. This is the phase that I will divide the project problem into small tasks and finish them one by one. 
3.	Assemble the tasks that have been finished previously. The main code work will be done, which means the program should be fully functional and can meet the requirements. 
4.	Some extensions. In addition to realize the basic goals, I will do some extension work at this point, like improve the user interface, change the rules of life to see what will happen, etc.     
5.	Write the narrative file of the final project. 

I’d like due the first deliverable at the midpoint check in. Frist, I need to create the board which contains all the squares and initialize the liveness of some cells. Second, implement the rules that controls the updates of cells. Third, test the code and run life. Here are more detailed steps. 

Steps
1.	Build the basic structures and store the board state. 
2.	Print the board to the terminal. 
3.	Calculate the next state of the board according to the rules of Life. 
•	How to store new state?
•	How to calculate the number of live neighbors. 
•	How to deal with the cells on the edge?
4.	Run Life. 
5.	Do some extension work. 
