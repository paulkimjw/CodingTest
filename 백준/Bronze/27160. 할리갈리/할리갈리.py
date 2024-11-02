n = int(input())
s = {}

for i in range(n):
    a, b = input().split()
    if a in s:
        s[a] += int(b)
    else:
        s[a] = int(b)

# 수정된 부분: s.values()로 변경
if 5 in s.values():
    print("YES")
else:
    print("NO")