UNSOLVABLE_LABEL = "Unsolvable puzzle"

#from AvSet import AvSet
from binSet import binSet as AvSet


class Cell:
    def __init__(self, value=0, fixed=False):
        """fixed: cell had a value since the beginning of the puzzle (used for printing)."""
        self.value = value
        self.fixed = fixed
        if fixed:
            self.av_set = None
        else:
            self.av_set = AvSet()
            #self.av_set = set()


    @classmethod
    def getFreeCell(cls, n=9):
        res = Cell()
        res.av_set = AvSet.getFullAvailableSet(n)
        return res


    def has_value(self):
        """Returns if the cell has an associated value."""
        return self.value != 0


    def av_set_remove(self, value):
        """Safe checks and removes a value from an available sets.
        Also checks unsolvable puzzles."""
        res = False
        if not self.has_value():
            res = self.av_set.myDiscard(value)
            if len(self.av_set) == 0:
                raise Exception(UNSOLVABLE_LABEL)
        return res


    def deep_copy(self):
        """Return a deep copy of the cell."""
        deep_copy = Cell()
        deep_copy.value = self.value
        if self.av_set is not None:
            deep_copy.av_set = self.av_set.copy()
        deep_copy.fixed = self.fixed
        return deep_copy

