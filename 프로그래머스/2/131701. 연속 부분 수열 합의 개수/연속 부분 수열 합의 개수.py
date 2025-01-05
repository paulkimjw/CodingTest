def solution(elements):
    n = len(elements)
    extended = elements * 2   # 원형 배열 구현
    sums = set()

  
    for length in range(1, n + 1):
        for start in range(n):  
            sub_sum = sum(extended[start:start + length])
            sums.add(sub_sum)

    return len(sums)  # 고유한 합의 개수 반환