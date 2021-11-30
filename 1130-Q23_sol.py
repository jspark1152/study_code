#23번 정렬문제 솔루션
#sort 함수 인수에 key=lambda x: 입력

n = int(input())
students = []

for _ in range(n):
    students.append(input().split())

'''
정렬 기준
두번째 국어점수를 기준으로 내림차순
국어점수가 동일한 경우 세번째 영어점수를 기준으로 오름차순
영어점수가 동일한 경우 네번째 수학점수를 기준으로 내림차순
수학점수가 동일한 경우 첫번째 이름을 기준으로 오름차순
'''

students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in students:
    print(i[0])