"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of non-overlapping intervals that cover all the intervals in the input

Example 1:

input: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
output: [[1, 6], [8, 10], [15, 18]]
Explantation:  since intervals [1, 3] and [2, 6] overlaps, merge them into [1, 6]


Example 2:
Input:
intervals = [[1, 4], [4, 5]]
Output: [[1, 5]]
explanation: intervals [1, 4] and [4, 5] are considered overlapping

Use a queue, if there is an overlap, then pop it out, and add a new one
otherwise just keep going

# think about edge cases
"""


def merge(intervals):

    # sort base on the first element
    intervals.sort(key=lambda x: (x[0], x[1]))
    print(intervals)

    n = len(intervals)
    if n == 1:
        return intervals

    queue = [intervals[0]]
    for i in range(1, n):
        if len(queue) != 0:
            last_interval = queue[-1]
            last_start = last_interval[0]
            last_end = last_interval[1]

            current_start = intervals[i][0]
            current_end = intervals[i][1]

            # check if there is an overlap, need to check for equal case
            if last_start <= current_end and last_end >= current_start:

                # create new overlap
                new_start = min(last_start, current_start)
                new_end = max(last_end, current_end)
                new_interval = [new_start, new_end]

                # remove the old interval, aka the last one
                queue.pop(-1)
                # append the new interval
                queue.append(new_interval)
            else:
                queue.append(intervals[i])

    return queue


# intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

# input2 = [[1,4], [4, 5]]

input3 = [[2, 3], [2, 2], [3, 3], [1, 3], [5, 7], [2, 2], [4, 6]]
example = [[1, 3], [2, 2], [2, 2], [2, 3], [4, 6]]
example2 = [[1, 3], [4, 6], [5, 7]]

# print(merge(intervals))
# print(merge(input2))

# print(merge(input3))
print(merge(example2))

"""
let N be the lengths of intervals
time:
- O(NlogN) for sorting

space:
- O(N)

"""
