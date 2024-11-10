n = int(input())
for i in range(n):
    s = input().split()  # 각 라인에서 단어를 입력받아 split()으로 리스트로 만듦
    reversed_s = s[::-1]  # 단어 순서를 반대로 뒤집음
    print(f"Case #{i + 1}: {' '.join(reversed_s)}")