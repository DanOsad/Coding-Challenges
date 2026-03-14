# https://leetcode.com/problems/product-of-array-except-self/
from typing import List

class Solution:
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        postfix = 1

        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
            print(res)
            print(prefix)
        
        j = len(nums) - 1
        for i in range(len(nums)):
            res[j] *= postfix
            postfix *= nums[j]
            j -= 1
            print(res)
            print(postfix)

        return res




cases = [
    {
        'input': [1, 2, 3, 4],
        'solution': [24, 12, 8, 6]
    },
    {
        'input': [-1, 1, 0, -3, 3],
        'solution': [0, 0, 9, 0, 0]
    }
]

from tests import TestSuite
test_suite = TestSuite(
    **{
        'testcases': cases,
        'func': Solution().productExceptSelf
    }
)
test_suite.run_tests()