// https://leetcode.com/problems/remove-element

const removeElement = (nums, val) => {
    let j = 0
    for (let i=0; i<nums.length; i++) {
      if (nums[i] == val) {
        nums.splice(i, 1)
        i--
      }
    }
    return nums.length
  }