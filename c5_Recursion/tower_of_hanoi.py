'''
Logic:
if we know how to move two disks to last pole, we can move three by moving two to the intermediate pole, moving the
bottom disc, and call 2 disc solution to move to last pole
base case: height == 1

Pseudocode:
def move_tower(height-1, from_pole, with_pole, to_pole:
    move_tower(height-1, from_pole, to_pole, with_pole)
    move_disc(from_pole, to_pole)
    move_tower(height-1, with_pole, from_pole, to_pole)

Exploring a maze
def make_move(direction):
    try moving north, if successful return True, direction

def solve_maze():
    base case: if square == 'end', return number of moves
    else
'''

def move_tower(height, from_pole, with_pole, to_pole):
    return
