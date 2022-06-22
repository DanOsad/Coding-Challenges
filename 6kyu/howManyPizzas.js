// https://www.codewars.com/kata/599bb194b7a047b04d000077

const howManyPizzas = diameter => {
  let pizzaEight = 64
  let pizzaGiven = diameter**2
  let fullPizzas = Math.floor(pizzaGiven/pizzaEight)
  let slices = Math.round((pizzaGiven%pizzaEight)/8)
  return `pizzas: ${fullPizzas}, slices: ${slices}`
}