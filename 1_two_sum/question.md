# Two Sum Problem

**Problem Statement:**
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

**Examples:**

1. **Example 1**

   * Input: `nums = [2,7,11,15]`, `target = 9`
   * Output: `[0,1]`
   * Explanation: Because `nums[0] + nums[1] == 9`, we return `[0, 1]`.

2. **Example 2**

   * Input: `nums = [3,2,4]`, `target = 6`
   * Output: `[1,2]`

3. **Example 3**

   * Input: `nums = [3,3]`, `target = 6`
   * Output: `[0,1]`

**Constraints:**

* `2 <= nums.length <= 10^4`
* `-10^9 <= nums[i] <= 10^9`
* `-10^9 <= target <= 10^9`
* Only one valid answer exists.

**Follow-up:** Can you come up with an algorithm that is less than O(n²) time complexity?

---

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
