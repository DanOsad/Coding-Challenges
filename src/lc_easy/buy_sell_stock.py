# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
# dynamic programming - keep track of lowest value and compare each coming day to see if its > already set max_profit

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # OPTIMIZED SOLUTION #
        max_profit = 0
        min_sale_price = None

        for price in prices:
            if min_sale_price == None:
                min_sale_price = price
                continue
            if price < min_sale_price:
                min_sale_price = price
            profit = price - min_sale_price
            if profit > max_profit:
                max_profit = profit
        return max_profit

        # NAIVE SOLUTION #
        # max_payoff = 0
        # for i in range(len(prices)-1):
        #     for j in range(i, len(prices)):
        #         if prices[j] <= prices[i]:
        #             continue
        #         payoff = prices[j] - prices[i]
        #         if payoff > 0:
        #             if not max_payoff:
        #                 max_payoff = payoff
        #             elif payoff > max_payoff:
        #                 max_payoff = payoff
        # return max_payoff

cases = [
    {
        'input':  [7,1,5,3,6,4],
        'solution': 5
    },
    {
        'input': [7,6,4,3,1],
        'solution': 0
    },
    {
        'input': [2,1,2,1,0,1,2],
        'solution': 2
    },
]

def passed():
    return "passed".upper()

def failed():
    return "failed".upper()

def pass_fail(is_correct: bool):
    return passed() if is_correct else failed()

def test():
    for i, case in enumerate(cases, 1):
        answer = Solution().maxProfit(case['input'])
        is_correct = (answer == case['solution'])
        print(f'{i}) Expected: {case["solution"]} | Answer: {answer} | {pass_fail(is_correct)}')

test() 