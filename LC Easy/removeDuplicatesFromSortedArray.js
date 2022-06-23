// https://leetcode.com/problems/remove-duplicates-from-sorted-array/

const removeDuplicates = nums => {
    for (let i=1; i<nums.length; i++) {
      if (nums[i]==nums[i-1]) {
        nums.splice(i, 1)
      }
    return nums.length
    }
  }