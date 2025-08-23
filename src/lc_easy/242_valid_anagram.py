# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sh = defaultdict(int)
        th = defaultdict(int)

        for c in s: sh[c] += 1
        for c in t: th[c] += 1

        return sh == th