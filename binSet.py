"""
Binary set implementation by
Andreas Wachtel (Ph.D. since 7. Jan. 2016)
Last change: 18.12.2022
"""

class binSet:

    def __init__(self, n=0):
        """Construct available set of  n  elements."""
        self._set = (1 << n) -1    # same as int(2**n-1)
        self.length = n


    def __len__(self):
        return self.length


    @classmethod
    def getFullAvailableSet(cls, n=9):
        return binSet(n)


    def remove(self, omega):
        """Remove element."""
        self.myDiscard(omega)


    def myDiscard(self, omega):
        """remove element and say whether it was present"""
        if self._set > 0:                    # could be length > 0
            oldset = self._set
            self._set &= ~(1 << (omega-1))   # bit AND
            res = self._set < oldset
            if res:
                self.length -= 1
        return res


    def __int__(self):
        assert(self.length == 1), 'there must not be more than 1 element in the set'
        return bin2omega[self._set]


    def add(self, omega):
        """set bit (value-1 = position) to one."""
        oldset = self._set
        self._set |= (1 << (omega-1))   # bit OR
        if self._set > oldset:
            self.length += 1


    def copy(self):
        deep_copy = binSet()
        deep_copy._set = self._set
        deep_copy.length = self.length
        return deep_copy


    def __contains__(self, omega):
        """provide:  if value in binSet"""
        return (self._set & (1 << (omega-1))) > 0
    
    
    #def union(self, other):
    #    deep_copy = binSet( n=self.n )
    #    deep_copy._set = self._set | other._set
    #    deep_copy.length = deep_copy.countBits()
    #    return deep_copy

    
    def countBits(self):
        a = self._set
        res = 0
        while a > 0:
            lsb = a & (~a+1)
            a -= lsb
            res += 1
        return res

    
    # -----------------------------------------------------------------------------------
    # ----------------------- iterators and print methods -------------------------------
    # -----------------------------------------------------------------------------------
    @classmethod
    def setGlobalMap(cls, n=9):
        global bin2omega
        if 'bin2omega' not in globals():
            bin2omega = {}
            for i in range(1,n+1):
                bin2omega[1<<(i-1)] = i


    def getList( self ):
        """Convert to list."""
        # requires the global map: bin2omega
        global bin2omega
        a = self._set
        _list = []
        while a > 0:
            lsb = a & (~a+1)
            _list.append( bin2omega[lsb] )
            a -= lsb
        return _list


    def __iter__(self):
        """provide:  for x in binSet"""
        return iter( self.getList() )


    def __set__(self):
        """provide:  set(binSet)"""
        return set( self.getList() )

    
    def __str__(self):
        """needs  __iter__"""
        res = 'set {'
        for ome in self:
            res += str(ome)
        res += '}'
        return res
