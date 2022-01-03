"""
Given an array nums of distint integers, return all the possible permutations.
You can return the answer in any order

Constraint:
- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10
- All the integers of nums are unique

example 1:
input: nums = [1, 2, 3]
output: [[1,2, 3], [1, 3, 2], [2, 1, 3], [3, 1, 2], [3, 2, 1]]

"""


def permute(nums):

    n = len(nums)
    result = []

    def backtracking(start, combo):
        # if solution:
        # output result
        if len(combo) == n:
            result.append(list(combo))
            # exist out
            return

        # visit all the next candidates
        for i in range(n):
            # place the next candidate
            if nums[i] not in combo:
                combo.append(nums[i])

                # backtracking
                backtracking(0, combo)

                # revert the choice for other exploration
                combo.pop()

    backtracking(0, [])
    return result


print(permute([1, 2, 3]))
print(permute([0, 1]))
print(permute([1]))

"""
let N be the number of candidates in nums

time:
- N for a deep copy
- N!
=> O(NxN!)

space:
- O(N!) since one has to keep O(N!) number of permutation
"""
