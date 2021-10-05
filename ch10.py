#Graph란 Node와 Node 간의 연결된 Edge의 정보를 가지고 있는 자료구조를 의미
#서로 다른 개체(또는 객체)가 연결되어 있다라는 언급이 있다면 그래프 알고리즘과 관련
#Tree 자료구조는 다양한 알고리즘에서 사용
#다익스트라 알고리즘에서 우선순위 큐가 사용되었는데 이를 구현하기 위해 최소힙 또는 최대힙을 사용
#그래프 구현은 2가지 방식
#1. 인접 행렬 : 2차원 배열로 행렬 표현
#2. 인접 리스트 : 리스트를 사용
#메모리와 시간을 염두에 두고 알고리즘을 선택해서 구현해야 함
#노드와 간선의 개수가 많은 경우는 플로이드 워셜(인접 행렬로 구현) 알고리즘은 불리함

#서로소 집합 Disjoint Sets
#수학에서 공통 원소가 없는 두 집합을 의미
#서로소 집합 자료구조 : 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
#union 과 find 2개의 연산으로 조작
#union : 2개의 원소가 포함된 집합을 하나의 집합으로 합
#find : 특정 원소가 속한 집합이 어떤 집합인지 알려줌
#따라서 union-find 자료구조라고 불리기도 함
#구현할 때는 트리 자료구조를 이용하여 집합을 표현
#집합을 표현하는 서로소 집합 계산 알고리즘은 다음과 같음
#1. union 연산을 확인하고 서로 연결된 두 노드 A, B를 확인
#1-1) A와 B의 루트 노드 A', B'을 각각 찾음
#1-2) A'을 B'의 부모 노드로 설정(B'이 A'을 가리키도록)
#2. 모든 union 연산을 처리할 때까지 1번 반복
#예제
#union 1,4 & 2,3 & 2,4 &5,6
#이 경우 4의 부모 노드는 1이라는 의미
#3의 부모 노드는 2
#4의 부모 노드는 2 > 하지만 이미 1이 부모 노드로 존재 > 2의 부모 노드 또한 1이 됨
#6의 부모 노드는 5
#따라서 {1, 2, 3, 4, 5, 6}의 집합이 {1, 2, 3, 4} 과 {5, 6}으로 나뉨

#특정 원소가 속한 집합(결국 그 집합을 대표하는 부모 원소(가장 작은 값)를 출력)
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

#두 원소가 속한 집합을 합치기. 즉, 그 집합을 대표하는 부모 원소로 마킹
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    #작은 값을 부모 노드로 설정
    if a < b: 
        parent[b] = a
    else:
        parent[a] = b

print('노드 개수 v, 간선 개수 e 입력')
v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

print('간선 정보 입력')
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합 : ', end='')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')

print()

print('부모 테이블 : ', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')

#이 때 3의 부모 노드를 찾는 과정에서 결국은 1이긴 하지만 부모 테이블에선 현재 2로서 파악
#즉, 이대로 구현시 N의 부모 노드를 찾기 위해 모든 부모 노드를 거슬러 올라가야하는 번거러움
#이는 곧 시간 복잡도 상승으로 이어짐

#따라서 find_parent 함수를 경로 압축 기법으로 수정

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
#즉, find 함수에서 부모노드를 끝까지 거슬러가서 미리 파악

#수정 후엔 부모 테이블에 3의 부모 노드가 1로 파악

#사이클 판별
#서로소 집합으로 사이클 판별 가능
#(1,2) / (1,3) / (2,3) 인 경우 1, 2, 3 의 부모 노드가 1로 동일하므로 사이클이 발생

#신장 트리
#자주 출제되는 유형
#하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프를 의미
#이 때 모든 노드가 포함되어 서로 연결되면서 사이클이 존재하지 않는다는 조건은 트리의 성립 조건이기도 함
#크루스칼 알고리즘
#가능한 최소 비용으로 신장 트리를 찾아야할 때
#모든 도시를 연결하고자 할때 최소한의 비용으로 연결하는 유형
#이 때 신장 트리 중 최소 비용의 신장 트리를 찾는 알고리즘을 최소 신장 트리 알고리즘이라 함
#대표적인 최소 신장 트리 알고리즘으로 크루스칼 알고리즘이 있음
#이는 그리디 알고리즘으로 분류되며 알고리즘은 다음과 같음
#1. 간선 데이터를 비용에 따라 오름차순으로 정렬
#2. 간선을 하나씩 확인하여 현재 간선이 사이클을 발생시키는지 확인
#2-1) 사이클이 발생하지 않는 경우 최소 신장 트리에 포함
#2-2) 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않음
#3. 모든 간선에 대하여 2번 반복

#구현 코드는 ch10-kruskal.py 에 직접 해봄

#위상정렬 Topology Sort
#방향 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 나열하는 것'
#예시로는 선수과목을 고려한 학습 순서 설정(커리큘럼에 따라 수강)
#그래프상에서 선후 관계가 있다면 위상 정렬을 수행하여 모든 선후 관계를 지키는 전체 순서를 계산
#진입차수 : 특정한 노드로 들어오는 간선의 개수
#위상정렬 알고리즘은 다음과 같음
#1. 진입차수가 0인 노드를 큐에 넣음
#2. 큐가 빌 때까지 다음 과정 반복
#2-1) 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거
#2-2) 새롭게 진입차수가 0이 된 노드를 큐에 넣음