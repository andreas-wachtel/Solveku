"""
Binary set implementation by
Andreas Wachtel (Ph.D. since 7. Jan. 2016)
Last change: 18.12.2022
"""

class binSet:
    def __init__(self, n=9):
        # constructor gives complete available set (n elements)
        self._set = int(2**n-1)
        self.length = n
        self.n = n
        self.setGlobalMap(n)


    def remove(self, value):
        # set bit (value-1 = position) to zero
        if self.length > 0:
            oldset = self._set
            self._set &= ~(1 << (value-1))   # bit AND
            if oldset > self._set:
                self.length -= 1
        return self


    def __len__(self):
        return self.length

    
    def copy(self):
        deep_copy = binSet( n=self.n )
        deep_copy._set = self._set
        deep_copy.length = self.length
        return deep_copy


    #def union(self, other):
    #    deep_copy = binSet( n=self.n )
    #    deep_copy._set = self._set | other._set
    #    deep_copy.length = deep_copy.countBits()
    #    return deep_copy
    

    @staticmethod
    def setGlobalMap(n):
        global bin2omega
        if 'bin2omega' not in globals():
            bin2omega = {}
            for i in range(1,n+1):
                bin2omega[1<<(i-1)] = i

    
    def __iter__(self):
        # requires the global map: bin2omega
        global bin2omega
        a = self._set
        _list = []
        while a > 0:
            lsb = a & (~a+1)
            _list.append( bin2omega[lsb] )
            a -= lsb
        return iter(_list)

    
    def __str__(self):
        res = 'set {'
        for ome in self:
            res += str(ome)
        res += '}'
        return res

    
    def countBits(self):
        a = self._set
        res = 0
        while a > 0:
            lsb = a & (~a+1)
            a -= lsb
            res += 1
        return res

