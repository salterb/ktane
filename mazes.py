LEFT = -1
RIGHT = 1
UP = 2
DOWN = -2

maze1ValidMoves = {(1,1): [UP, RIGHT], (2,1): [LEFT], (3,1): [UP, RIGHT],
                   (4,1): [LEFT, UP], (5,1): [RIGHT], (6,1): [LEFT, UP],
                   (1,2): [UP, RIGHT, DOWN], (2,2): [LEFT, RIGHT],
                   (3,2): [LEFT, DOWN], (4,2): [DOWN, RIGHT], (5,2): [LEFT],
                   (6,2): [UP, DOWN], (1,3): [UP, DOWN], (2,3): [RIGHT],
                   (3,3): [LEFT, UP, RIGHT], (4,3): [LEFT, UP],
                   (5,3): [RIGHT], (6,3): [UP, LEFT, DOWN],
                   (1,4): [UP, DOWN], (2,4): [RIGHT, UP], (3,4): [DOWN,LEFT],
                   (4,4): [DOWN, RIGHT], (5,4): [LEFT, RIGHT],
                   (6,4): [UP, LEFT, DOWN], (1,5): [UP, DOWN],
                   (2,5): [RIGHT, DOWN], (3,5): [LEFT, UP],
                   (4,5): [UP, RIGHT], (5,5): [LEFT, RIGHT],
                   (6,5): [LEFT, DOWN], (1,6): [DOWN, RIGHT],
                   (2,6): [LEFT, RIGHT], (3,6): [LEFT, DOWN],
                   (4,6): [DOWN, RIGHT], (5,6): [LEFT, RIGHT], (6,6): [LEFT]}

maze2ValidMoves = {(1,1): [UP], (2,1): [UP, RIGHT], (3,1): [LEFT, UP],
                   (4,1): [UP, RIGHT], (5,1): [LEFT, RIGHT],
                   (6,1): [LEFT, UP], (1,2): [UP, DOWN], (2,2): [DOWN],
                   (3,2): [UP, DOWN], (4,2): [RIGHT, DOWN],
                   (5,2): [UP, RIGHT], (6,2): [UP, DOWN],
                   (1,3): [UP, RIGHT, DOWN], (2,3): [LEFT, UP],
                   (3,3): [DOWN, RIGHT], (4,3): [UP, LEFT], (5,3): [DOWN],
                   (6,3): [UP, DOWN], (1,4): [UP, DOWN], (2,4): [RIGHT, DOWN],
                   (3,4): [LEFT, UP], (4,4): [DOWN, RIGHT],
                   (5,4): [LEFT, RIGHT], (6,4): [UP, LEFT, DOWN],
                   (1,5): [DOWN, RIGHT], (2,5): [UP, LEFT],
                   (3,5): [DOWN, RIGHT], (4,5): [UP, LEFT],
                   (5,5): [RIGHT, UP], (6,5): [LEFT, DOWN], (1,6): [RIGHT],
                   (2,6): [LEFT, RIGHT, DOWN], (3,6): [LEFT],
                   (4,6): [DOWN, RIGHT], (5,6): [LEFT, RIGHT, DOWN],
                   (6,6): [LEFT]}

maze3ValidMoves = {(1,1): [RIGHT, UP], (2,1): [LEFT, RIGHT],
                   (3,1): [LEFT, RIGHT], (4,1): [LEFT, UP], (5,1): [UP, RIGHT],
                   (6,1): [LEFT, UP], (1,2): [UP, DOWN], (2,2): [UP, RIGHT],
                   (3,2): [LEFT, UP], (4,2): [UP, DOWN], (5,2): [UP, DOWN],
                   (6,2): [UP, DOWN], (1,3): [UP, DOWN], (2,3): [UP, DOWN],
                   (3,3): [UP, DOWN], (4,3): [UP, DOWN], (5,3): [UP, DOWN],
                   (6,3): [UP, DOWN], (1,4): [DOWN, RIGHT],
                   (2,4): [UP, DOWN, LEFT], (3,4): [UP, DOWN],
                   (4,4): [DOWN, RIGHT], (5,4): [LEFT, DOWN],
                   (6,4): [UP, DOWN], (1,5): [UP], (2,5): [DOWN],
                   (3,5): [UP, DOWN], (4,5): [UP, RIGHT], (5,5): [UP, LEFT],
                   (6,5): [UP, DOWN], (1,6): [DOWN, RIGHT],
                   (2,6): [LEFT, RIGHT], (3,6): [LEFT, DOWN], (4,6): [DOWN],
                   (5,6): [RIGHT, DOWN], (6,6): [LEFT, DOWN]}

