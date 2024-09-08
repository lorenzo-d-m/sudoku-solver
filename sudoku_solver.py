"""
Sudoku solver Script

Author Lorenzo M.
Date 1 Jan 2024
Version 0.0.2
"""

import numpy as np
import random

# given scheme. Zeros are empty cells

# example of easy scheme
# scheme = np.array([
#     [0,0,0,0,0,3,0,4,0],
#     [6,3,0,9,1,0,0,7,0],
#     [0,0,5,2,4,0,1,0,0],
#     [9,0,0,0,0,0,7,5,0],
#     [0,8,7,0,0,0,9,3,0],
#     [0,2,3,0,0,0,0,0,6],
#     [0,0,9,0,2,4,3,0,0],
#     [0,4,0,0,3,9,0,6,7],
#     [0,5,0,7,0,0,0,0,0]
#     ])

# example of hard scheme
scheme = np.array([
    [2,7,0,5,0,0,0,0,1],
    [0,0,3,0,9,0,0,0,7],
    [0,0,6,8,0,0,2,4,0],
    [0,0,0,0,0,0,9,0,6],
    [0,2,0,0,0,0,0,5,0],
    [9,0,1,0,0,0,0,0,0],
    [0,8,2,0,0,4,6,0,0],
    [3,0,0,0,8,0,4,0,0],
    [7,0,0,0,0,5,0,8,2]
    ])


def solver(scheme):
    idxs = np.array([0,1,2,3,4,5,6,7,8])
    values = np.array([1,2,3,4,5,6,7,8,9])
    ok = np.zeros((9,9), dtype=int)

    for n in range(10): # 10 is a trade-off 
        # row strategy
        for i in idxs: # set a row
            for v in values: # set a value
                ok = np.zeros((9,9), dtype=int) # re-initialize
                if v not in scheme[i,:]: # not in row
                    for j in idxs: # try in columns
                        if scheme[i,j] == 0: # empty cell
                            if v not in scheme[3*int(i/3):3*int(i/3)+3,3*int(j/3):3*int(j/3)+3]: # not in sub-scheme
                                if v not in scheme[:,j]: # not in column
                                    ok[i,j] = 1
                if (ok == 1).sum() == 1:
                    scheme[ok==1] = v

        # column strategy
        for j in idxs: # set a column
            for v in values: # guess a value
                ok = np.zeros((9,9), dtype=int) # re-initialize
                if v not in scheme[:,j]: # not in column
                    for i in idxs: # try in columns
                        if scheme[i,j] == 0: # empty cell
                            if v not in scheme[3*int(i/3):3*int(i/3)+3,3*int(j/3):3*int(j/3)+3]: # not in sub-scheme
                                if v not in scheme[i,:]: # not in row
                                    ok[i,j] = 1
                if (ok == 1).sum() == 1:
                    scheme[ok==1] = v
    

    # check correctness
    correct = False
    proof = np.unique(scheme, return_counts=True)
    if len(proof[0]) == 9 and len(proof[1]) == 9:
        if (proof[0] == values).all() and (proof[1] == np.array([9,9,9,9,9,9,9,9,9])).all():
            correct = True

    return (correct, scheme)



def guess(scheme):
    backup_scheme = np.copy(scheme)
    
    for _ in range(10): # 10 is a trade-off 
        # initialize
        guess_i = random.randint(0,8)
        guess_j = random.randint(0,8)
        values = np.array([1,2,3,4,5,6,7,8,9])
        
        # get random indices
        while scheme[guess_i,guess_j] != 0:
            guess_i = random.randint(0,8)
            guess_j = random.randint(0,8)
        
        # try values in the selected cell
        for v in values:
            if v not in scheme[guess_i,:]: # not in row
                if v not in scheme[3*int(guess_i/3):3*int(guess_i/3)+3,3*int(guess_j/3):3*int(guess_j/3)+3]: # not in sub-scheme
                    if v not in scheme[:,guess_j]: # not in column
                        scheme[guess_i,guess_j] = v
                        solved, solution = solver(scheme)
                        if solved: # the random value is right
                            return solution
                        else: # re-initialize the scheme
                            scheme = np.copy(backup_scheme)

    return False


if __name__ == '__main__':
    solved, deterministic_solution = solver(scheme)
    if solved:
        print("It was a piece of cake!")
        print(deterministic_solution)
    else:
        solution = guess(deterministic_solution)
        print("It was an hard work!")
        print(solution)
