// https://leetcode.com/problems/remove-duplicates-from-sorted-array/

const removeDuplicates = nums => {
    let j = 1
    for (let i=1; i<nums.length; i++) {
      if (nums[i] != nums[i-1]) {
        nums[j] = nums[i]
        j++
      }
    }
    return j
  }