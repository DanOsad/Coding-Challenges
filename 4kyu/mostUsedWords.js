// https://www.codewars.com/kata/51e056fe544cf36c410000fb
// Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the top-3 most occurring words, in descending order of the number of occurrences.

function topThreeWords(text) {
    text = text.replace(/[^\w\s\']/gi, '').split(' ').filter(l=>l!==''&&l!=="'")
    let count = {}
    if (text.length > 0) {
      text.forEach(word=> {
        word = word.toLowerCase()
        if (count[word]) {
          count[word] += 1
          return
        } 
        count[word] = 1
      })
      let toSort = []
      for (let [key,val] of Object.entries(count)) {
        toSort.push([key,val])
        sorted = toSort.sort((a,b)=>b[1]-a[1])
      }
      
      let solve = []
      for (let i=0; i<sorted.length; i++) {
          solve.push(sorted[i][0])
      }
      return solve.slice(0,3)
    } else {
      return text
    }
}

const testCases = [
    [topThreeWords("a a a  b  c c  d d d d  e e e e e"), ['e','d','a']],
    [topThreeWords("a a c b b"), ['a','b','c']],
    [topThreeWords("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"),['e','ddd','aa']],
    [topThreeWords("  //wont won't won't "), ["won't", "wont"]],
    [topThreeWords("  , e   .. "), ["e"]],
    [topThreeWords("  ...  "), []],
    [topThreeWords("  '  "), []],
    [topThreeWords(`In a village of La Mancha, the name of which I have no desire to call to
                    mind, there lived not long since one of those gentlemen that keep a lance
                    in the lance-rack, an old buckler, a lean hack, and a greyhound for
                    coursing. An olla of rather more beef than mutton, a salad on most
                    nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
                    on Sundays, made away with three-quarters of his income.`), ['a','of','on']],
]

function testTopThreeWords(tests){
    tests.forEach(test=>console.log(test[0]===test[1]))
}

testTopThreeWords(testCases)