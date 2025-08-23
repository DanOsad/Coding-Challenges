# https://leetcode.com/problems/intersection-of-two-arrays/description/

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        n1 = set(nums1)
        n2 = set(nums2)
        res = []
        for n in n1:
            if n in n2:
                res.append(n)

        return res


cases = [
    {
        'input': [[1,2,2,1], [2,2]],
        'solution': [2]
    },
    {
        'input': [[4,9,5], [9,4,9,8,4]],
        'solution': [9,4]
    },
]

for case in cases:
    input = case['input']
    solution = case['solution']
    # nums1, m, nums2, n = input
    res = Solution().intersection(*input)
    if res == solution:
        print('PASS')
    else:
        print('FAIL')