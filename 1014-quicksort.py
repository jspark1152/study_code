list1 = list(map(int, input().split()))

def quick_sort(list):
    if len(list) <= 1:
        return list
    
    pivot = list[0]
    tail = list[1:]

    left = [i for i in tail if i < pivot]
    right = [j for j in tail if j > pivot]
    return quick_sort(left)+[pivot]+quick_sort(right)
    
list1 = quick_sort(list1)

print(list1)