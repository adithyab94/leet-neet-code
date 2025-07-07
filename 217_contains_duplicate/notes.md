# 217. Contains Duplicate - Interview Notes

## Problem Summary
Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

## Three Approaches

### 1. Brute Force Approach
**Time Complexity:** O(n²)  
**Space Complexity:** O(1)

```python
def containsDuplicate_brute_force(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False
```

**How it works:**
- Compare every element with every other element using nested loops
- Outer loop picks each element, inner loop compares with remaining elements
- Returns `true` as soon as a duplicate is found

**Pros:**
- Minimal space usage (constant space)
- Simple to understand and implement
- No modification to original array

**Cons:**
- Extremely slow for large arrays
- Quadratic time complexity makes it impractical for large inputs

**Best for:** Very small arrays (< 100 elements) or when memory is extremely limited

---

### 2. Sorting Approach
**Time Complexity:** O(n log n)  
**Space Complexity:** O(1) [in-place sorting]

```python
def containsDuplicate_sorting(nums):
    nums.sort()  # In-place sorting
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False
```

**How it works:**
- Sort the array first (duplicates will be adjacent)
- Compare adjacent elements in a single pass
- Return `true` if any adjacent pair is equal

**Pros:**
- Better time complexity than brute force
- Minimal space usage
- Simple logic after sorting

**Cons:**
- Modifies the original array
- Not optimal time complexity
- Sorting overhead

**Best for:** Medium-sized arrays (100-10,000 elements) when you can modify the array and want to balance time/space

---

### 3. Hashset Approach (Optimal)
**Time Complexity:** O(n)  
**Space Complexity:** O(n)

```python
def containsDuplicate_hashset(nums):
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False
```

**How it works:**
- Use a hashset to track seen elements
- For each element, check if it already exists in the set
- If yes, return `true` (duplicate found)
- If no, add it to the set and continue

**Pros:**
- Optimal time complexity (linear)
- Preserves original array
- Simple and readable code
- Early termination when duplicate is found

**Cons:**
- Uses extra space proportional to input size
- Hashset operations have some overhead

**Best for:** Most practical scenarios, especially large arrays (>10,000 elements)

---

## Complexity Comparison Table

| Approach | Time Complexity | Space Complexity | Best Use Case |
|----------|----------------|------------------|---------------|
| Brute Force | O(n²) | O(1) | Very small arrays, memory-critical |
| Sorting | O(n log n) | O(1) | Medium arrays, balanced approach |
| Hashset | O(n) | O(n) | Large arrays, performance-critical |

## Trade-off Analysis

### Time vs Space Trade-off:
- **Brute Force**: Minimum space, maximum time
- **Sorting**: Low space, moderate time  
- **Hashset**: Higher space, minimum time

### Practical Decision Framework:

**Choose Brute Force when:**
- Array size < 100
- Memory is extremely limited
- Interviewer specifically asks for minimal space solution

**Choose Sorting when:**
- Array size 100-10,000
- You can modify the original array
- Want to balance time and space
- Interviewer asks about trade-offs

**Choose Hashset when:**
- Array size > 10,000
- Performance is critical
- Memory is available
- Most practical scenarios

## Interview Tips

### When to Mention Each Approach:
1. **Start with Hashset** - It's the most practical solution
2. **Mention Sorting** - Shows you understand trade-offs
3. **Mention Brute Force** - Shows you can think of simple solutions

### Key Points to Emphasize:
- Hashset provides optimal time complexity
- Sorting is a good middle ground
- Brute force is simple but inefficient
- Consider the input size when choosing approach

### Follow-up Questions to Expect:
- "What if memory is limited?"
- "Can you optimize further?"
- "What if the array is already sorted?"
- "How would you handle very large datasets?"

## Optimizations

### Early Termination:
```python
def containsDuplicate_optimized(nums):
    if len(nums) <= 1:
        return False
    
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False
```

### Memory Optimization (if range is known):
If you know the range of values is small (e.g., 0 to n-1), you could use a boolean array instead of a hashset.

## Common Mistakes to Avoid:
1. Not considering edge cases (empty array, single element)
2. Modifying original array without permission
3. Not explaining trade-offs clearly
4. Choosing brute force for large arrays
5. Not mentioning early termination benefits

## Related Problems:
- [219. Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/)
- [220. Contains Duplicate III](https://leetcode.com/problems/contains-duplicate-iii/)
- [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
