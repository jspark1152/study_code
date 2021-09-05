#얼음 케이스 답안 예시

n, m = map(int, input().split())

#2차원 리스트 입력받는 방식 기억해두자
graph = [] #2차원으로 초기화부터 굳이 시키지 않아도 되네
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y): #함수 인수를 애초에 좌표로 받음
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    #얼음 구멍 0인 곳을 방문하지 않은 곳으로
    #1로 방문 처리함과 동시에 True값
    if graph[x][y] == 0:
        graph[x][y] = 1 #일종의 방문 처리

        #(x, y)의 상하좌우 확인
        #인접한 0인 곳을 모두 방문 처리하고 돌아옴
        #결과적으로 True값은 맨 처음 시작한 포인트만 True값을 받게됨
        #왜냐 그 다음 포인트에서 dfs 함수가 작동하면 방문한 곳이기에 False를 출력
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            print(i, j)
            result += 1

print(result)

#음 재귀 표현이 참 어렵다 여전히.. 이걸 잘해야할듯
