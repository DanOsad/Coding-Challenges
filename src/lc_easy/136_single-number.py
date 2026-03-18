# https://leetcode.com/problems/single-number/
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            print(f'Checking n({n}) XOR res({res}) = {n ^ res}')
            res = res ^ n
        return res

cases = [
    {
        'input': [2, 2, 1],
        'solution': 1
    },
    {
        'input': [4, 1, 2, 1, 2],
        'solution': 4
    },
    {
        'input': [1],
        'solution': 1
    }
]

from tests import TestSuite
test_suite = TestSuite(
    **{
        'testcases': cases,
        'func': Solution().singleNumber
    }
)
test_suite.run_tests()