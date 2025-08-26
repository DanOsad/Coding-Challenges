# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left = 0
        right = 1
        curr_max = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                curr_max = max(curr_max, prices[right] - prices[left])
            else:
                left = right
            right += 1
        return curr_max

cases = [
    {
        'input': [7,1,5,3,6,4],
        'solution': 5
    },
    {
        'input': [7,6,4,3,1],
        'solution': 0
    },
    {
        'input': [2,1,2,1,0,1,2],
        'solution': 2
    }
]

from tests import TestSuite
test_suite = TestSuite(
    **{
        'testcases': cases,
        'func': Solution().maxProfit
    }
)
test_suite.run_tests()