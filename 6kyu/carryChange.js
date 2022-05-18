// https://www.codewars.com/kata/58dfc0d8ca6895cb4e00005c
// So given a set of coin denominations determine the fewest number of coins required to add up to a given amount.

function coinsNeeded(amount, coinDenomiation){
    let arr = coinDenomiation.sort((a,b)=>b-a)
    let coins = 0
    for (i=0; amount>0; i++){
      let coin = Math.floor(amount/arr[i])
      amount -= coin*arr[i]
      console.log(`${coin} ${arr[i]} cent coin added. Amount remaining: ${amount}`)
      coins+=coin
    }
    return coins
}

const testCases = [
    [coinsNeeded(75, [1,2,5,10,20,50]), 3],
    [coinsNeeded(75, [1,5,10,25]), 3],
    [coinsNeeded(123, [1,2,5,10,20,50]), 5],
    [coinsNeeded(123, [1,5,10,25]), 9],
]

function testCoins(tests){
    tests.forEach(test=>console.log(test[0]===test[1]))
}

testCoins(testCases)