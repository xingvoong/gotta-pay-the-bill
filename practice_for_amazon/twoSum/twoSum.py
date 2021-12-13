

# {
#   7: 0
#   2: 1
#   -2: 2
#   -6: 3
# }

def twoSum(nums, target):
  hashmap = {}
  for i in range(len(nums)):
    if nums[i] in hashmap and i != hashmap[nums[i]]:
      return[hashmap[nums[i]], i]
    else:
      complement = target - nums[i]
      hashmap[complement] = i

print(twoSum([3, 2, 4], 6))
