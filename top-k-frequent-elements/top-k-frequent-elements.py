class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 1:
            return nums

        import heapq
        valueMap = {}
        freqMap = {}
        for i in range(len(nums)):
            if nums[i] in valueMap:
                valueMap[nums[i]] += 1
            else:
                valueMap[nums[i]] = 1

  
        return heapq.nlargest(k, valueMap.keys(), key=valueMap.get)