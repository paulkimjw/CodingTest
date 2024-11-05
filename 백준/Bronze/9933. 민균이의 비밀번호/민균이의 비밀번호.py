n = int(input())
s = []
for i in range(n):
    s.append(input())

for i in s:
    if i[::-1] in s:
        print(len(i), i[len(i) // 2])
        break