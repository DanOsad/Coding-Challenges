// Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.

function isValidIP(str){
    let r = str.split('.')
    return r.length == 4 
    && r.every(n=>+n<=255 && +n>=0) 
    && !r.some(n=>n.charAt(0)=='0' && n.length>1)
    && r.every(n=>n==n.trim())
    && !r.some(n=>n.includes('e'))
    && !r.some(n=>n=='')
      ? true : false
  }

const testCases = [
    [isValidIP("0.0.0.0"), true],
    [isValidIP("12.255.56.1"), true],
    [isValidIP("137.255.156.100"), true],
    [isValidIP(''), false],
    [isValidIP('abc.def.ghi.jkl'), false],
    [isValidIP('123.456.789.0'), false],
    [isValidIP('12.34.56'), false],
    [isValidIP('01.02.03.04'), false],
    [isValidIP('256.1.2.3'), false],
    [isValidIP('1.2.3.4.5'), false],
    [isValidIP('123,45,67,89'), false],
    [isValidIP('1e0.1e1.1e2.2e2'), false],
    [isValidIP(' 1.2.3.4'), false],
    [isValidIP('1.2.3.4 '), false],
    [isValidIP('12.34.56.-7'), false],
    [isValidIP('1.2.3.4\n'), false],
    [isValidIP('\n1.2.3.4'), false],
]

function testIsValidIP(tests){
    tests.forEach(test=>console.log(tests[0] === tests[1]))
}

testIsValidIP(testCases)