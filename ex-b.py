#소수 구하기
#M 이상 N이하의 소수를 모두 출력
import math

print("1 이상 1,000,000 이하인 수 (M, N)을 입력 : ")
M, N = map(int, input().split())

prime = [i for i in range(2,N+1)]

print(prime)

for i in range(2, int(math.sqrt(N))+1):
    j = 2
    while i*j <= N:
        prime = [k for k in prime if k != i*j]
        j += 1

prime = [i for i in prime if i >= M]

print(prime)
for i in range(len(prime)):
    print(prime[i])

#암호 만들기
#서로 다른 L개의 알파벳 소문자들로 구성
#최소 한 개의 모음과 최소 두개의 자음으로 구성
#또한 암호는 정렬되어 있음 ex) abc
#문자 종류는 C
#가능성 있는 암호를 구하는 코드
#첫 줄 : 두 정수 L, C가 입력(3<= L <= C <=15)
#다음 줄에는 C개의 문자들이 주어지며 공백으로 구분

#알파벳은 총 26개 이중 모음은 a e i o u 5개

#모음 최소 1개 / 자음 최소 2개

#L-모음개수 >= 2 자연스럽게 자음 2개 이상
#L-모음개수 < 2 경우가 문제
#a e i b c 5개 선택 하고 3자리 암호 만들 시 a e i 도 가능

print("암호 길이와 사용될 문자 종류를 순서대로 입력")
L, C = map(int, input().split())


print("암호에 사용할 문자 {} 개를 입력".format(C))
code = list(map(str, input().split()))
list_lowercase=['a', 'e', 'i', 'o', 'u']

code.sort()

print(code)

import itertools

combi=list(itertools.combinations(code, L)) #L개를 선택하는 조합, 정렬은 자동

print(combi) #최소 모음1개 & 자음2개 규칙을 찾아야 함

#모음의 개수를 카운트한 후 조건식으로 넣음
for pw in combi:
    count = 0
    for i in pw:
        if i in list_lowercase:
            count += 1
    
    if count >= 1 and L-count >= 2:
        print(''.join(pw))