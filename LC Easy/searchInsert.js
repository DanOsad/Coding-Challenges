// https://leetcode.com/problems/search-insert-position

const searchInsert = (nums, target) => {
    if (nums.includes(target)) {
        return nums.indexOf(target)
    } else {
        for (let i=0; i<nums.length; i++) {
            if (target<nums[i]) {
                return i
            } else if (i == nums.length-1) {
                return nums.length
            }
        }
    }
}
  
searchInsert([1,3,5,6],5)//2
searchInsert([1,3,5,6],2)//1
searchInsert([1,3,5,6],7)//4