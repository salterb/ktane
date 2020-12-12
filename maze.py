from copy import copy

def get_coords(string):
    while True:
        coords = input(string).strip('()[] ')
        try:
            if (len(coords) >= 2 and
            1 <= int(coords[0]) <= 6 and
            1 <= int(coords[-1]) <= 6):
                return int(coords[0]), int(coords[-1])
        except ValueError:
            pass  # Fall through to error message below
        print("\nInvalid coordinates. Please provide (x,y) coordinates "
              "where 1 ≤ x,y ≤ 6\n")


class Maze:
    def __init__(self):
        while True:
            maze_ipt = get_coords("Enter the coordinates of any green circle in the maze: ")
            try:
                self.maze = MAZE_LOOKUP[maze_ipt]
                break
            except KeyError:
                print("Invalid circle coordinates")

        self.start = get_coords("Enter the coordinates of the START of the maze (white light): ")
        self.end = get_coords("Enter the coordinates of the END of the maze (red triangle): ")

    def DFS_maze(self):
        """Find the moves to solve the maze module by performing a DFS"""
        return self._DFS_maze_helper(self.start, self.end, [])


    def _DFS_maze_helper(self, player_pos, end, current_moves):
        """Internal function to perform a DFS to solve the maze.
        Has an extra bookkeeping parameter to track the putative
        list of current moves that the _actual_ solving function
        doesn't have
        """
        for move in self.maze[player_pos]:
            # Check if move is backtracking
            if len(current_moves) == 0 or move != -current_moves[-1]:
                new_moves = copy(current_moves)
                new_moves.append(move)
                new_pos = list(player_pos)
                if move in (LEFT, RIGHT):
                    new_pos[0] += move
                else:
                    # UP/DOWN are encoded as +/- 2 respectively
                    new_pos[1] += move//2
                new_pos = tuple(new_pos)
                if new_pos == end:
                    return new_moves
                possible_moves = self._DFS_maze_helper(new_pos, end, new_moves)

                # If we get non-None output from the DFS, it found a solution,
                # so propagate that down the call stack
                if possible_moves is not None:
                    return possible_moves
        return None

    def solve(self):
        moves = self.DFS_maze()
        print_moves(moves)

def print_moves(moves):
    """Prints the necessary moves to solve the maze."""
    print("")  # New line
    if moves is None:
        print("No moves - maybe you specified the same start and end point?")
        return

    for i, direction in enumerate(moves):
        print(f"{str(i+1)}: {MOVE_LOOKUP[direction]}")
    print("")  # New line



if __name__ == "__main__":
    print("Please run the script ktane.py instead!")

# Lookup tables
LEFT = -1
RIGHT = 1
UP = 2
DOWN = -2

MOVE_LOOKUP = {-1: "LEFT", 1: "RIGHT", -2: "DOWN", 2: "UP"}

MAZE_1 = {(1,1): [UP, RIGHT], (2,1): [LEFT], (3,1): [UP, RIGHT],
          (4,1): [LEFT, UP], (5,1): [RIGHT], (6,1): [LEFT, UP],
          (1,2): [UP, RIGHT, DOWN], (2,2): [LEFT, RIGHT], (3,2): [LEFT, DOWN],
          (4,2): [DOWN, RIGHT], (5,2): [LEFT], (6,2): [UP, DOWN],
          (1,3): [UP, DOWN], (2,3): [RIGHT], (3,3): [LEFT, UP, RIGHT],
          (4,3): [LEFT, UP], (5,3): [RIGHT], (6,3): [UP, LEFT, DOWN],
          (1,4): [UP, DOWN], (2,4): [RIGHT, UP], (3,4): [DOWN,LEFT],
          (4,4): [DOWN, RIGHT], (5,4): [LEFT, RIGHT], (6,4): [UP, LEFT, DOWN],
          (1,5): [UP, DOWN], (2,5): [RIGHT, DOWN], (3,5): [LEFT, UP],
          (4,5): [UP, RIGHT], (5,5): [LEFT, RIGHT], (6,5): [LEFT, DOWN],
          (1,6): [DOWN, RIGHT], (2,6): [LEFT, RIGHT], (3,6): [LEFT, DOWN],
          (4,6): [DOWN, RIGHT], (5,6): [LEFT, RIGHT], (6,6): [LEFT]}

