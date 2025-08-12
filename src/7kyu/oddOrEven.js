// https://www.codewars.com/kata/5949481f86420f59480000e7

function oddOrEven(arr) {
    let j = 0
    for (i=0;i<arr.length;i++) {
        j += arr[i];
         }
    if (j%2==0) {
        return "even"
    } else {
      return "odd"
    }
}