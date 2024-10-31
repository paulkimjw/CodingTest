from collections import Counter

def solution(clothes):
    # Step 1: 각 의상 종류별로 의상의 개수를 셈
    clothes_count = Counter([kind for name, kind in clothes])
    
    # Step 2: 모든 의상 종류의 조합 경우의 수를 계산
    answer = 1
    for count in clothes_count.values():
        answer *= (count + 1)  # (의상을 입지 않는 경우 + 입는 경우)를 곱함
    
    # Step 3: 아무것도 입지 않는 경우를 제외
    return answer - 1