// https://www.codewars.com/kata/546f922b54af40e1e90001da

const alphabetPosition = str => {
    const alphabet = 'abcdefghijklmnopqrstuvwxyz'
    let solution = ''
    str.split('')
       .filter(elem => elem.match(/[a-zA-Z]/))
       .map(elem => elem.toLowerCase())
       .forEach(elem => solution += `${alphabet.indexOf(elem)+1} `)
    return solution.trim()
}