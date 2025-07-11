class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
            
        previous_map = {}
        for ind,num in enumerate(nums):
            diff = target-num
            if diff in previous_map:
                return [previous_map[diff], ind]
            previous_map[num] = ind
        return [] #if no solution is found