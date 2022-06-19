// https://leetcode.com/problems/detect-capital

const detectCapitalUse = word => {
    if (word == word.toUpperCase()) {
      return true
    } else if (word.charAt(0) == word.charAt(0).toUpperCase() && word.split('').splice(1).join('') == word.split('').splice(1).join('').toLowerCase()) {
      return true
    } else if (word == word.toLowerCase()) {
      return true
    } else {
      return false
    }
  }