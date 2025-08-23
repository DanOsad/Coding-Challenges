# https://leetcode.com/problems/rotate-array

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find total number of rotations to do (minus full rotations)
        k = k % len(nums)

        for i in range(1,k):
            nums.insert(i-1, nums.pop(-i))

        # return nums[-k:] + nums[:-k]

cases = [
    {
        'input': ([1,2,3,4,5,6,7], 3),
        'solution': [5,6,7,1,2,3,4]
    },
    {
        'input': ([-1,-100,3,99], 2),
        'solution': [3,99,-1,-100]
    },

]

from tests import TestSuite
test_suite = TestSuite(
    **{
        'testcases': cases,
        'func': Solution().rotate
    }
)

test_suite.run_tests()