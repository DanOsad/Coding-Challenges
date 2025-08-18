# https://leetcode.com/problems/missing-number

class Solution:
    def missingNumber(self, nums: list) -> int:
        # set the result to the length of nums (since thats the max number 
        # we can have)
        r = len(nums)

        # for each number in the range, add the number and at the same time 
        # subtract the indexed number from the original list
        for i in range(len(nums)):
            r += (i - nums[i])

        return r

cases = [
    {
        'input': [3,0,1],
        'solution': 2
    },
    {
        'input': [0,1],
        'solution': 2
    },
    {
        'input': [9,6,4,2,3,5,7,0,1],
        'solution': 8
    },
]

from tests import TestSuite
test_suite = TestSuite(
    **{
        'testcases': cases,
        'func': Solution().missingNumber
    }
)

test_suite.run_tests()