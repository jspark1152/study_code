print('몇개의 수를 입력하시겠습니까?')
n = int(input())

list=[]

for i in range(n):
    print('{}번째 값 = '.format(i+1))
    list.append(input())

print(list)

n, k = map(int, input().split())
print(n, k)