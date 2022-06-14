// https://leetcode.com/problems/palindrome-number/

const isPalindrome = num => num.toString() == num.toString().split('').reverse().join('')