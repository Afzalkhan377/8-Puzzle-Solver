#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Afzal Khan
# email:afzal@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name:Jamil Khodr
# partner's email:kjkjamil@bu.edu
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        for r in range(len(self.tiles)):
            for c in range(3):
                self.tiles[r][c]= digitstr[(3*r + c) ]
                if self.tiles[r][c]=='0':
                    self.blank_r=r
                    self.blank_c=c

    ### Add your other method definitions below. ###
    def __repr__(self):
        """ Returns a board in the form of string 
        """
        s=''
        for row in range(len(self.tiles)):
         
           for col in range(len(self.tiles[0])):
               if self.tiles[row][col]=='0':
                   s+="_"+ " "
               else:
                   s += self.tiles[row][col] + " "
           
           s += '\n'  
           
        return s
                
    def move_blank(self, direction):
        """ checks if the blank can be moved in that specific direction and 
        moves the blank in that direction
        """
        
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c]=="0":
                
                    
                  if direction=="left":  
                        if c-1>=0 and c-1<=2:
                            self.tiles[r][c]=self.tiles[r][c-1]
                            self.tiles[r][c-1]="0"
                            self.blank_r=r
                            self.blank_c=c-1
                            return True 
                        else:
                            break
                  elif direction=="right":
                        if c+1>=0 and c+1<=2:
                            self.tiles[r][c]=self.tiles[r][c+1]
                            self.tiles[r][c+1]="0"
                            self.blank_r=r
                            self.blank_c=c+1
                            return True 
                        else:
                            break
                            
                  elif direction=="down":
                         if r+1>=0 and r+1<=2:
                             self.tiles[r][c]=self.tiles[r+1][c]
                             self.tiles[r+1][c]="0"
                             self.blank_r=r+1
                             self.blank_c=c
                             return True 
                         else:
                             break
                             
                  elif direction=="up":
                         if r-1>=0 and r-1<=2:
                            self.tiles[r][c]=self.tiles[r-1][c]
                            self.tiles[r-1][c]="0"
                            self.blank_r=r-1
                            self.blank_c=c
                            return True
                         else:
                            break
                  
        return False
    
    def digit_string(self):
        """ gives a string of number 
        """
        j=""
        for r in range (len(self.tiles)):
            for c in range (len(self.tiles[0])):
                if self.tiles[r][c]=="_":
                    j+="0"
                else:
                    j+=self.tiles[r][c]
        return j
                
   
    
    def copy(self):
        
        
        """ copy(grid) that creates and returns a deep copy of grid–a new,
        separate 2-D list that has the same dimensions and cell values as grid."""
        copy=self.digit_string()
        g=Board(copy)            
            
        return g



    def  num_misplaced(self):
        """  num_misplaced(self) that counts and returns the number
        of tiles in the called Board object that are not where they 
        should be in the goal state 
        """
        count=0
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c]!=GOAL_TILES[r][c]:
                    
                    if self.tiles[r][c]!="0":
                        count+=1
                    else:
                        count+=0
        return count
    
    def num_misplaced_row(self):
        """ counts the number of tiles that are in the wrong row 
        """
        count=0
      
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles)):
              
                  if self.tiles[r]!=GOAL_TILES[r]:
                      if self.tiles[r][c] not in GOAL_TILES[r]:
                          if self.tiles[r][c]!='0':
                              count+=1
                    
        return count
    
    def num_misplaced_col(self):
        """ counts the number of misplaced tiles in each column 
        """
        count=0
        bo=[]
        go=[]
        d=[]
        f=[]
        
        for r in range(len(self.tiles)):
          
              
                for c in range(3):
                    bo+=self.tiles[c][r]
                    go+=GOAL_TILES[c][r]
                    if len(bo)==3:
                        d+=[bo]
                        f+=[go]
                        bo=[]
                        go=[]
        for r in range(len(d)):
            for c in range(len(d[0])):
                   
                    if d[r][c] not in f[r]:
                        if d[r][c]!='0':
                            count+=1
        return count
                
               
               
                
        
                                
                                
    
        
    def __eq__(self, other):
        """ __eq__(self, other) that can be called when the ==
        operator is used to compare two Board objects. The method 
        should return True if the called object (self) and the
        argument (other) have the same values for the tiles attribute,
        and False otherwise. 
        """
        ot=other.digit_string()
        real= self.digit_string()
        for r in range(len(real)):
            if ot[r]!=real[r]:
                return False
        return True
            
       
        