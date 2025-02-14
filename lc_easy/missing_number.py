# https://leetcode.com/problems/missing-number/description/
import math
def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l = len(nums)
    s = sorted(nums)
    
    # hi = l
    # lo = s[0]

    # while hi > lo:
    #     m = math.floor(lo + (hi-lo) / 2)

    # p = s[1]
    # print('s=', s)
    # for i in range(l):
    #       if i >= l:
    #             return False
    #       print('p=', p)
    #       print('i=', i, 's[i]=', s[i])
    #       if p != s[i] + 1:
    #             return s[i] + 1
    #       else:
    #             p  += 1
    #             continue
    
    for i in range(l):
          if i > 0:
                curr_num = s[i]
                next_num = s[i] + 1
                # if s[i] != s[i-1] + 1:
                #       return s[i-1] + 1
                if next_num != curr_num + 1:
                      return curr_num + 1
            


nums_list = [
        [3,0,1],
        [0,1],
        [9,6,4,2,3,5,7,0,1]
]

for nums in nums_list:
        print(missingNumber(nums))