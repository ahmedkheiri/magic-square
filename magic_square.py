# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 18:44:54 2024

@author: Ahmed Kheiri
"""

import random
import copy

# Function to calculate the magic constant for an n x n magic square
def M(n):
    """
    Calculate the magic constant for a magic square of size n.
    The magic constant is the sum that each row, column, and diagonal must equal.
    
    Args:
    n (int): Size of the magic square (number of rows/columns).
    
    Returns:
    int: Magic constant.
    """
    return n * (n * n + 1) // 2


# Function to create an initial solution (n x n grid)
def InitialSolution(n):
    """
    Generate an initial solution for the magic square by filling numbers sequentially.
    
    Args:
    n (int): Size of the magic square (number of rows/columns).
    
    Returns:
    list: 2D list representing the initial solution.
    """
    sol = []
    for i in range(n):
        sol.append(list(range(i * n + 1, i * n + n + 1)))
    return sol


# Function to calculate the cost of the solution (how far it is from a magic square)
def Cost(sol):
    """
    Compute the cost of the solution based on how close it is to a magic square.
    
    Args:
    sol (list): 2D list representing the current solution.
    
    Returns:
    int: Cost of the solution (lower is better, 0 is a perfect magic square).
    """
    obj = 0
    n = len(sol)

    # Calculate cost based on row sums
    for i in range(n):
        sumR = sum(sol[i])
        obj += abs(M(n) - sumR)

    # Calculate cost based on column sums
    for i in range(n):
        sumC = sum(sol[j][i] for j in range(n))
        obj += abs(M(n) - sumC)

    # Calculate cost for main diagonal (top-left to bottom-right)
    sumD = sum(sol[i][i] for i in range(n))
    obj += abs(M(n) - sumD)

    # Calculate cost for secondary diagonal (top-right to bottom-left)
    sumD = sum(sol[i][n - 1 - i] for i in range(n))
    obj += abs(M(n) - sumD)

    return obj


# Function to return the number of Low-Level Heuristics (LLHs)
def getNumberOfLLHs():
    """
    Get the number of low-level heuristics (LLHs) available.
    
    Returns:
    int: Number of LLHs.
    """
    return 2


# Low-Level Heuristic 0: Randomly swap two elements
def LLH0(sol):
    """
    Perform a random swap of two elements in the solution (LLH 0).
    
    Args:
    sol (list): 2D list representing the current solution.
    """
    x1 = random.randint(0, len(sol) - 1)
    y1 = random.randint(0, len(sol) - 1)
    x2 = random.randint(0, len(sol) - 1)
    y2 = random.randint(0, len(sol) - 1)
    SwapOperator(sol, x1, y1, x2, y2)


# Low-Level Heuristic 1: Apply LLH0 twice
def LLH1(sol):
    """
    Perform two consecutive random swaps in the solution (LLH 1).
    
    Args:
    sol (list): 2D list representing the current solution.
    """
    LLH0(sol)
    LLH0(sol)


# Apply a specific low-level heuristic based on its index
def applyLLH(h, sol):
    """
    Apply a low-level heuristic (LLH) to the solution.
    
    Args:
    h (int): Index of the heuristic to apply (0 or 1).
    sol (list): 2D list representing the current solution.
    """
    if h == 0:
        LLH0(sol)
    elif h == 1:
        LLH1(sol)


# Simple Random Hyper-Heuristic Search (SRHH) to optimise the magic square solution
def SRHH(sol):
    """
    Perform simple random hyper-heuristic (SRHH) search to optimise the solution.
    
    Args:
    sol (list): 2D list representing the initial solution.
    
    Returns:
    list: Optimised solution.
    """
    prevSol = copy.deepcopy(sol)
    solCost = Cost(sol)

    for i in range(10000):
        h = random.randint(0, getNumberOfLLHs() - 1)
        applyLLH(h, sol)
        solCost_new = Cost(sol)

        if solCost_new <= solCost:
            solCost = solCost_new
            prevSol = copy.deepcopy(sol)  # Accept the new solution
        else:
            sol = copy.deepcopy(prevSol)  # Revert to the previous solution

    return sol


# Hill Climbing algorithm to optimise the magic square solution
def HillClimbing(sol):
    """
    Perform hill climbing search to optimise the solution by random swaps.
    
    Args:
    sol (list): 2D list representing the initial solution.
    
    Returns:
    list: Optimised solution.
    """
    solCost = Cost(sol)

    for i in range(10000):
        x1 = random.randint(0, len(sol) - 1)
        y1 = random.randint(0, len(sol) - 1)
        x2 = random.randint(0, len(sol) - 1)
        y2 = random.randint(0, len(sol) - 1)

        # Perform a swap
        SwapOperator(sol, x1, y1, x2, y2)
        solCost_new = Cost(sol)

        if solCost_new <= solCost:
            solCost = solCost_new  # Accept the new solution
        else:
            # Revert the swap if no improvement
            SwapOperator(sol, x1, y1, x2, y2)

    return sol


# Function to swap two elements in the solution
def SwapOperator(sol, x1, y1, x2, y2):
    """
    Swap two elements in the solution.
    
    Args:
    sol (list): 2D list representing the solution.
    x1, y1, x2, y2 (int): Coordinates of the elements to be swapped.
    """
    temp = sol[x1][y1]
    sol[x1][y1] = sol[x2][y2]
    sol[x2][y2] = temp


# Main execution to test the algorithms
if __name__ == "__main__":
    n = 3  # Size of the magic square

    # Generate the initial solution
    sol = InitialSolution(n)

    # Apply Simple Random Hyper-Heuristic (SRHH) algorithm
    sol = SRHH(sol)
    
    # Uncomment to apply Hill Climbing algorithm
    # sol = HillClimbing(sol)

    # Display the final solution and its cost
    print("Final Solution:")
    print(sol)
    print("Cost of the solution:", Cost(sol))
