list1 = list(map(int, input().split()))
print(list1)
def quick_sort(list):
    if len(list) <= 1:
        return list

    pivot = list[0]
    tail = list[1:]

    left_side = [i for i in tail if i < pivot]
    right_side = [j for j in tail if j >= pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

list1 = quick_sort(list1)
print(list1)