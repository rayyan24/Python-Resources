def selectionSort(arr):
    size = len(arr)
    for i in range(0, size-1):
        currentLeast = arr[i]
        for j in range(i+1, size):
            if arr[j] < currentLeast:
                currentLeast = arr[j]
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def bubbleSort(arr):
    size = len(arr)
    for i in range(0, size-1):
        for j in range(0, size-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        leftList = arr[0:mid]  # 0 to mid-1
        rightList = arr[mid:]  # mid to len of list-1
        mergeSort(leftList)
        mergeSort(rightList)
        i, j, k = 0, 0, 0
        while i < len(leftList) and j < len(rightList):
            if leftList[i] < rightList[j]:
                arr[k] = leftList[i]
                i += 1
                k += 1
            else:
                arr[k] = rightList[j]
                j += 1
                k += 1
        while i < len(leftList):
            arr[k] = leftList[i]
            i += 1
            k += 1
        while j < len(rightList):
            arr[k] = rightList[j]
            j += 1
            k += 1
    return arr

def insertionSort(arr):
    size=len(arr)
    for i in range(size-1):
        for j in range(i+1,size):
            if arr[i]<arr[j]:
                continue
            else:
                arr[i],arr[j]=arr[j],arr[i]
    return arr

def main():
    data = ["Zub", "Kai", "Aba", "DRS"]
    data = [5, 6, 4, 200, 200, 56, 23]
    print(data)
    data = insertionSort(data)
    print(data)


main()
