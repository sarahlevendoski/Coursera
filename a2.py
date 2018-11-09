# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    def __init__(self, symbol, row, col):
        """ (Rat, str, int, int) -> NoneType

        The Rat's inital position in the maze.  The Rat is represented by a one letter string.  
        It's position is represented first by an int which is the row number and secondly by an int which is the column number.
        
        >>> Rat(’P’, 1, 4)
        >>> Rat('J', 2, 3)    
        """
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0    


    def set_location(self, row, col):
        """ (Rat, int, int) -> NoneType

        The first int is the rat's row position and the second int is the rat's column position.

        >>> rat_1 = Rat('P', 1, 4)
        >>> rat_1.set_location(1, 2)

        >>> rat_2 = Rat('J', 2, 3)
        >>> rat_2.set_location(2, 3)              
        """
        self.row = row
        self.col = col


    def eat_sprout(self):
        """ (Rat) -> NoneType

        Tells the rat to eat a sprout.  

        >>> rat_1 = Rat('P', 1, 4)
        >>> rat_1.eat_sprout()

        >>> rat_2 = Rat('J', 2, 3)
        >>> rat_2.eat_sprout()        
        """

        self.num_sprouts_eaten = self.num_sprouts_eaten + 1
    

    def __str__(self):
        """ (Rat) -> str

        Return a string represention of the Rat in the following format: symbol at (row, col) ate num_sprouts_eaten sprouts.

        >>> rat_1 = Rat('P', 1, 4)
        >>> str(rat_1)
        'P at (1, 4) ate 0 sprouts.'
        """

        return '{0} at ({1}, {2}) ate {3} sprouts.'.format(self.symbol, self.row, self.col, self.num_sprouts_eaten)


class Maze:
    """ A 2D maze. """

    def __init__(self, contents_of_maze, rat_1, rat_2):
        """ (Maze, list of list of str, Rat, Rat) -> NoneType

        The layout of the maze, including locations of walls, halls, sprouts, rat 1 and rat 2

        >>> rat_1 = Rat('P', 1, 1)
        >>> rat_2 = Rat('J', 1, 4)

        >>> Maze([['#', '#', '#', '#', '#', '#', '#'], 
        ['#', '.', '.', '.', '.', '.', '#'], 
        ['#', '.', '#', '#', '#', '.', '#'], 
        ['#', '.', '.', '@', '#', '.', '#'], 
        ['#', '@', '#', '.', '@', '.', '#'], 
        ['#', '#', '#', '#', '#', '#', '#']],
        Rat('P', 1, 1),
        Rat('J', 1, 4)) 
        """

        self.maze = contents_of_maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = 0
       
        for row in contents_of_maze:
            for item in row:
                if item == '@':
                    self.num_sprouts_left = self.num_sprouts_left + 1
                    

    def is_wall(self, row, col):
        """ (Maze, int, int) -> bool

        Precondition: The rows and columns are all within the bounds of the maze.

        Represents the Maze itself and the row and column.  Return True if and only if there is a wall at the given row and column.

        >>> maze_1 = Maze([['#', '#', '#', '#', '#', '#', '#'], 
        ['#', '.', '.', '.', '.', '.', '#'], 
        ['#', '.', '#', '#', '#', '.', '#'], 
        ['#', '.', '.', '@', '#', '.', '#'], 
        ['#', '@', '#', '.', '@', '.', '#'], 
        ['#', '#', '#', '#', '#', '#', '#']],
        Rat('P', 1, 1),
        Rat('J', 1, 4))
        >>> maze_1.is_wall(2, 2)
        True
        >>> maze_1.is_wall(3, 1)
        False
        """

        return self.maze[row][col] == WALL


    def get_character(self, row, col):
        """ (Maze, int, int) -> str

        Precondition: The rows and columns are all within the bounds of the maze.

        Represents the Maze, row and column.  Return the character in the maze at the given row and column.
        If there is a rat at that location then its character should be returned rather than HALL.

        >>> maze_1 = Maze([['#', '#', '#', '#', '#', '#', '#'], 
        ['#', '.', '.', '.', '.', '.', '#'], 
        ['#', '.', '#', '#', '#', '.', '#'], 
        ['#', '.', '.', '@', '#', '.', '#'], 
        ['#', '@', '#', '.', '@', '.', '#'], 
        ['#', '#', '#', '#', '#', '#', '#']],
        Rat('P', 1, 1),
        Rat('J', 1, 4))

        >>> maze_1.get_character(2, 1)
        HALL
        >>> maze_1.get_character(4, 2)
        WALL
        >>> maze_1.get_character(4, 1)
        SPROUT
        """

        if self.rat_1.row == row and self.rat_1.col == col:
            return self.rat_1.symbol
        elif self.rat_2.row == row and self.rat_2.col == col:
            return self.rat_2.symbol
        else:
            return self.maze[row][col]


    def move(self, rat, vertical_change, horizontal_change):
        """ (Maze, Rat, int, int) -> bool

        Precondition: Vertical and/or Horizontal change will not put the rat outside the bounds of the maze.

        Represents the Maze, the Rat, a vertical change (UP, NO_CHANGE, or DOWN), and a horizontal change (LEFT, NO_CHANGE, or RIGHT).
        Move the Rat in the given direction, unless there is a wall in the way.

        >>> rat_1 = Rat('P', 1, 1)
        >>> rat_2 = Rat('J', 1, 4)
        
        >>> maze_1 = Maze([['#', '#', '#', '#', '#', '#', '#'], 
        ['#', '.', '.', '.', '.', '.', '#'], 
        ['#', '.', '#', '#', '#', '.', '#'], 
        ['#', '.', '.', '@', '#', '.', '#'], 
        ['#', '@', '#', '.', '@', '.', '#'], 
        ['#', '#', '#', '#', '#', '#', '#']],
        rat_1,
        rat_2)

        >>> maze_1.move(rat_1, 1, 0)
        True
        >>> maze_1.move(rat_2, 1, -1)
        False
        """
        
        if self.is_wall(rat.row + vertical_change, rat.col + horizontal_change):
            return False
        else:
            rat.set_location(rat.row + vertical_change, rat.col + horizontal_change)
            if self.maze[rat.row][rat.col] == SPROUT:
                rat.eat_sprout()
                self.num_sprouts_left = self.num_sprouts_left - 1
                self.maze[rat.row][rat.col] = HALL
            return True

    def __str__(self):
        """ (Maze) -> str

        Returns a string representation of the Maze.

        >>> maze_1 = Maze([['#', '#', '#', '#', '#', '#', '#'], 
        ['#', '.', '.', '.', '.', '.', '#'], 
        ['#', '.', '#', '#', '#', '.', '#'], 
        ['#', '.', '.', '@', '#', '.', '#'], 
        ['#', '@', '#', '.', '@', '.', '#'], 
        ['#', '#', '#', '#', '#', '#', '#']],
        Rat('P', 1, 1),
        Rat('J', 1, 4))
        
        >>> str(maze_1)
        #######
        #J..P.#
        #.###.#
        #..@#.#
        #@#.@.#
        #######
        J at (1, 1) ate 0 sprouts.
        P at (1, 4) ate 0 sprouts.
        """

        result = ''
        
        for row in self.maze:
            result = result + ''.join(row) + '\n'
        return result + str(self.rat_1) + '\n' + str(self.rat_2)
            
