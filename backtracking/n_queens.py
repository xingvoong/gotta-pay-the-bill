'''
1. hard, back tracking

2. problem statement

3. solution in plain English/ pseudocode
this is a classic backtracking algorithm.
I found there are a lot of good sources for explaning it.
1: https://leetcode.com/problems/n-queens-ii/solution/
2: https://www.youtube.com/watch?v=wGbuCyNpxIg&t=331s

Alg:
    1: iterate over all rows.  When we at the last row,
    we should explore all the solution

    2: on second iteration, we iterate over each column, along the current row,
    with (row, col), we can decide whether to place a queen on that cell.

    3: before placing a queen, we need to check whether it is in attack zone.

    4: when placing a queen, we can mark the attack zone of that queen

    5: when backtrack, remove a queen.

4. implementation
I will implement this in 2 ways.
1: easy to understand way
2: backtracking template that helps with other backtracking problems
'''


class Solution1(object):

    def totalNQueens(self, n):
        """
            :type n: int
            :rtype: int
        """
        self.count = 0

        def helper(row=0, dales=set(), hills=set(), columns=set()):
            # if we can iterate through all row
            # means we can place a queen at the last row
            if row == n:
                self.count += 1
            for col in range(n):
                # if a cell is not in the attacking zone
                # place a queen on that cell
                if row - col not in dales and row + col not in hills \
                        and col not in columns:
                    helper(row + 1, dales.union({row - col}),
                           hills.union({row + col}), columns.union({col}))

        helper()

        return self.count


class Solution2(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def attack_zone(row, col):
            return self.rows[col] or self.hills[row + col] \
                    or self.dales[row - col]

        def place_queen(row, col):
            self.rows[col] = 1
            self.hills[row + col] = 1
            self.dales[row - col] = 1

        def remove_queen(row, col):
            self.rows[col] = 0
            self.hills[row + col] = 0
            self.dales[row - col] = 0

        def backtrack(row=0, count=0):
            for col in range(n):
                if not attack_zone(row, col):
                    place_queen(row, col)
                    if row == n - 1:
                        count += 1
                    else:
                        count = backtrack(row+1, count)
                    remove_queen(row, col)
            return count

        self.rows = [0] * n
        self.hills = [0] * (2*n + 1)
        self.dales = [0] * (2*n + 1)
        return backtrack()


test = Solution1()
assert test.totalNQueens(5) == 10
assert test.totalNQueens(4) == 2

test2 = Solution2()
assert test2.totalNQueens(5) == 10
assert test.totalNQueens(4) == 2

'''
5. complexity analysis:
time: O(N!)
N! ways to put the first queen
Nx(N-3) ways to put the second queen, subtract 1 row, 1 column and
Nx(N-3)x(N6) ways to put the third queen
space: O(N)
to store the rows, hills and dales
'''
