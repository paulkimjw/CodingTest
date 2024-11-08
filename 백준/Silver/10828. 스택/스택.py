import sys

input = sys.stdin.readline  # 빠른 입력을 위해 sys.stdin.readline 사용
a = int(input())
s = []
output = []  # 출력을 모아둘 리스트

for _ in range(a):
    command = input().split()
    n = command[0]

    if n == "push":
        s.append(int(command[1]))
    elif n == "top":
        if len(s) == 0:
            output.append(-1)
        else:
            output.append(s[-1])
    elif n == "size":
        output.append(len(s))
    elif n == "empty":
        if len(s) == 0:
            output.append(1)
        else:
            output.append(0)
    elif n == "pop":
        if len(s) == 0:
            output.append(-1)
        else:
            output.append(s.pop())

# 최종적으로 한 번에 출력
sys.stdout.write("\n".join(map(str, output)) + "\n")