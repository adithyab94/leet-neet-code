# Anagram Checking Techniques


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


UPDATE : 4th method is the best one.
---

## 4. Hash Map (Single Dictionary)

**Idea:** Build a frequency map of characters from `s`, then decrement counts while scanning `t`. If at any point a character is missing or its count drops below zero, `t` is not an anagram. Otherwise, it is.

```python
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Early exit if lengths differ
        if len(s) != len(t):
            return False

        # Build frequency map from s
        char_frequency = {}
        for char in s:
            char_frequency[char] = char_frequency.get(char, 0) + 1

        # Decrement based on t
        for char in t:
            # If char not in map or already used up, not an anagram
            if char_frequency.get(char, 0) == 0:
                return False
            char_frequency[char] -= 1

        return True
```

**Time Complexity:**

* Building map for `s`: O(n)
* Scanning `t`: O(m)
  Overall **O(n + m)**.

**Space Complexity:**

* O(k), where k is the size of the character set present in `s` (≤ n).
* In practice, for fixed alphabets (e.g. lowercase letters), this is O(1).

---

This approach commonly outperforms many submissions on platforms like LeetCode, beating around 80 % in both runtime and memory usage.
