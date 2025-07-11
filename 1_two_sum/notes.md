# Two Sum Solutions

## 1. Brute Force Solution

```python
class Solution(object):
    def twoSum(self, nums, target):
        # Check every pair of indices
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

**Time Complexity:** O(n²)
**Space Complexity:** O(1)

## 2. Slice & Index Solution

```python
class Solution(object):
    def twoSum(self, nums, target):
        for ind, num in enumerate(nums):
            two = target - num
            # look only in the sublist after the current index
            if two in nums[ind + 1:]:
                ind_two = nums[ind + 1:].index(two)
                return [ind, ind + 1 + ind_two]
        return []
```

**Time Complexity:** O(n²)
**Space Complexity:** O(n)
(creates a slice of size up to n in each iteration)

## 3. Hash Map Solution

```python
class Solution(object):
    def twoSum(self, nums, target):
        previous_map = {}
        for ind, num in enumerate(nums):
            diff = target - num
            if diff in previous_map:
                return [previous_map[diff], ind]
            previous_map[num] = ind
```

**Time Complexity:** O(n) on average
**Space Complexity:** O(n)
(stores up to n elements in the hash map)
