from collections import deque
import sys

input = sys.stdin.readline
a = int(input())
s = deque()  # 큐로 사용할 deque 초기화

for _ in range(a):
    command = input().split()
    n = command[0]

    if n == "push":
        s.append(command[1])
    elif n == "pop":
        if len(s) == 0:
            print(-1)
        else:
            print(s.popleft())  # deque에서 가장 앞의 요소를 제거하고 출력
    elif n == "front":
        if len(s) == 0:
            print(-1)
        else:
            print(s[0])
    elif n == "back":
        if len(s) == 0:
            print(-1)
        else:
            print(s[-1])
    elif n == "size":
        print(len(s))
    elif n == "empty":
        if len(s) == 0:
            print(1)
        else:
            print(0)