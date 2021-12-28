'''
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.

The same number may be chosen from candidayes an unlimited number of times.  Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

example 1:
input: candidates = [2, 3, 6, 7], target = 7
output: [[2, 2, 3], [7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7.  Not that 2 can be used multiple times.
7 is a candiate, and 7 = 7

example 2:
input: candidates = [2, 3, 5], target = 8
output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

example 3:
input: candidates = [2], target = 1
output: []
'''