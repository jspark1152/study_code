def check_left(A, B, d):
    if d == 0:
        if B-1 >= 0 and world[A][B-1] == 0:
            return 0 #0은 육지를 의미
        else:
            return 1 #1은 바다를 의미
    elif d == 3:
        if A+1 <= N and world[A+1][B] == 0:
            return 0
        else:
            return 1
    elif d == 2:
        if B+1 <= M and world[A][B+1] == 0:
            return 0
        else:
            return 1
    elif d == 1:
        if A-1 >= 0 and world[A-1][B] == 0:
            return 0
        else:
            return 1

A = 0
B = 0
d = 0

print(check_left(A, B, d))







