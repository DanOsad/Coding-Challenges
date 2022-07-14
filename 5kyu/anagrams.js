// https://www.codewars.com/kata/523a86aa4230ebb5420001e1

const anagrams = (str,arr) => {
    const strSorted = str.split('').sort().join('')
    return arr.filter(word=>word.split('').sort().join('') == strSorted)
}