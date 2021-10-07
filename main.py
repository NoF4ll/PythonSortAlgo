from random import seed
from random import randint

seed(1)

bubbleList = []
insertionList = []
selectionList = []
randomMinRange = 0
randomMaxRange = 100


for x in range(randomMinRange, randomMaxRange):
    value = randint(0, 10)
    bubbleList.append(value)
    insertionList.append(value)
    selectionList.append(value)

print(bubbleList)


def bubble_sort(arr):
    temp = 0
    for x in range(1, len(arr)):
        for y in range(0, len(arr) - 1):
            if arr[y] > arr[y + 1]:
                temp = arr[y]
                arr[y] = arr[y + 1]
                arr[y + 1] = temp
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def selection_sort(arr):
    for i in range(len(arr)):

        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


bubbleList = bubble_sort(bubbleList)
insertionList = insertion_sort(insertionList)
selectionList = selection_sort(selectionList)

print(selectionList)
