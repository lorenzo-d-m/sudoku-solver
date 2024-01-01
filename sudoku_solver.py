"""
Sudoku solver Script

Author Lorenzo M.
Date 1 Jan 2024
Version 0.0.1
"""

import numpy as np


scheme = np.array([
    [0,0,0,0,0,3,0,4,0],
    [6,3,0,9,1,0,0,7,0],
    [0,0,5,2,4,0,1,0,0],
    [9,0,0,0,0,0,7,5,0],
    [0,8,7,0,0,0,9,3,0],
    [0,2,3,0,0,0,0,0,6],
    [0,0,9,0,2,4,3,0,0],
    [0,4,0,0,3,9,0,6,7],
    [0,5,0,7,0,0,0,0,0]
    ])


idxs = np.array([0,1,2,3,4,5,6,7,8])
values = np.array([1,2,3,4,5,6,7,8,9])
ok = np.zeros((9,9), dtype=int)

for n in range(10): # 10 is a trade-off 
    # row strategy
    for i in idxs: # set a row
        for guess in values: # guess a value
            ok = np.zeros((9,9), dtype=int) # re-initialize
            if guess not in scheme[i,:]: # not in row
                for j in idxs: # try in columns
                    if scheme[i,j] == 0: # empty cell
                        if guess not in scheme[3*int(i/3):3*int(i/3)+3,3*int(j/3):3*int(j/3)+3]: # not in sub-scheme
                            if guess not in scheme[:,j]: # not in column
                                ok[i,j] = 1
            if (ok == 1).sum() == 1:
                scheme[ok==1] = guess



    # column strategy
    for j in idxs: # set a column
        for guess in values: # guess a value
            ok = np.zeros((9,9), dtype=int) # re-initialize
            if guess not in scheme[:,j]: # not in column
                for i in idxs: # try in columns
                    if scheme[i,j] == 0: # empty cell
                        if guess not in scheme[3*int(i/3):3*int(i/3)+3,3*int(j/3):3*int(j/3)+3]: # not in sub-scheme
                            if guess not in scheme[i,:]: # not in row
                                ok[i,j] = 1
            if (ok == 1).sum() == 1:
                scheme[ok==1] = guess


print(scheme)
