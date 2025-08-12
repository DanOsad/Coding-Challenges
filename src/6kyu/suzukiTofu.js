// https://www.codewars.com/kata/57d4ecb8164a67b97c00003c

function buyTofu(cost,box){
    let value = 0
    let mon = 0
    let monme = 0 
    let numCoinsSpent = 0
    box.split(' ').filter(el => el=='mon' || el=='monme').forEach(el=> {
      if (el=='mon'){
        mon += 1
        value += 1
      } else{
        monme += 1
        value += 60
      }
    })
    let remainingMon = mon
    let remainingMonme = monme
    let remainingCost = cost
    while (remainingCost > 0){
      if (remainingCost / 60 >= 1 && remainingMonme >= 1){
          remainingCost -= 60 
        remainingMonme -= 1
        numCoinsSpent +=1
      }else{
        remainingCost -= 1
        remainingMon -= 1
        numCoinsSpent += 1
      }
    }
    if (value < cost) {
      return 'leaving the market'
    }else if (remainingCost > 0){
      return 'leaving the market'
    }else if (numCoinsSpent > mon + monme){
      return 'leaving the market'
    }else {
    return [mon, monme, value, numCoinsSpent]
    }
  }