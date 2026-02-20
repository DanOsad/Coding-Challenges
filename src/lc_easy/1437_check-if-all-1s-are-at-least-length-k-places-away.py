# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

from typing import List
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        pointer_a = 0
        pointer_b = 1

        while pointer_b < len(nums):
            if nums[pointer_a] == 1:
                if nums[pointer_b] == 1:
                    current_gap = (pointer_b - 1) - pointer_a
                    if current_gap < k:
                        return False
                    pointer_a = pointer_b
                    pointer_b += 1
                else:
                    pointer_b += 1
            else:
                pointer_a += 1
                pointer_b += 1

        return True
        

cases = [
    {
        'input': ([1, 0, 0, 0, 1, 0, 0, 1], 2),
        'solution': True
    },
    {
        'input': ([1, 0, 0, 1, 0, 1], 2),
        'solution': False
    }
]

from tests import TestSuite
test_suite = TestSuite(
    **{
        'testcases': cases,
        'func': Solution().kLengthApart
    }
)
test_suite.run_tests()