#경쟁적 전염
#N X N 시험관에 특정 위치에 바이러스가 존재
#바이러스는 1 ~ K 까지 총 K 가지
#모든 바이러스는 1초마다 상하좌우로 증식
#단, 낮은 번호의 바이러스가 우선적으로 증식하며 바이러스가 증식한 자리에는 다른 바이러스가 증식 못함
#시험관 크기와 바이러스 위치 정보가 주어졌을 때, S초가 지난 후에 (X, Y) 에 존재하는 바이러스를 출력

#입력 조건
#1. 첫 줄에 자연수 N, K가 주어짐
#2. 다음 줄부터 N줄에 걸쳐 시험관 정보가 주어짐
#3. 다음 줄에 S, X, Y가 주어짐

#출력 조건 : S초 뒤에 (X, Y)에 존재하는 바이러스 번호 출력

print('시험관 크기 N, 바이러스 종류 K 입력')
N, K = map(int, input().split())

plate = []
print('시험관 정보 입력')
for i in range(N):
    list0 = list(map(int, input().split()))
    plate.append(list0)

print('S, X, Y 입력')
S, X, Y = map(int, input().split())

#먼저 plate에서 바이러스 위치 파악
def scan_virus():
    list_virus = [[] for _ in range(K+1)]
    for i in range(N):
        for j in range(N):
            for n in range(1, K+1):
                if plate[i][j] == n:
                    list_virus[n].append((i, j))
    return list_virus

visited = [[False] * N for _ in range(N)]

#위치가 파악된 바이러스로부터 1초간의 증식
def virus(list_virus):
    for i in range(1, K+1):
        for x in list_virus[i]:
            if x[0]-1 >= 0:
                if plate[x[0]-1][x[1]] == 0 and not visited[x[0]-1][x[1]]:
                    visited[x[0]-1][x[1]] = True
                    plate[x[0]-1][x[1]] = i
            
            if x[1]-1 >= 0:
                if plate[x[0]][x[1]-1] == 0 and not visited[x[0]][x[1]-1]:
                    visited[x[0]][x[1]-1] = True
                    plate[x[0]][x[1]-1] = i
            
            if x[0]+1 < N:
                if plate[x[0]+1][x[1]] == 0 and not visited[x[0]+1][x[1]]:
                    visited[x[0]+1][x[1]] = True
                    plate[x[0]+1][x[1]] = i
            
            if x[1]+1 < N:
                if plate[x[0]][x[1]+1] == 0 and not visited[x[0]][x[1]+1]:
                    visited[x[0]][x[1]+1] = True
                    plate[x[0]][x[1]+1] = i

#1초마다 바이러스 위치를 갱신하면서 증식
for _ in range(S):
    list_virus = scan_virus()
    print(list_virus)
    virus(list_virus)

print(plate[X-1][Y-1])

#자체 평가 : 한번에 성공. 역시 짜릿함. 최대한 간결하게 짜보려고 노력했음.
#다만 알고리즘 구현 방식에 대한 고민을 짧게 함. 그래서 조금 조잡할 수 있겠다는 걱정이 듬.