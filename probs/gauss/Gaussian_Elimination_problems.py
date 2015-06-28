# version code 021f9affec63+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

from matutil import *
from GF2 import one
import triangular as tg
from vecutil import zero_vec



## 1: (Problem 1) Recognizing Echelon Form
# Write each matrix as a list of row lists
"""

echelon_form_1 = [[   ...   ],
                  [   ...   ],
                  [   ...   ],
                  [   ...   ],
                  [   ...   ]]

echelon_form_2 = [[   ...   ],
                  [   ...   ],
                  [   ...   ],
                  [   ...   ]]

echelon_form_3 = [[   ...   ],
                  [   ...   ],
                  [   ...   ]]

echelon_form_4 = [[   ...   ],
                  [   ...   ],
                  [   ...   ],
                  [   ...   ]]
"""



## 2: (Problem 2) Is it echelon?
def is_echelon(A):
    '''
    Input:
        - A: a list of row lists
    Output:
        - True if A is in echelon form
        - False otherwise
    Examples:
        >>> is_echelon([[9,-1,2],[0,4,5],[0,0,2]])
        True
        >>> is_echelon([[0,4,5],[0,3,0],[0,0,2]])
        False
        >>> is_echelon([[9,10]])
        True
        >>> is_echelon([[5]])
        True
        >>> is_echelon([[1],[1]])
        False
        >>> is_echelon([[0]])
        True
        >>> is_echelon([[0],[1]])
        False
        >>> is_echelon([[1,0,2],[0,0,0],[0,0,-1]])
        False
        >>> is_echelon([[7,1,0],[0,5,0],[0,0,0],[0,0,0]])
        True
    '''
    
    echelon = []
    k = len(A[0])
    bFound  = False;
    for v in reversed(A):
        for i in range(len(v)):
            if (v[i] != 0):
                bFound = True
                k = i
                break

        if (bFound):
            echelon.append(k)

    #print (echelon)
    res =  all ([echelon[i] > echelon[i+1] for i in range(len(echelon) -1 )])
    return res

"""

## 3: (Problem 3) Solving with Echelon Form: No Zero Rows
# Give each answer as a list

echelon_form_vec_a = ...
echelon_form_vec_b = ...
echelon_form_vec_c = ...



## 4: (Problem 4) Solving with Echelon Form
# If a solution exists, give it as a list vector.
# If no solution exists, provide "None" (without the quotes).

solving_with_echelon_form_a = ...
solving_with_echelon_form_b = ...

"""

## 5: (Problem 5) Echelon Solver
def echelon_solve(row_list, label_list, b):
    '''
    Input:
        - row_list: a list of Vecs
        - label_list: a list of labels establishing an order on the domain of
                      Vecs in row_list
        - b: a vector (represented as a list)
    Output:
        - Vec x such that row_list * x is b
    >>> D = {'A','B','C','D','E'}
    >>> U_rows = [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one})]
    >>> b_list = [one,0,one]
    >>> cols = ['A', 'B', 'C', 'D', 'E']
    >>> echelon_solve(U_rows, cols, b_list) == Vec({'B', 'C', 'A', 'D', 'E'},{'B': 0, 'C': one, 'A': one})
    True
    >>> U_rows == [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one})]
    True
    >>> b_list == [one,0,one]
    True
    '''
    """
        v = zero_vec(label_list)
        n = len(label_list) - len(row_list)

        zero_list = [v for i in range(n)]
        row_list = row_list + zero_list

        pass
    """ 
    D = row_list[0].D 
    x = zero_vec(D)
    num_labels = len(label_list)
    for j in reversed(range(len(D))):
        if j > len(row_list)-1: continue
        row = row_list[j]
        if row == zero_vec(D): continue
        # in the row find the label of the column with the first non-zero entry
        for i in range(num_labels):
            if row[label_list[i]] == one: break
        c = label_list[i]
        x[c] = (b[j] - x*row)/row[c]
    return x

    #r = tg.triangular_solve(row_list, label_list, b)
    #print(r)
    #return r

"""
## 6: (Problem 6) Solving General Matrices via Echelon
row_list = [ ... ]    # Provide as a list of Vec instances
label_list = [ ... ] # Provide as a list
b = [ ... ]          # Provide as a list of GF(2) values



## 7: (Problem 7) Nullspace A
null_space_rows_a = {...} # Put the row numbers of M from the PDF



## 8: (Problem 8) Nullspace B
null_space_rows_b = {...} # Put the row numbers of M from the PDF
"""
