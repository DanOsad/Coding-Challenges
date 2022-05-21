// https://www.codewars.com/kata/52449b062fb80683ec000024

const generateHashtag = str => {
    let x = str.trim().split('').filter(e=>e!==' ')
    return x.length == 0 ? false
    : x.length >= 140 ? false
    : '#' + str.trim().split(' ').filter(e=>e!=='').map(word=>word[0].toUpperCase()+word.substring(1)).join('')
}