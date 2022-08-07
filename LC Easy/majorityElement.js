// https://leetcode.com/problems/majority-element

const majorityElement = nums => {
    let countObject = {}
    nums.forEach(num=>{
      if (!countObject[num]) {
        countObject[num] = 1
      } else {
        countObject[num] += 1
      }
    })
    for (num in countObject) {
      if (countObject[num] > nums.length/2) {
        return +num
      }
    }
}

majorityElement([3,2,3])//3
majorityElement([2,2,1,1,1,2,2])//2