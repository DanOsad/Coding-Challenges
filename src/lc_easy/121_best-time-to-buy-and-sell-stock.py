# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        lowest_price = None
        for price in prices:
            if lowest_price is None or price < lowest_price:
                lowest_price = price
            if (price - lowest_price) > max_profit:
                max_profit = price - lowest_price
        return max_profit


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