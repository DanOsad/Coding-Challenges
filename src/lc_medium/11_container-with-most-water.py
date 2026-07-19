# https://leetcode.com/problems/container-with-most-water/
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            length = right - left
            width = min(height[left], height[right])
            area = length * width
            max_area = max(area, max_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

cases = [
    {
        'input': [1, 8, 6, 2, 5, 4, 8, 3, 7],
        'solution': 49
    },
    {
        'input': [1, 1],
        'solution': 1
    },
    {
        'input': [8,7,2,1],
        'solution': 7
    }
]

from tests import TestSuite
test_suite = TestSuite(
    **{
        'testcases': cases,
        'func': Solution().maxArea
    }
)
test_suite.run_tests()