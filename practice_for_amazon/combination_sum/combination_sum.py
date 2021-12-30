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

I:a list of candidate and a target
O: lists of list that sum up to the target

backtracking parameter:
- remain combo because I decrease the sum everytime
- the combo because by looking at the result, I see that it is a list of lists
- start: slicing because I do not go back to the previous candidate

'''

def combinationSum(candidates, target):

  n = len(candidates)
  result = []

  def backtracking(remain_sum, combo, start):
    if remain_sum == 0:
      # mutation again
      # list is mutable,
      # mutable means that it can change the original version after you pass
      # it into another function
      # combo.pop() will change it
      result.append(list(combo))
      return
    elif remain_sum < 0:
      return
    else:
      # visit the remain candidates:
      for i in range(start, n):
        # place the next candidate
        combo.append(candidates[i])

        # backtrack
        backtracking(remain_sum - candidates[i], combo, i)

        # remove the next candidate
        combo.pop()

  backtracking(target, [], 0)
  return result

input1 = [2,3,6, 7]
target1 = 7

input2 = [2, 3, 5]
target2 = 8

input3 = [2]
target3 = 1


print(combinationSum(input1, target1))
print(combinationSum(input2, target2))
print(combinationSum(input3, target3))
