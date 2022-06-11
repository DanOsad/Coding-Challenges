# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        s = []
        for n in nums:
            r = target - n
            if r in nums[i + 1:]:
                s.append(i)
                s.append(nums.index(r, i+1))
                break
            else:
                i += 1
        return s