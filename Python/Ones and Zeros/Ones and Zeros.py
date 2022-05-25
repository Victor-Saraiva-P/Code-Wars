def binary_array_to_number(arr):
    num = 0
    lenght = len(arr)
    for i in range(lenght):
        if arr[i] == 1:
            num += 2**(lenght - (i+1))
    return num


print(binary_array_to_number([1, 0, 0, 1]))
