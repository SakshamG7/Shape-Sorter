numbers = list(set([18, 57, 79, 77, 26, 95, 15, 1, 71, 37, 22, 96, 65, 63, 94, 74, 2, 94, 82, 82, 1, 84, 46, 59, 25, 24, 13, 88, 70, 38, 67, 92, 96, 17, 72, 72, 87, 36, 56, 53, 32, 26, 37, 13, 39, 79, 4, 14, 69, 7, 63, 47, 37, 28, 70, 58, 18, 39, 2, 94, 89, 3, 81, 12, 92, 58, 86, 88, 77, 62, 71, 4, 34, 31, 75, 91, 100, 95, 42, 94, 99, 35, 73, 45, 18, 80, 39, 60, 9, 3, 94, 2, 64, 16, 2, 84, 12, 18, 37, 9]))
newNumberMatrix = []
sortedArray = []

smallest = numbers[0]
for number in numbers:
    newNumberMatrix.append([])
    if number < smallest:
        smallest = number
_ = 0
for number in numbers:
    for i in range(smallest - 1, number):
        if i >= number - 1:
            newNumberMatrix[_].append(number)
        else:
            newNumberMatrix[_].append(0)
        sortedArray.append(0)
    _ += 1

# MERGE ARRAYS
for i in range(len(newNumberMatrix)):
    for j in range(len(newNumberMatrix[i])):
        sortedArray[j] += newNumberMatrix[i][j]
# Strip the zeros from the sorted array
sortedArray = list(filter(lambda a: a != 0, sortedArray))
print(sortedArray)