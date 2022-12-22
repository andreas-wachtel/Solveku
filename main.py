# This is a sample Python script.
from Utils import print_grid, print_av_set
import Sudoku as sudo
import timeit
from Constants import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    number_grid = [[0, 0, 0,    0, 0, 6,    9, 0, 0],
                   [5, 1, 0,    7, 2, 0,    0, 0, 0],
                   [0, 0, 3,    0, 0, 0,    0, 2, 0],

                   [0, 0, 0,    0, 7, 1,    0, 0, 0],
                   [1, 7, 4,    0, 0, 9,    5, 0, 0],
                   [0, 0, 2,    0, 4, 0,    0, 0, 0],

                   [0, 9, 0,    0, 0, 0,    6, 5, 0],
                   [0, 0, 8,    0, 0, 0,    0, 3, 2],
                   [3, 0, 0,    0, 5, 0,    0, 0, 0]]

    start = timeit.default_timer()
    sudoku = sudo.SudokuGrid( 9, number_grid )

    actSTAGES = [1, 2, 3]
    #actSTAGES = [1, 2, 3, 4, 5]
    #actSTAGES = [STAGE_ONE_INDEX]
    sudoku.solve( active_stages = actSTAGES )
    #sudoku.solve()
    stop = timeit.default_timer()
    print((stop-start)*1000, "ms")
    sudoku.print()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