MAZE_2 = {(1,1): [UP], (2,1): [UP, RIGHT], (3,1): [LEFT, UP],
          (4,1): [UP, RIGHT], (5,1): [LEFT, RIGHT], (6,1): [LEFT, UP],
          (1,2): [UP, DOWN], (2,2): [DOWN], (3,2): [UP, DOWN],
          (4,2): [RIGHT, DOWN], (5,2): [UP, RIGHT], (6,2): [UP, DOWN],
          (1,3): [UP, RIGHT, DOWN], (2,3): [LEFT, UP], (3,3): [DOWN, RIGHT],
          (4,3): [UP, LEFT], (5,3): [DOWN], (6,3): [UP, DOWN],
          (1,4): [UP, DOWN], (2,4): [RIGHT, DOWN], (3,4): [LEFT, UP],
          (4,4): [DOWN, RIGHT],(5,4): [LEFT, RIGHT], (6,4): [UP, LEFT, DOWN],
          (1,5): [DOWN, RIGHT], (2,5): [UP, LEFT], (3,5): [DOWN, RIGHT],
          (4,5): [UP, LEFT], (5,5): [RIGHT, UP], (6,5): [LEFT, DOWN],
          (1,6): [RIGHT], (2,6): [LEFT, RIGHT, DOWN], (3,6): [LEFT],
          (4,6): [DOWN, RIGHT], (5,6): [LEFT, RIGHT, DOWN], (6,6): [LEFT]}

MAZE_3 = {(1,1): [RIGHT, UP], (2,1): [LEFT, RIGHT], (3,1): [LEFT, RIGHT],
          (4,1): [LEFT, UP], (5,1): [UP, RIGHT], (6,1): [LEFT, UP],
          (1,2): [UP, DOWN], (2,2): [UP, RIGHT], (3,2): [LEFT, UP],
          (4,2): [UP, DOWN], (5,2): [UP, DOWN], (6,2): [UP, DOWN],
          (1,3): [UP, DOWN], (2,3): [UP, DOWN], (3,3): [UP, DOWN],
          (4,3): [UP, DOWN], (5,3): [UP, DOWN], (6,3): [UP, DOWN],
          (1,4): [DOWN, RIGHT], (2,4): [UP, DOWN, LEFT], (3,4): [UP, DOWN],
          (4,4): [DOWN, RIGHT], (5,4): [LEFT, DOWN], (6,4): [UP, DOWN],
          (1,5): [UP], (2,5): [DOWN], (3,5): [UP, DOWN],
          (4,5): [UP, RIGHT], (5,5): [UP, LEFT], (6,5): [UP, DOWN],
          (1,6): [DOWN, RIGHT], (2,6): [LEFT, RIGHT], (3,6): [LEFT, DOWN],
          (4,6): [DOWN], (5,6): [RIGHT, DOWN], (6,6): [LEFT, DOWN]}

MAZE_4 = {(1,1): [RIGHT, UP], (2,1): [LEFT, RIGHT], (3,1): [LEFT],
          (4,1): [RIGHT], (5,1): [LEFT, UP], (6,1): [UP],
          (1,2): [UP, RIGHT, DOWN], (2,2): [LEFT, RIGHT], (3,2): [LEFT, RIGHT],
          (4,2): [LEFT, RIGHT], (5,2): [LEFT, DOWN], (6,2): [UP, DOWN],
          (1,3): [UP, DOWN], (2,3): [RIGHT], (3,3): [LEFT, RIGHT],
          (4,3): [LEFT, RIGHT, UP], (5,3): [LEFT, RIGHT], (6,3): [LEFT, UP, DOWN],
          (1,4): [UP, DOWN], (2,4): [UP, RIGHT], (3,4): [LEFT, UP],
          (4,4): [DOWN, RIGHT], (5,4): [LEFT], (6,4): [UP, DOWN],
          (1,5): [UP, DOWN], (2,5): [UP, DOWN], (3,5): [DOWN, RIGHT],
          (4,5): [LEFT, RIGHT], (5,5): [LEFT, RIGHT], (6,5): [LEFT, UP, DOWN],
          (1,6): [RIGHT, DOWN], (2,6): [LEFT, DOWN], (3,6): [RIGHT],
          (4,6): [LEFT, RIGHT], (5,6): [LEFT, RIGHT], (6,6): [LEFT, DOWN]}

