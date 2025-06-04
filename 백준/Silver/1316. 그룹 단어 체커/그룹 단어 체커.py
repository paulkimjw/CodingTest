a = int(input())
count = 0

for _ in range(a):
    word = input()
    is_group = True
    seen = set()
    prev = ''
    for char in word:
        if char != prev:
            if char in seen:
                is_group = False
                break
            seen.add(char)
        prev = char
    if is_group:
        count += 1

print(count)