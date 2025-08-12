// https://www.codewars.com/kata/52774a314c2333f0a7000688

// PREP
// Parameters: 

// Return: boolean

// Example: 
    // "()"              =>  true
    // ")(()))"          =>  false
    // "("               =>  false
    // "(())((()())())"  =>  true

// Pseudocode:
    // loop through input
        // if input is opening bracket, push to stack
        // if input is closing bracket, pop from stack
    // check stack.length, should be empty if valid

// Implementation:
const validParentheses = parens => {
    let stack = []
    for(let i = 0; i < parens.length; i++){
        if (parens[i] == '('){
            stack.push(parens[i])
            continue
        }
        if (stack.length == 0){ return false }
        if (parens[i] == ')'){
            stack.pop()
        }
    }
    return (stack.length == 0)
}

// Tests:
console.log(validParentheses("()"))
console.log(validParentheses(")(()))"))
console.log(validParentheses("("))
console.log(validParentheses("(())((()())())"))