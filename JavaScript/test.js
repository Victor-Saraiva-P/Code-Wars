// Sum Numbers
function sum(numbers) {
  sum_numbers = 0
  for (let i = 0; i < numbers.length; i++) {
    sum_numbers += numbers[i]
  }
  return sum_numbers
}

sum([1, 5.2, 4, 0, -1])