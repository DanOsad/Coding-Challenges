// https://leetcode.com/problems/find-first-palindromic-string-in-the-array

const firstPalindrome = arr => {
    for (str in arr) {
      if (arr[str] == arr[str].split('').reverse().join('')) {
        return arr[str]
      }
    }
    return ""
}