maze4ValidMoves = {(1,1): [LEFT, UP], (2,1): [LEFT, RIGHT], (3,1): [LEFT],
                   (4,1): [RIGHT], (5,1): [LEFT, UP], (6,1): [UP],
                   (1,2): [UP, RIGHT, DOWN], (2,2): [LEFT, RIGHT],
                   (3,2): [LEFT, RIGHT], (4,2): [LEFT, RIGHT],
                   (5,2): [LEFT, DOWN], (6,2): [UP, DOWN], (1,3): [UP, DOWN],
                   (2,3): [RIGHT], (3,3): [LEFT, RIGHT],
                   (4,3): [LEFT, RIGHT, UP], (5,3): [LEFT, RIGHT],
                   (6,3): [LEFT, UP, DOWN], (1,4): [UP, DOWN],
                   (2,4): [UP, RIGHT], (3,4): [LEFT, UP], (4,4): [DOWN, RIGHT],
                   (5,4): [LEFT], (6,4): [UP, DOWN], (1,5): [UP, DOWN],
                   (2,5): [UP, DOWN], (3,5): [DOWN, RIGHT],
                   (4,5): [LEFT, RIGHT], (5,5): [LEFT, RIGHT],
                   (6,5): [LEFT, UP, DOWN], (1,6): [RIGHT, DOWN],
                   (2,6): [LEFT, DOWN], (3,6): [RIGHT], (4,6): [LEFT, RIGHT],
                   (5,6): [LEFT, RIGHT], (6,6): [LEFT, DOWN]}

maze5ValidMoves = {(1,1): [UP], (2,1): [UP, LEFT], (3,1): [LEFT, RIGHT],
                   (4,1): [LEFT, RIGHT], (5,1): [LEFT, RIGHT],
                   (6,1): [LEFT, UP], (1,2): [UP, DOWN], (2,2): [RIGHT, DOWN],
                   (3,2): [LEFT, RIGHT], (4,2): [LEFT, RIGHT, UP],
                   (5,2): [RIGHT], (6,2): [UP, DOWN], (1,3): [UP, DOWN],
                   (2,3): [UP, RIGHT], (3,3): [LEFT, RIGHT],
                   (4,3): [LEFT, DOWN], (5,3): [UP], (6,3): [UP, DOWN],
                   (1,4): [UP, RIGHT, DOWN], (2,4): [LEFT, DOWN],
                   (3,4): [RIGHT], (4,4): [UP, LEFT], (5,4): [DOWN, RIGHT],
                   (6,4): [LEFT, DOWN], (1,5): [DOWN, RIGHT],
                   (2,5): [LEFT, RIGHT], (3,5): [LEFT, RIGHT],
                   (4,5): [LEFT, DOWN, RIGHT], (5,5): [LEFT, UP],
                   (6,5): [UP], (1,6): [LEFT], (2,6): [LEFT, RIGHT],
                   (3,6): [LEFT, RIGHT], (4,6): [LEFT, RIGHT],
                   (5,6): [LEFT, DOWN, RIGHT], (6,6): [LEFT, DOWN]}

maze6ValidMoves = {(1,1): [RIGHT, UP], (2,1): [LEFT, RIGHT],
                   (3,1): [LEFT, RIGHT], (4,1): [LEFT, UP], (5,1): [RIGHT],
                   (6,1): [LEFT, UP], (1,2): [DOWN, RIGHT], (2,2): [UP, LEFT],
                   (3,2): [UP], (4,2): [UP, DOWN], (5,2): [UP, RIGHT],
                   (6,2): [DOWN, LEFT, UP], (1,3): [UP, RIGHT],
                   (2,3): [LEFT, DOWN], (3,3): [DOWN, RIGHT],
                   (4,3): [DOWN, LEFT, UP], (5,3): [UP, DOWN], (6,3): [DOWN],
                   (1,4): [UP, RIGHT, DOWN], (2,4): [LEFT, UP], (3,4): [UP],
                   (4,4): [UP, DOWN], (5,4): [DOWN, RIGHT], (6,4): [UP, LEFT],
                   (1,5): [UP, DOWN], (2,5): [UP, DOWN], (3,5): [UP, DOWN],
                   (4,5): [DOWN, RIGHT], (5,5): [LEFT, UP], (6,5): [UP, DOWN],
                   (1,6): [DOWN], (2,6): [DOWN, RIGHT], (3,6): [DOWN, LEFT],
                   (4,6); [RIGHT], (5,6): [LEFT, DOWN, RIGHT],
                   (6,6): [LEFT, DOWN]}
                   
