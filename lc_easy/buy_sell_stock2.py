# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        lowest_price = None

        for price in prices:
            if lowest_price == None:
                lowest_price = price
                continue
            
            if price < lowest_price:
                lowest_price = price
            
            profit = price - lowest_price
            
            if profit > max_profit:
                max_profit = profit

        return max_profit
    
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
    }
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