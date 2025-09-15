# https://leetcode.com/problems/search-insert-position/
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (hi + lo) // 2
            if target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid
            if hi == lo and nums[mid] == target:
                return mid
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

# from tests import TestSuite
import TestSuite
test_suite = TestSuite(
    **{
        'testcases': cases,
        'func': Solution().searchInsert
    }
)
test_suite.run_tests()