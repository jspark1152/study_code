#실전 문제 : 바닥 공사
#가로 길이 N / 세로 길이 2 직사각형태의 바닥
#이 바닥을 1 X 2 / 2 X 1 / 2 X 2 타일로 채우기
#바닥을 채우는 모든 경우의 수를 찾기

#첫 줄에 N 이 주어짐(1 이상 1,000 이하)

#출력 조건 : 바닥을 채우는 방법의 수를 796796으로 나눈 나머지를 출력

#구상 : 가로 길이를 1 또는 2로 분할하는 경우의 수 > 2인 경우 세로 길이가 2인 녀석으로 쪼갤 수 있음
import math

print('N 값을 입력')
N = int(input())

a = N//2

print('a =', a)

result = 0

for i in range(0, a+1): #i = 2의 개수
    b = N - 2*i #1 개수
    
    x = math.factorial(i+b)/math.factorial(b)
    y = x/math.factorial(i)
    result += y * pow(2, i)

print(result % 796796)

#자체 평가 : ... 단순 경우의 수를 구한듯 함
#심지어 N = 400 쯤부터 오버플로 오류 발생...