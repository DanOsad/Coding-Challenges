// https://www.codewars.com/kata/514a024011ea4fb54200004b

const domainName = str => {
    return str.split('/').filter(link=>link.includes('.'))[0].split('.').filter(word=>word !== 'www')[0]
  }