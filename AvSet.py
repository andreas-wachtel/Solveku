
class AvSet(set):       
        
    def myDiscard( self, value ):
        """removes value if present and returns True only if value was present."""
        return self.discard2(value)
        #return self.discard3(value)
        
    def copy(self):
        """Need to construct a new set of this type."""
        return AvSet( self )
    
    def discard2(self, value):
        lenB = len(self)
        self.discard(value)
        return len(self) < lenB
    
    def discard3(self, value):
        if value in self:
            self.remove(value)
            return True
        return False
    
    
    def __int__(self):
        assert(len(self) == 1), 'there must not be more than 1 element in the set'
        return int(next(iter(self)))

    
    @classmethod
    def setGlobalMap(cls, n=9):
        pass
    
    
    @classmethod
    def getFullAvailableSet(cls, n=9):
        return AvSet( range(1,n+1) )
