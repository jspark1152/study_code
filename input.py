#알고리즘 문제 풀이의 첫 단계는 데이터를 입력받는 것
#입력을 받아서 적절한 알고리즘을 수행한 뒤 결과를 출력
#input() : 한 줄의 문자열을 입력받도록 함
#입력받은 데이터를 정수형 데이터로 처리하기 위해 int() 사용

#list(map(int, input().split())) : 공백으로 구분하여 여러 데이터를 입력받을 때 사용

n = int(input())

data = list(map(int, input().split()))

data.sort(reverse=True)

print(data)

#n, m, k를 공백으로 구분하여 입력
n, m, k = map(int, input().split())

#이러한 경우 3개의 값을 정확히 입력해줘야함
print(n, m, k)

#input() 함수는 동작 속도가 느림
#입력해야할 데이터가 엄청나게 많을 경우 sys 라이브러리의 sys.stdin.readline() 이용
#import sys
#sys.stdin.readline().rstrip()
#rstrip()의 용도는 readline()으로 입력후 엔터가 줄 바꿈 기호로 입력되는데 이 공백을 제거하기 위해 사용

import sys

#data = sys.stdin.readline().rstrip()
data = sys.stdin.readline().rstrip()
print(data)

