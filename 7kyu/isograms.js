// https://www.codewars.com/kata/54ba84be607a92aa900000f1

function isIsogram(str) {
    const s = str.toLowerCase().split('').sort();
    console.log(s)
    for (i=0; i<s.length; i++) {
      if (s[i] === s[i+1]) {
            return false;
          }
    }
    return true;
  }