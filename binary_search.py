def binary_search(list, target):
    first = 0
    last  = len(list)-1

    while first <= last:
        midPoint = (first + last) // 2
        if(list[midPoint] == target):
            return midPoint
        if(list[midPoint] < target):
            first = midPoint + 1
        else:
            last = midPoint -1
    return None

def verify(index):
    if index is None:
        print("Item not found")
    else:
        print(f"Item found at index {index}")

list = [1,2,3,4,5,6,7,8,9,10]
# result = binary_search(list, 10)
# middle = len(list) // 2

# print(middle)
# print(list[middle])
# print(2//2)
# print(list[middle+1:])
# print(list[:middle])
# verify(result)
# print(list[5:])


def recursive_binary_search(list, target, start =0):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list) // 2
        if list[midpoint] == target:
            return midpoint + start
        elif list[midpoint] < target:
            return recursive_binary_search(list[midpoint+1:],target, start + midpoint + 1)
        else:
            return recursive_binary_search(list[:midpoint], target, start)
        


list = [1,2,3,4,5,6,7,8,9,10]
result = recursive_binary_search(list, 9)
print(f"Result: {result}")
print(f"Target: {list[result]}")
verify(result)

# verify(f"\nfrom recursive function {result}")




def binarySearch2(list, target):
    start = 0
    last = len(list)+1

    while start <= last:
        midPoint = len(list) // 2
        if list[midPoint] == target:
            return midPoint
        elif list[midPoint] < target:
            midPoint = midPoint + 1
        else :
            midPoint = midPoint - 1

    return None


def recursiveBinarySearch2(list, target, start = 0):
    if len(list) == 0:
        return False
    else:
        middpoint = len(list)//2
        if list[middpoint] == target:
            return middpoint + start
        elif list[middpoint] < target:
            return recursiveBinarySearch2(list[middpoint+1:],target, start+middpoint+1)
        else:
            return recursiveBinarySearch2(list[:middpoint], target, start)
        

list = [1,2,3,4,5,6,7,8,9,10]


unsortedList = [5,4,3,6,9,8,7,2,1,12,11,0]

unsortedList.sort()
print(unsortedList)