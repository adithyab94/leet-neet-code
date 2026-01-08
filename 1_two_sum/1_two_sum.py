class Solution:
    def twoSum(self, nums, target):
        #create a hashmap to store the difference between the target and the current number
        #the key is the difference, the value is the index of the current number
        #if the number is not in the hashmap, add it to the hashmap
        #if the number is in the hashmap, return the index of the current number and the index of the number in the hashmap
        
        hashmap  = {}
        for ind, num in enumerate(nums):
            if num not in hashmap:
                hashmap[target-num]=ind
            else:
                return [hashmap[num], ind]