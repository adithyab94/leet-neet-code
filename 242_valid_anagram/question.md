# 242. Valid Anagram

## Problem Description

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Examples

### Example 1:
**Input:** `s = "anagram"`, `t = "nagaram"`  
**Output:** `true`

### Example 2:
**Input:** `s = "rat"`, `t = "car"`  
**Output:** `false`

## Follow-up
What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

## Constraints

- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

## Notes

- An anagram must use all the original letters exactly once
- The order of characters doesn't matter
- Case sensitivity matters (lowercase vs uppercase are different)
- Empty strings are considered anagrams of each other
