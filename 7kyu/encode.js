// https://www.codewars.com/kata/592e830e043b99888600002d

const encode = (str, key) => {
    const alphabet = "abcdefghijklmnopqrstuvwxyz"
    let codeList = {}
    for (let i=0; i<alphabet.length; i++) {
      codeList[alphabet[i]] = i+1
    }
    let final = []
    str = str.split('')
    key = key.toString().split('')
    let keyIndex = 0
    for (let i=0; i<str.length; i++) {
      if (keyIndex < key.length) {
        final.push(codeList[str[i]] + +key[keyIndex])
      } else {
        keyIndex = 0
        final.push(codeList[str[i]] + +key[keyIndex])
      }  
      keyIndex++
    }
    return final
}