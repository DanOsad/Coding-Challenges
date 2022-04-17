// https://www.codewars.com/kata/539ee3b6757843632d00026b
// Write a function that takes a single string (word) as argument. The function must return an ordered list containing the indexes of all capital letters in the string.

let capitals = function (word) {
    let r = []
    for (i=0; i<word.length; i++){
      if (word.charAt(i) === word.charAt(i).toUpperCase())
        r.push(i)
    }
    return r
  };