# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # p1 = 0
        # p2 = 1
        # nums_length = len(nums)

        # while p2 < nums_length:
        #     if nums[p1] == nums[p2]:
        #         nums.pop(p2)
        #         nums_length -= 1
        #     else:
        #         p1 += 1
        #         p2 += 1
        # return nums_length
        
        i = 0
        j = 1

        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
                j += 1
        print(nums)
        return i + 1






cases = [
    {
        'input': [1, 1, 2],
        'solution': 2
    },
    {
        'input': [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
        'solution': 5
    }
]

from tests import TestSuite
test_suite = TestSuite(
    **{
        'testcases': cases,
        'func': Solution().removeDuplicates
    }
)
test_suite.run_tests()