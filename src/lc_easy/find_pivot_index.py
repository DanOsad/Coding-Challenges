# https://leetcode.com/problems/find-pivot-index

# NAIVE SOLUTION #
class _Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pivot = -1
        left_sum = 0

        for i in range(len(nums)):
            right_sum = sum(nums[i+1:])
            if (i >= 1):
                left_sum = sum(nums[0:i])
            if left_sum == right_sum:
                pivot = i
                break

        return pivot

# OPTIMIZED SOLUTION #
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pivot = -1

        left_sum = 0
        right_sum = sum(nums)

        for i, n in enumerate(nums):
            right_sum -= n
            if left_sum == right_sum:
                pivot = i
                break
            else:
                left_sum += n


        return pivot

cases = [
    {
        'input':  [1,7,3,6,5,6],
        'solution': 3
    },
    {
        'input': [1,2,3],
        'solution': -1
    },
    {
        'input': [2,-1,1],
        'solution': 0
    },
    {
        'input': [-1,-1,0,1,1,0],
        'solution': 5
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
        # print(f'Testing Case {i}')
        answer = Solution().pivotIndex(case['input'])
        is_correct = (answer == case['solution'])
        print(f'{i}) Expected: {case["solution"]} | Answer: {answer} | {pass_fail(is_correct)}')

if __name__ == "__main__":
    test() 