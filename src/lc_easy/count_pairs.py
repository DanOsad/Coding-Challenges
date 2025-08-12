# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target

def countPairs(nums, target) -> int:
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    pairs = []

    # condition -> (0, 1) since 0 < 1 and nums[0] + nums[1] = 0 < target
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            if i < j and nums[i] + nums[j] < target:
                pairs.append([i,j])

    return len(pairs)

def countPairsOptimized(nums, target):

    nums.sort()
    count = 0
    left = 0
    right = len(nums) - 1

    while right > left:
        if nums[left] + nums[right] < target:
            count += (right-left)
            left += 1
        else:
            right -= 1
    
    return count


nums_list = {
    2: [-1,1,2,3,1],
    -2: [-6,2,5,-2,-7,-1,3]
}

for target, nums in nums_list.items():
    solution = countPairsOptimized(nums, target)
    print(solution)