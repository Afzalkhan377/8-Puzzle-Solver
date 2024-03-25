#
# eight_puzzle.py (Final project)
#
# driver/test code for state-space search on Eight Puzzles   
#
# name: 
# email:
#
# If you worked with a partner, put their contact info below:
# partner's name: jamil
# partner's email:kjkjamil@bu.edu
#

from searcher import *
from timer import *

def create_searcher(algorithm, param):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * param - a parameter that can be used to specify either
            a depth limit or the name of a heuristic function
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(param)

    elif algorithm == 'BFS':
        searcher = BFSearcher(param)
    elif algorithm == 'DFS':
       searcher = DFSearcher(param)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(param)
    elif algorithm == 'A*':
        searcher = AStarSearcher(param)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher

def eight_puzzle(init_boardstr, algorithm, param):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * param - a parameter that is used to specify either a depth limit
            or the name of a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')
    searcher = create_searcher(algorithm, param)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()


def  process_file(filename, algorithm, param):
    """ processes a file and solves all the puzzle using the algorithm and parameter given. 
    """
    file = open(filename, 'r')
    count=0
    num_moves=0
    num_tested=0
    for line in file:
        s=line[:9]
        init_board = Board(s)
        init_state = State(init_board, None, 'init')
        searcher = create_searcher(algorithm, param)
        try:
            soln = searcher.find_solution(init_state)
            if soln==None: 
                print (s + ":", "no solution")
            else:
                print (s,":", soln.num_moves,"moves,", searcher.num_tested,"states tested")
                count+=1
                num_moves+=soln.num_moves
                num_tested+= searcher.num_tested
               
        except KeyboardInterrupt:
             print(s,": Search terminated, no solution")
             
    if count==0:
        print("solved 0 puzzles")
    else:
        print("solved", count, "puzzles")
        print("average:", num_moves/count, "moves", num_tested/count, "states, tested")
        
            
    
        
        
        
       
        
        
        
     