def solution(n):
    if n < 2:
        return 0

    # 에라토스테네스의 체 초기화: True이면 소수, False이면 소수 아님
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님

    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1

    # 소수 개수 세기
    prime_count = sum(is_prime)
    return prime_count