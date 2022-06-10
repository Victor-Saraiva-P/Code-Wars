console.log(find_average([]))

function find_average(array) {
  let avg = 0
  if (array.length == 0) {
    return 0
  }
  for (let i = 0; i < array.length; i++) {
    avg += array[i]
  }
  return avg / array.length
}
