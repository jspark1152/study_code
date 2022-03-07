'''
못생긴 수 : 2, 3, 5 만을 소인수로 가지는 수를 의미
1은 못생긴 수라고 가정함
이 때 N번째 못생긴 수를 찾는 프로그램 작성

입력 조건
1. 첫 줄에 N이 입력

출력 조건 : N번째 못생긴 수를 출력
'''

print('N을 입력')
N = int(input())

list_ugly = [1]

num = 1

while len(list_ugly) != N:
    num += 1
    k = num
    print(num, k)
    
    while k % 2 == 0:#약수 2 여부 확인
        k = k / 2
    print(num, k)
    
    while k % 3 == 0:#약수 3 여부 확인
        k = k / 3
    print(num, k)
    
    while k % 5 == 0:#약수 5 여부 확인
        k = k / 5
    print(num, k)
    
    if k == 1:#약수가 2,3,5 뿐인 경우
        list_ugly.append(num)
    else:
        pass
    
    print(list_ugly)

print(list_ugly[-1])

#자체 평가 : 연산자 순간 혼동. while문을 잘 안써서 아직 버벅되는 경향이 있음.
#2~ 쭈욱 일일히 다 계산하기 때문에.. 오래 걸림.. 다른 방식으로 접근