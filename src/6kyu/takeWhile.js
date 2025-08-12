// https://www.codewars.com/kata/54f9173aa58bce9031001548

const takeWhile = (arr, pred) => {
    return arr.map(n=>pred(n)).indexOf(false) == -1 ? arr
    : arr.slice(0,arr.map(n=>pred(n)).indexOf(false))
}