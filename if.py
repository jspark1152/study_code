#조건문을 이용하면 조건에 따라서 프로그램의 로직을 설정

a=70

if a>=90:
    print('학점 : A')
elif a>=80:
    print('학점 : B')
elif a>=70:
    print('학점 : C')
else:
    print('학점 : F')

score = 65

if score>=70:
    print('성적이 70점 이상 입니다.')
    if score>=85:
        print('성적이 우수해요.')
else:
    print('성적이 70점 미만입니다.\n분발하세요.')
    #이 들여쓰기의 정석은 4번의 스페이스라고 함;; 탭 한번으로도 가능한데 뭐가 다른지 잘..

