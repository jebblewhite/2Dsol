
class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self): 
        """
        Method to print a string representation of a vector 
        """
        return "[" + str(self.x) + ", " + str(self.y) + "]"