MAZE_5 = {(1,1): [UP], (2,1): [UP, RIGHT], (3,1): [LEFT, RIGHT],
          (4,1): [LEFT, RIGHT], (5,1): [LEFT, RIGHT], (6,1): [LEFT, UP],
          (1,2): [UP, DOWN], (2,2): [RIGHT, DOWN], (3,2): [LEFT, RIGHT],
          (4,2): [LEFT, RIGHT, UP], (5,2): [LEFT], (6,2): [UP, DOWN],
          (1,3): [UP, DOWN], (2,3): [UP, RIGHT], (3,3): [LEFT, RIGHT],
          (4,3): [LEFT, DOWN], (5,3): [UP], (6,3): [UP, DOWN],
          (1,4): [UP, RIGHT, DOWN], (2,4): [LEFT, DOWN], (3,4): [RIGHT],
          (4,4): [UP, LEFT], (5,4): [DOWN, RIGHT], (6,4): [LEFT, DOWN],
          (1,5): [DOWN, RIGHT], (2,5): [LEFT, RIGHT], (3,5): [LEFT, RIGHT],
          (4,5): [LEFT, DOWN, RIGHT], (5,5): [LEFT, UP], (6,5): [UP],
          (1,6): [RIGHT], (2,6): [LEFT, RIGHT], (3,6): [LEFT, RIGHT],
          (4,6): [LEFT, RIGHT], (5,6): [LEFT, DOWN, RIGHT], (6,6): [LEFT, DOWN]}

MAZE_6 = {(1,1): [RIGHT, UP], (2,1): [LEFT, RIGHT], (3,1): [LEFT, RIGHT],
          (4,1): [LEFT, UP], (5,1): [RIGHT], (6,1): [LEFT, UP],
          (1,2): [DOWN, RIGHT], (2,2): [UP, LEFT], (3,2): [UP],
          (4,2): [UP, DOWN], (5,2): [UP, RIGHT], (6,2): [DOWN, LEFT, UP],
          (1,3): [UP, RIGHT], (2,3): [LEFT, DOWN], (3,3): [DOWN, RIGHT],
          (4,3): [DOWN, LEFT, UP], (5,3): [UP, DOWN], (6,3): [DOWN],
          (1,4): [UP, RIGHT, DOWN], (2,4): [LEFT, UP], (3,4): [UP],
          (4,4): [UP, DOWN], (5,4): [DOWN, RIGHT], (6,4): [UP, LEFT],
          (1,5): [UP, DOWN], (2,5): [UP, DOWN], (3,5): [UP, DOWN],
          (4,5): [DOWN, RIGHT], (5,5): [LEFT, UP], (6,5): [UP, DOWN],
          (1,6): [DOWN], (2,6): [DOWN, RIGHT], (3,6): [DOWN, LEFT],
          (4,6): [RIGHT], (5,6): [LEFT, DOWN, RIGHT], (6,6): [LEFT, DOWN]}

MAZE_7 = {(1,1): [RIGHT, UP], (2,1): [LEFT, RIGHT], (3,1): [LEFT, RIGHT],
          (4,1): [LEFT, RIGHT], (5,1): [LEFT, UP, RIGHT], (6,1): [LEFT, UP],
          (1,2): [UP, DOWN], (2,2): [UP], (3,2): [UP, RIGHT],
          (4,2): [LEFT, RIGHT], (5,2): [LEFT, DOWN], (6,2): [UP, DOWN],
          (1,3): [DOWN, RIGHT], (2,3): [LEFT, DOWN], (3,3): [UP, RIGHT, DOWN],
          (4,3): [LEFT, RIGHT], (5,3): [LEFT, UP], (6,3): [DOWN],
          (1,4): [UP, RIGHT], (2,4): [LEFT, UP], (3,4): [DOWN, RIGHT],
          (4,4): [LEFT], (5,4): [DOWN, RIGHT], (6,4): [LEFT, UP],
          (1,5): [UP, DOWN], (2,5): [DOWN, RIGHT], (3,5): [LEFT],
          (4,5): [UP, RIGHT], (5,5): [LEFT, UP], (6,5): [UP, DOWN],
          (1,6): [DOWN, RIGHT], (2,6): [LEFT, RIGHT], (3,6): [LEFT, RIGHT],
          (4,6): [LEFT, DOWN], (5,6): [DOWN, RIGHT], (6,6): [LEFT, DOWN]}

