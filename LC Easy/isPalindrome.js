// https://leetcode.com/problems/valid-palindrome

const isPalindrome = str => {
    let s = str.replace(/[^a-z0-9]/gi, '').toLowerCase().split('')
    return s.join('') == s.reverse().join('')
  }