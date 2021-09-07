#실전 문제 : 떡볶이 떡 만들기
#떡볶이 떡의 길이가 일정하지 않음
#한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰줌
#절단기에 H를 지정하면 줄지어진 떡을 한 번에 절단
#잘려나간 떡을 손님이 가져감
#손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 H의 최댓값 구하는 프로그램 작성

#첫 줄에 떡 개수 N, 손님이 요청한 떡길이 M 을 입력(1<=N<=1,000,000 & 1<=M<=2,000,000,000)
#두번째 줄에는 떡의 개별 높이가 주어짐

#출력 조건 : 적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 H 최대값 출력(H는 0 또는 자연수)

print('떡 개수 N / 요청한 떡 길이 M 입력')
N, M = map(int, input().split())

print('떡 길이 입력')
leng = list(map(int, input().split()))

leng = sorted(leng)

def cut_sum(k):
    result = []
    for i in range(len(leng)):
        result.append(leng[i] - k)
    sum = 0
    for j in range(len(leng)):
        if result[j]>=0:
            sum += result[j]
    return sum

def setup_H(target, start, end):
    end = leng[-1]

    while start < end:
        H = (start+end)//2
        if cut_sum(H) == target:
            return H
        elif cut_sum(H) < target:
            end = H - 1
        elif cut_sum(H) > target:
            start = H + 1
    
    if start == end:
        return start

H = setup_H(M, 0, N-1)

print(H)

#자체평가 : 오류발생, M이 큰 경우 가장 작은 떡길이 보다 낮은 H 설정 불가능
#이진 탐색으로 접근은 좋았음
#자체 수정 완, 생각보다 어렵지 않음