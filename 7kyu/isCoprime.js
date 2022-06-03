// https://www.codewars.com/kata/585c50e75d0930e6a7000336

const isCoprime = (x,y) => [...Array(x+1).keys()]
                                .filter(n=>x%n==0)
                                .filter(value=>[...Array(y+1).keys()]
                                .filter(n=>y%n==0)
                                .includes(value)) == 1