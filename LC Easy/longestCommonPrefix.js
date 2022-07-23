// https://leetcode.com/problems/longest-common-prefix

const longestCommonPrefix = strs => {
    strs.sort((a,b)=>a.length-b.length)
    let r = ''
    for (let i=0; i<strs[0].length; i++) {
      let currentLetter = strs[0].charAt(i)
      if (strs.every(word=>word.charAt(i)==currentLetter)) {
        r += currentLetter
      } else {
        break
      }
    }
    return r
  }