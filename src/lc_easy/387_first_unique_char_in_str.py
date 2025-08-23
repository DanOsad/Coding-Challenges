# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        for i, c in enumerate(s):
            if not c in seen:
                seen[c] = 0
            seen[c] += 1
        
        for i, c in enumerate(s):
            if seen[c] == 1:
                return i
        return -1


cases = [
    {
        'input': "leetcode",
        'solution': 0
    },
    {
        'input': "loveleetcode",
        'solution': 2
    },
    {
        'input': "aabb",
        'solution': -1
    },
]