#https://leetcode.com/problems/kth-distinct-string-in-an-array

import math

class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        item_map = { i: 0 for i in arr }
        for i in range(len(arr)):
            item_map[arr[i]] += 1
        solution = [ k for k,v in item_map.items() if v == 1 ]
        return "" if k - 1 > len(solution) else solution[k - 1]

cases = [
    {
        'name': 'case1',
        'arr': ["d","b","c","b","c","a"],
        'k': 2,
        'solution': "a"
    },
    {
        'name': 'case2',
        'arr': ["aaa","aa","a"],
        'k': 1,
        'solution': "aaa"
    },
    {
        'name': 'case3',
        'arr': ["a","b","a"],
        'k': 3,
        'solution': ""
    },
]

def test():
    for case in cases:
        print(f'Testing {case["name"]}')
        s = Solution()
        answer = s.kthDistinct(case['arr'], case['k'])
        is_correct = answer == case['solution']
        print(f'Expected {case["solution"]}, got {answer} = {is_correct}')

test()

"""
Example 1:

Input: arr = ["d","b","c","b","c","a"], k = 2
Output: "a"
Explanation:
The only distinct strings in arr are "d" and "a".
"d" appears 1st, so it is the 1st distinct string.
"a" appears 2nd, so it is the 2nd distinct string.
Since k == 2, "a" is returned. 
Example 2:

Input: arr = ["aaa","aa","a"], k = 1
Output: "aaa"
Explanation:
All strings in arr are distinct, so the 1st string "aaa" is returned.
Example 3:

Input: arr = ["a","b","a"], k = 3
Output: ""
Explanation:
The only distinct string is "b". Since there are fewer than 3 distinct strings, we return an empty string "".
"""