M,N  = map(int,input().split())

num_to_word = {
    0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
    5: "five", 6: "six", 7: "seven", 8:"eight", 9: "nine"
}

# M 이상 N 이하의 각 숫자를 영어 단어로 변환
numbers = [(i, " ".join(num_to_word[int(digit)] for digit in str(i))) for i in range(M, N +1)]

# 영어 단어 기준으로 정렬
numbers.sort(key = lambda x: x[1])

#출력
for idx, (num, _) in enumerate(numbers):
    if idx >0 and idx % 10 == 0:
        print()
    print(num, end= " ")

    