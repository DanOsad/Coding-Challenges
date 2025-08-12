# https://leetcode.com/problems/move-zeroes
# two pointers

class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # NAIVE APPROACH #

        # new_list = []
        # i = 0
        # for n in nums[:]:
        #     if n == 0:
        #         i += 1
        #     else:
        #         new_list.append(nums.pop(i))

        # return new_list + nums

        # OPTIMIZED APPROACH #

        i = -1 # keep track next place to place non-zero element
        j = 0 # looks for non-zero elements 

        while j < len(nums):
            if nums[j] != 0:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            j += 1
        return nums

cases = [
    {
        'input':  [0,1,0,3,12],
        'solution': [1,3,12,0,0]
    },
    {
        'input': [0],
        'solution': [0]
    },
    # {
    #     'input': [[5], 5],
    #     'solution': 0
    # },
    # {
    #     'input': [[2,5], 5],
    #     'solution': 1
    # }
]

def passed():
    return "passed".upper()

def failed():
    return "failed".upper()

def pass_fail(is_correct: bool):
    return passed() if is_correct else failed()

def test():
    for i, case in enumerate(cases, 1):
        answer = Solution().moveZeroes(case['input'])
        is_correct = (answer == case['solution'])
        print(f'{i}) Expected: {case["solution"]} | Answer: {answer} | {pass_fail(is_correct)}')

test() 