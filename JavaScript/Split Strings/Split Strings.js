function solution(str) {
  // solving the odd or even problemm
  if (str.length % 2 != 0) {
    str = str.concat('_')
  }
  // spliting the words
  split = []
  for (let i = 1; i < str.length; i += 2) {
    split.push(str[i - 1] + str[i])
  }
  return split
}

console.log(solution('abc'))
