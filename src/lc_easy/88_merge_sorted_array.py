# https://leetcode.com/problems/merge-sorted-array

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # there is enough space in nums1 to fit nums2, and it's sorted; start from the back
        # i = (len(nums1) - n) - 1
        # j = len(nums2) - 1
        # insert_at = len(nums1) - 1 if len(nums1) else 1

        # while insert_at > 0 and len(nums2):
        #     if nums2[j] > nums1[i] and nums2[j] > 0:
        #         nums1[insert_at] = nums2[j]
        #         j -= 1
        #         insert_at -= 1
        #     elif nums1[i] >= nums2[j] and nums1[i] > 0:
        #         nums1[insert_at] = nums1[i]
        #         i -= 1
        #         insert_at -= 1

        # return nums1

        last = (m + n) - 1
        # m = m - 1
        # n = n - 1

        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1

        # edge case where there are leftover elements in nums2 (i.e. - nums2 has lower values than start of nums1)
        while n > 0:
            nums1[last] = nums2[n-1]
            n -= 1
            last -= 1

        return nums1



cases = [
    {
        'input': ([1,2,3,0,0,0], 3, [2,5,6], 3),
        'output': [1,2,2,3,5,6]
    },
    {
        'input': ([1], 1, [], 0),
        'output': [1]
    },
    {
        'input': ([0], 0, [1], 1),
        'output': [1]
    }
]

for case in cases:
    input = case['input']
    output = case['output']
    nums1, m, nums2, n = input
    res = Solution().merge(nums1, m, nums2, n)
    if res == output:
        print('PASS')
    else:
        print('FAIL')
    