// https://www.codewars.com/kata/5966eeb31b229e44eb00007

const vaporcode = string => {
    return Array.from(string).map(x=>x).filter(letter=>letter !== ' ').map(letter=>letter.toUpperCase()).join('  ')
  }