MAZE_8 = {(1,1): [RIGHT, UP], (2,1): [LEFT, UP, RIGHT], (3,1): [LEFT, RIGHT],
          (4,1): [LEFT, RIGHT], (5,1): [LEFT, RIGHT], (6,1): [LEFT],
          (1,2): [UP, DOWN], (2,2): [DOWN], (3,2): [UP, RIGHT],
          (4,2): [LEFT, RIGHT], (5,2): [LEFT, RIGHT], (6,2): [LEFT],
          (1,3): [UP, DOWN], (2,3): [UP, RIGHT], (3,3): [LEFT, DOWN],
          (4,3): [RIGHT], (5,3): [LEFT, UP, RIGHT], (6,3): [LEFT, UP],
          (1,4): [UP, DOWN], (2,4): [DOWN, RIGHT], (3,4): [LEFT, RIGHT],
          (4,4): [LEFT, RIGHT], (5,4): [LEFT, DOWN], (6,4): [UP, DOWN],
          (1,5): [UP, RIGHT, DOWN], (2,5): [LEFT, RIGHT, UP], (3,5): [LEFT],
          (4,5): [UP, RIGHT], (5,5): [LEFT, UP], (6,5): [UP, DOWN],
          (1,6): [DOWN], (2,6): [DOWN, RIGHT], (3,6): [LEFT, RIGHT],
          (4,6): [LEFT, DOWN], (5,6): [DOWN, RIGHT], (6,6): [LEFT, DOWN]}

MAZE_9 = {(1,1): [UP, RIGHT], (2,1): [LEFT, UP], (3,1): [UP, RIGHT],
          (4,1): [LEFT, UP], (5,1): [UP, RIGHT], (6,1): [LEFT],
          (1,2): [UP, DOWN], (2,2): [UP, DOWN], (3,2): [UP, DOWN],
          (4,2): [DOWN, RIGHT], (5,2): [LEFT, DOWN], (6,2): [UP],
          (1,3): [UP, DOWN], (2,3): [DOWN], (3,3): [DOWN, RIGHT],
          (4,3): [LEFT, UP], (5,3): [RIGHT], (6,3): [DOWN, LEFT, UP],
          (1,4): [DOWN, RIGHT, UP], (2,4): [LEFT, UP, RIGHT], (3,4): [LEFT, UP],
          (4,4): [DOWN, RIGHT], (5,4): [LEFT, UP], (6,4): [UP, DOWN],
          (1,5): [UP, DOWN], (2,5): [UP, DOWN], (3,5): [DOWN, RIGHT],
          (4,5): [LEFT], (5,5): [UP, DOWN], (6,5): [UP, DOWN],
          (1,6): [DOWN], (2,6): [DOWN, RIGHT], (3,6): [LEFT, RIGHT],
          (4,6): [LEFT, RIGHT], (5,6): [LEFT, DOWN, RIGHT], (6,6): [LEFT, DOWN]}


MAZE_LOOKUP = {(1,5): MAZE_1, (6,4): MAZE_1,
               (2,3): MAZE_2, (5,5): MAZE_2,
               (4,3): MAZE_3, (6,3): MAZE_3,
               (1,3): MAZE_4, (1,6): MAZE_4,
               (4,1): MAZE_5, (5,4): MAZE_5,
               (3,2): MAZE_6, (5,6): MAZE_6,
               (2,1): MAZE_7, (2,6): MAZE_7,
               (3,3): MAZE_8, (4,6): MAZE_8,
               (1,2): MAZE_9, (3,5): MAZE_9}
