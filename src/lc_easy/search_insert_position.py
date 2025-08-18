# https://leetcode.com/problems/search-insert-position

class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo

cases = [
    {            
        'input': [[1,3,5,6], 5],
        'solution': 2
    },
    {
        'input': [[1,3,5,6], 2],
        'solution': 1
    },
    {
        'input': [[1,3,5,6], 7],
        'solution': 4
    }
]

from tests import TestSuite
test_suite = TestSuite(
    **{
        'testcases': cases,
        'func': Solution().searchInsert
    }
)

test_suite.run_tests()