// https://www.codewars.com/kata/58279e13c983ca4a2a00002a

const greetDevelopers = list => {
    list.forEach(x=>x.greeting = `Hi ${x.firstName}, what do you like the most about ${x.language}?`)
    return list
  }