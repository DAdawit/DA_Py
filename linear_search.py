def linear_search(list, target):
    for i in range(0, len(list)):
        print(f"i = {i} length of list {len(list)}")
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print(f"Target foun at index :{index}")
    else:
        print("Target not found")

list =[1,2,3,4,5,6,7,8,9,10]
index  = linear_search(list, 10)

verify(index)