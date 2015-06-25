"""This code counts the number of paths from the top left 
corner to the bottom right corner in a lattice size 20x20
There are two ways to do this, we could start at the top and explore all the paths to the bottom, or we could start at the bottom and use memoization.

In this code we will use the memoization strategy.

Since we are going backwards, the valid movements are up and left. We will count the number stored in lattice[0][0] in the 
end, and that will be the solution.
"""

import numpy as np

n = 20

lattice = np.zeros((n, n))

def visit(lattice, i, j):
    """When we visit a vertex, increment the vertex counter
    Then look for another vertex."""
    lattice[i][j] += 1
    if(i + 1) < n:
        visit(lattice, i+1, j)
    if(j + 1) < n:
        visit(lattice, i, j+1)
visit(lattice, 0, 0)
print(lattice[n-1][n-1])

 
