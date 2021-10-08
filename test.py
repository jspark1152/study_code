list1 = list(map(int, input().split()))

def quick_sort(list):
    if len(list)<=1:
        return list
    
    pivot = list[0]
    tail = list[1:]
    x = [i for i in tail if i <= pivot]
    y = [i for i in tail if i > pivot]
    return quick_sort(x)+[pivot]+quick_sort(y)

list1 = quick_sort(list1)

print(list1)