maze7ValidMoves = {(1,1): [RIGHT, UP], (2,1): [LEFT, RIGHT],
                   (3,1): [LEFT, RIGHT], (4,1): [LEFT, RIGHT],
                   (5,1): [LEFT, UP, RIGHT], (6,1): [LEFT, UP]
                   (1,2): [UP, DOWN], (2,2): [UP], (3,2): [UP, RIGHT],
                   (4,2): [LEFT, RIGHT], (5,2): [LEFT, DOWN],
                   (6,2): [UP, DOWN], (1,3): [DOWN, RIGHT],
                   (2,3): [LEFT, DOWN], (3,3): [UP, RIGHT, DOWN],
                   (4,3): [LEFT, RIGHT], (5,3): [LEFT, UP], (6,3): [DOWN],
                   (1,4): [UP, RIGHT], (2,4): [LEFT, UP], (3,4): [DOWN, RIGHT],
                   (4,4): [LEFT], (5,4): [DOWN, RIGHT], (6,4): [LEFT, UP],
                   (1,5): [UP, DOWN], (2,5): [DOWN, RIGHT], (3,5): [LEFT],
                   (4,5): [UP, RIGHT], (5,5): [LEFT, UP], (6,5): [UP, DOWN],
                   (1,6): [DOWN, RIGHT], (2,6): [LEFT, RIGHT],
                   (3,6): [LEFT, RIGHT], (4,6): [LEFT, DOWN],
                   (5,6): [DOWN, RIGHT], (6,6): [LEFT, DOWN]}

maze8ValidMoves = {(1,1): [LEFT, UP], (2,1): [LEFT, UP, RIGHT],
                   (3,1): [LEFT, RIGHT], (4,1): [LEFT, RIGHT],
                   (5,1): [LEFT, RIGHT], (6,1): [RIGHT], (1,2): [UP, DOWN],
                   (2,2): [DOWN], (3,2): [UP, RIGHT], (4,2): [LEFT, RIGHT],
                   (5,2): [LEFT, RIGHT], (6,2): [LEFT], (1,3): [UP, DOWN],
                   (2,3): [UP, RIGHT], (3,3): [LEFT, DOWN], (4,3): [RIGHT],
                   (5,3): [LEFT, UP, RIGHT], (6,3): [LEFT, UP],
                   (1,4): [UP, DOWN], (2,4): [DOWN, RIGHT],
                   (3,4): [LEFT, RIGHT], (4,4): [LEFT, RIGHT],
                   (5,4): [LEFT, DOWN], (6,4); [UP, DOWN],
                   (1,5): [UP, RIGHT, DOWN], (2,5): [LEFT, RIGHT, UP],
                   (3,5): [LEFT], (4,5): [UP, RIGHT], (5,5): [LEFT, UP],
                   (6,5): [UP, DOWN], (1,6): [DOWN], (2,6): [DOWN, RIGHT],
                   (3,6): [LEFT, RIGHT], (4,6): [LEFT, DOWN],
                   (5,6): [DOWN, RIGHT], (6,6): [LEFT, DOWN]}

maze9ValidMoves = {(1,1): [UP, RIGHT], (2,1): [LEFT, UP], (3,1): [UP, RIGHT],
                   (4,1): [LEFT, UP], (5,1): [UP, RIGHT], (6,1): [LEFT],
                   (1,2): [UP, DOWN], (2,2): [UP, DOWN], (3,2): [UP, DOWN],
                   (4,2): [DOWN, RIGHT], (5,2): [LEFT, DOWN], (6,2): [UP],
                   (1,3): [UP, DOWN], (2,3): [DOWN], (3,3): [DOWN, RIGHT],
                   (4,3): [LEFT, UP], (5,3): [RIGHT], (6,3): [DOWN, LEFT, UP],
                   (1,4): [DOWN, RIGHT UP], (2,4): [LEFT, UP, RIGHT],
                   (3,4): [LEFT, UP], (4,4): [DOWN, RIGHT], (5,4): [LEFT, UP],
                   (6,4): [UP, DOWN], (1,5): [UP, DOWN], (2,5): [UP, DOWN],
                   (3,5): [DOWN, RIGHT], (4,5): [LEFT], (5,5): [UP, DOWN],
                   (6,5): [UP, DOWN], (1,6): [DOWN], (2,6): [DOWN, RIGHT],
                   (3,6): [LEFT, RIGHT], (4,6): [LEFT, RIGHT],
                   (5,6): [LEFT, DOWN, RIGHT], (6,6): [LEFT, DOWN]}



