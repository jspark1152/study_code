#실전 문제 : 1로 만들기

#정수 X가 주어질 때 정수 X에 사용할 수 있는 연산은 다음 4가지
#1. 5로 나누어 떨어지면 5로 나눔
#2. 3으로 나누어 떨어지면 3으로 나눔
#3. 2로 나누어 떨어지면 2로 나눔
#4. X에서 1을 뺌

#정수 X가 주어졌을 때 위 4가지 연산을 적절히 사용하여 1을 만듬
#연산을 사용하는 횟수의 최솟값을 출력

#첫 줄에 정수 X가 입력(1이상 30,000이하)

#출력 조건 : 첫줄에 연산횟수 최솟값 출력

#어.. 이거 생각보다 어렵
#알고리즘 어떻게 짜지.. 와 이거 생각보다 어렵다 백신 맞은 왼팔이 아려온다

# 26 같은 경우
# 26 > 13 > 12 > 4 > 2 > 1
# 26 > 25 > 5 > 1

#과정 자체를 알고리즘 화하기는 힘들지 않을까
#모든 경우를 다 계산하게 한 뒤에 그 중 짧은거를 선택하는 방법?


print('정수 X 입력')
X = int(input())

mark = [[] for _ in range(X)]
#[[26], [25, 13], [5, 12], [1, 4], ...] 이렇게 진행되고 1의 위치 찾기?

count = 0

mark[count].append(X)

def make_one(mark, count):
    
    print(mark[count])
    for i in range(len(mark[count])):
        X = mark[count][i]

        if X % 5 == 0:
            mark[count+1].append(X/5)
        
        if X % 3 == 0:
            mark[count+1].append(X/3)
            
        if X % 2 == 0:
            mark[count+1].append(X/2)
        
        if X > 1:
            mark[count+1].append(X-1)

    count += 1

    if 1 in mark[count]:
        return
    
    make_one(mark, count)

make_one(mark, count)

for i in range(len(mark)):
    if 1 in mark[i]:
        print(i)

#자체 평가 : 처음에 문제를 잘못이해하고 접근 / 이후 어떻게 풀이해야할지 굉장히 난해했음
#지금 이런 반복도 메모이제이션이라고 할 수 있는가?
#빨리 되긴 하네?