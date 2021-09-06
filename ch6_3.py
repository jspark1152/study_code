#실전 문제 : 성적이 낮은 순서로 학생 출력하기
#N명의 학생 정보
#학생 정보는 학생의 이름과 성적으로 구분

#첫 줄에 학생 수 N이 입력(1이상 100,000이하)
#둘째줄부터 학생의 이름을 나타내는 문자열 A와 성적을 나타내는 정수 B가 공백으로 구분되어 입력
#문자열 A의 길이와 학생의 성적은 100이하의 자연수

#출력 조건 : 모든 학생의 이름을 성적이 낮은 순서대로 출력 / 동일할 경우 자유롭게 출력

print('학생 수를 입력')
N = int(input())

array = []

print('학생 이름 __ 학생 성적 입력')
for i in range(N):
    data = input().split()
    array.append([data[0], int(data[1])])

def setting(data):
    return data[1]

array = sorted(array, key=setting)
    
print(array)

for i in range(len(array)):
    print(array[i][0], end=' ')