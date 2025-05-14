#!/bin/python3
# only submitted on the hacker rank
import math
import os
import random
import re
import sys


#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#
def getLocation(r_q, c_q, obstacle):
    if obstacle[0] < r_q and obstacle[1] == c_q:
        return 'D'
    if obstacle[0] > r_q and obstacle[1] == c_q:
        return 'U'
    if obstacle[0] == r_q and obstacle[1] < c_q:
        return 'L'
    if obstacle[0] == r_q and obstacle[1] > c_q:
        return 'R'
    if abs(r_q - obstacle[0]) == abs(c_q - obstacle[1]):
        if obstacle[0] > r_q and obstacle[1] > c_q:
            return 'UR'
        if obstacle[0] < r_q and obstacle[1] > c_q:
            return 'DR'
        if obstacle[0] < r_q and obstacle[1] < c_q:
            return 'DL'
        if obstacle[0] > r_q and obstacle[1] < c_q:
            return 'UL'


def getCellsBlkbyObst(n, r_q, c_q, obstacles):
    blocked_cell = set()

    for obstacle in obstacles:
        x = obstacle[0]
        y = obstacle[1]
        direction = getLocation(r_q, c_q, obstacle)

        if direction == 'U':
            for i in range(x, n + 1):
                blocked_cell.add((i, c_q))
        if direction == 'R':
            for i in range(y, n + 1):
                blocked_cell.add((r_q, i))
        if direction == 'L':
            for i in range(y, 0, -1):
                blocked_cell.add((r_q, i))
        if direction == 'D':
            for i in range(x, 0, -1):
                blocked_cell.add((i, c_q))

        if direction == 'UR':
            while x <= n and y <= n:
                blocked_cell.add((x, y))
                x += 1
                y += 1
        if direction == "UL":
            while x <= n and y >= 1:
                blocked_cell.add((x, y))
                y -= 1
                x += 1
        if direction == "DL":
            while y >= 1 and x >= 1:
                blocked_cell.add((x, y))
                x -= 1
                y -= 1
        if direction == "DR":
            while y <= n and x >= 1:
                blocked_cell.add((x, y))
                x -= 1
                y += 1
        else:
            pass

    return blocked_cell


def cellsQueenCanAttack(n, k, r_q, c_q):
    orthagonal = 2 * n - 2
    diagonal = 2 * n - 2 - abs(r_q - c_q) - abs(r_q + c_q - n - 1)
    return orthagonal + diagonal


def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    if len(obstacles) == 0:
        return cellsQueenCanAttack(n, k, r_q, c_q)
    else:
        return cellsQueenCanAttack(n, k, r_q, c_q) - len(getCellsBlkbyObst(n, r_q, c_q, obstacles))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