mazeLookup = {(1,5): maze1ValidMoves, (6,4): maze1ValidMoves,
              (2,3): maze2ValidMoves, (5,5): maze2ValidMoves,
              (4,3): maze3ValidMoves, (6,3): maze3ValidMoves,
              (1,3): maze4ValidMoves, (1,6): maze4ValidMoves,
              (4,1): maze5ValidMoves, (5,4): maze5ValidMoves,
              (3,2): maze6ValidMoves, (5,6): maze6ValidMoves,
              (2,1): maze7ValidMoves, (2,6): maze7ValidMoves,
              (3,3): maze8ValidMoves, (4,6): maze8ValidMoves,
              (1,2): maze9ValidMoves, (3,5): maze9ValidMoves}

def DFS_maze_helper(maze, player_pos, end, current_moves):
    """
    Performs a DFS to find the solution to a maze.
    We use a dictionary to lookup permissable directions but also want to 
    modify the entries of the coordinate vectors for the start point, so we
    have to convert from list to tuple on the fly.
    """
    # Find the maze we are working with
    M = mazeLookup[maze]
    
    for move in M[tuple(player_pos)]:
        # We don't want to backtrack our most recent move
        if len(current_moves) == 0 or move != -current_moves[-1]:
            new_moves = current_moves[:]
            new_moves.append(move)
            new_pos = player_pos[:]
            
            if move == LEFT or move == RIGHT:
                new_pos[0]+=move
            else:
                new_pos[1]+=move//2 # UP/DOWN are encoded as +/- 2 respectively
            if new_pos == end:
                return new_moves
            
            # If we get non-None output from our DFS helper, then it found the
            # solution. We want to pass this down the call chain
            possible_moves = DFS_maze_helper(maze, new_pos, end, new_moves)
            if possible_moves != None:
                return possible_moves
    
def DFS_maze(maze, start, end):
    """ Initiates the DFS by calling the helper with an empty array """
    return DFS_maze_helper(maze, list(start), list(end), [])

def print_moves(maze, start, end):
    """ Prints the necessary moves to solve the maze. Currently not very
        aesthetic - will replace """
    moves = DFS_maze(maze, start, end)
    if moves == None:
        throw Exception("Moves returned None - something wrong with DFS?")
    for direction in moves:
        if direction == -1:
            print("LEFT")
        elif direction == 1:
            print("RIGHT")
        elif direction == 2:
            print("UP")
        else:
            print("DOWN")

def solve_maze():
    valid_symbols = [1,2,3,4,5,6]
    
    # Do-whiles for input
    while True:
        maze_ipt = input("Enter the coordinates of "
                        "any green circle in the maze: ").strip('()[] ')
        if (int(maze_ipt[0]) in valid_symbols and 
            int(maze_ipt[-1] in valid_symbols):
                break
        print("\nInvalid coordinates. Please provide (x,y) coordinates,"
              " where 1 < x,y < 6\n")
              
    # Assume the first and last digits are the correct ones, after
    # removing any brackets and whitespace.
    maze = (int(maze_ipt[0]), int(maze_ipt[-1]))
    
    while True:
        start_ipt = input("Enter the coordinates of the START of "
                          "the maze (white light): ").strip('()[] ')
        if (int(start_ipt[0]) in valid_symbols and 
            int(start_ipt[-1] in valid_symbols):
                break
        print("\nInvalid coordinates. Please provide (x,y) coordinates,"
              " where 1 < x,y < 6\n")
    start = (int(start_ipt[0]), start_ipt[-1])
    
    while True:
        end_ipt = input("Enter the coordinates of the END of the "
                        "maze (red triangle): ").strip('()[] ')
        if (int(end_ipt[0]) in valid_symbols and 
            int(end_ipt[-1] in valid_symbols):
                break
        print("\nInvalid coordinates. Please provide (x,y) coordinates,"
              " where 1 < x,y < 6\n")
    end = (int(end_ipt[0]), int(end_ipt[-1]))
    
    print_moves(maze, start, end)
