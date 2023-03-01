import random
import sys
import time

def merge(left, right):
    result =[]
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result

def merge_sort(array):
    if len(array) == 1:
        return array

    middle = len(array) // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])

    return merge(left, right)

def shell_sort(array):
    jump = len(array) // 2

    while jump > 0:
        i = jump
        while i < len(array):
            element = array[i]
            j = i
            while array[j - jump] > element and j >= jump:
                array[j] = array[j - jump]
                j = j - jump
            array[j] = element
            i += 1
        jump //= 2

    return array

def counting_sort(array):
    maximum = max(array)
    sortedArray = [0 for x in range(len(array))]
    frequency = [0 for x in range(maximum + 1)]

    for element in array:
        frequency[element] += 1

    for i in range(1, maximum + 1):
        frequency[i] += frequency[i-1]

    i = 0
    while i <= len(array) - 1:
        if frequency[array[i]] != 0:
            frequency[array[i]] -= 1
            sortedArray[frequency[array[i]]] = array[i]
        i += 1

    return sortedArray

def counting_sort_for_radix_b(array, power):
    sortedArray = [0 for x in range(len(array))]
    frequency = [0, 0]

    for element in array:
        frequency[(element >> power) & 1] += 1

    frequency[1] += frequency[0]

    i = len(array) - 1
    while i >= 0:
        if frequency[(array[i] >> power) & 1] != 0:
            frequency[(array[i] >> power) & 1] -= 1
            sortedArray[frequency[(array[i] >> power) & 1]] = array[i]
        i -= 1
    return sortedArray

def radix_sort(array):
    maximum = len(bin(max(array)))
    i = 1
    power = 0
    sortedArray = []
    while i <= maximum:
        sortedArray = counting_sort_for_radix_b(array, power)
        i += 1
        power += 1
        array = sortedArray
    return sortedArray

def counting_sort_for_radix_16(array, power):
    sortedArray = [0 for x in range(len(array))]
    frequency = [0 for x in range(16)]

    for element in array:
        frequency[(element >> power) & 15] += 1

    for i in range(1,16):
        frequency[i] += frequency[i-1]

    i = len(array)-1
    while i >= 0:
        if frequency[(array[i] >> power) & 15] != 0:
            frequency[(array[i] >> power) & 15] -= 1
            sortedArray[frequency[(array[i] >> power) & 15]] = array[i]
        i -= 1
    return sortedArray

def radix_sort_b16(array):
    maximum = len(bin(max(array)))
    power = 0
    auxArray = []
    while power <= maximum:
        auxArray = counting_sort_for_radix_16(array, power)
        power += 4
        array = auxArray
    return array

def divide(array, left, right):
    pivot_choice = [array[left], array[right], array[(right + left) // 2]]
    maximum = max(pivot_choice)
    minimum = min(pivot_choice)

    if array[left] != maximum and array[left] != minimum:
        pivot = array[left]
        swap = array[left]
        array[left] = array[right]
        array[right] = swap
    elif array[right] != maximum and array[left] != minimum:
        pivot = array[right]
    else:
        pivot = array[(right + left) // 2]
        pivot = array[(right + left) // 2]
        swap = array[(right + left) // 2]
        array[(left + right) // 2] = array[right]
        array[right] = swap

    i = left - 1
    j = left
    while j < right:
        if array[j] < array[right]:
            i += 1
            swap = array[i]
            array[i] = array[j]
            array[j] = swap
        j += 1

    i += 1
    swap = array[i]
    array[i] = array[right]
    array[right] = swap
    return (i, array)

def quicksort(array, minimum, maximum):
    if minimum <= maximum:
        p = divide(array, minimum, maximum)
        pivot = p[0]
        array = p[1]
        quicksort(array, minimum, pivot - 1)
        quicksort(array, pivot + 1, maximum)
    return array

def sortingAlgorithms(array, sortType):
    s = sorted(array)
    sortedArray = []
    if sortType == 0:
        sortedArray = merge_sort(array)
    if sortType == 1:
        sortedArray = shell_sort(array)
    if sortType == 2:
        sortedArray = counting_sort(array)
    if sortType == 3:
        sortedArray = radix_sort(array)
    if sortType == 4:
        sortedArray = radix_sort_b16(array)
    if sortType == 5:
        sortedArray = quicksort(array, 0, len(array)-1)

sys.setrecursionlimit(10**7)

tests = [(1000,10000000),(10000,1000000),(100000,1000000),(1000000,1000),(10000000,100000)]
sortType = ["Merge Sort", "Shell Sort", "Counting Sort", "Radix Sort cu baza 2", "Radix Sort cu baza 16", "Quick Sort"]
array = []

for test in tests:
    for i in range(test[0]):
        value = random.randint(1, test[1])
        array.append(value)

    for i in range(6):
        start = time.time()
        sortingAlgorithms(array, i)
        stop = time.time()
        print(f"{sortType[i]} executed in {stop-start:.4f} seconds, with N = {test[0]} & M = {test[1]}.")