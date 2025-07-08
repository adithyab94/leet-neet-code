````markdown
# Anagram Checking Techniques

This document covers three common approaches to determine if two strings `s` and `t` are anagrams of each other.

---

## 1. Sorting

**Idea:** Sort both strings and compare the results. If they are identical, `t` is an anagram of `s`.

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Early exit if lengths differ
        if len(s) != len(t):
            return False
        # Compare sorted strings
        return sorted(s) == sorted(t)
````

**Time Complexity:**

* Sorting `s`: O(n log n)
* Sorting `t`: O(m log m)

Overall: **O(n log n + m log m)**

**Space Complexity:**

* Depends on sorting algorithm:

  * In-place sort: O(1)
  * Not in-place: O(n + m)

Where:

* `n` = length of `s`
* `m` = length of `t`

---

## 2. Hash Map (Using Two Dictionaries)

**Idea:** Count occurrences of each character in both strings using dictionaries, then compare the counts.

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Early exit if lengths differ
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        # Count characters in both strings
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        # Compare the two maps
        return countS == countT
```

**Time Complexity:** O(n + m)

**Space Complexity:** O(1)

* At most 26 keys (for lowercase English letters), so constant extra space.

Where:

* `n` = length of `s`
* `m` = length of `t`

---

## 3. Hash Table (Fixed-Size Array)

**Idea:** Use a fixed-size integer array of length 26 to track the net count of each letter. Increment for `s` and decrement for `t` in a single pass.

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Early exit if lengths differ
        if len(s) != len(t):
            return False

        # Initialize count array for 26 lowercase letters
        count = [0] * 26
        # Update counts in one loop
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        # Check if all counts are zero
        return all(val == 0 for val in count)
```

**Time Complexity:** O(n + m)

**Space Complexity:** O(1)

* Fixed 26-element array.

Where:

* `n` = length of `s`
* `m` = length of `t`

---

Feel free to choose the method that best fits your constraints:

* Use **sorting** for simplicity when performance is not critical.
* Use a **hash map** or **fixed array** for O(n) performance with trade-offs in readability and character set flexibility.

```
```
