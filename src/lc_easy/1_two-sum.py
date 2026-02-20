# https://leetcode.com/problems/two-sum/
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pointer_a = 0
        pointer_b = 1
        while pointer_b < len(nums):
            if (target - nums[pointer_a]) == nums[pointer_b]:
                return [pointer_a, pointer_b]
            if pointer_b == len(nums) - 1:
                pointer_a += 1
                pointer_b = pointer_a + 1
            else:
                pointer_b += 1
            

cases = [
    {
        'input': ([2,7,11,15], 9),
        'solution': [0, 1]
    },
    {
        'input': ([3,2,4], 6),
        'solution': [1, 2]
    },
    {
        'input': ([3,3], 6),
        'solution': [0, 1]
    }
]

from tests import TestSuite
test_suite = TestSuite(
    **{
        'testcases': cases,
        'func': Solution().twoSum
    }
)
test_suite.run_tests()