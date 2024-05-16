def solution(answers):
    answer = []
    a_pattern = [1, 2, 3, 4, 5]
    b_pattern = [2, 1, 2, 3, 2, 4, 2, 5]
    c_pattern = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    scores = [0, 0, 0]  # 각 수포자의 점수를 저장할 리스트
    
    # 정답 비교하며 점수 계산
    for idx, ans in enumerate(answers):
        if ans == a_pattern[idx % len(a_pattern)]:
            scores[0] += 1
        if ans == b_pattern[idx % len(b_pattern)]:
            scores[1] += 1
        if ans == c_pattern[idx % len(c_pattern)]:
            scores[2] += 1
    
    # 최고 점수 구하기
    max_score = max(scores)
    
    # 최고 점수를 받은 수포자 찾기
    for i, score in enumerate(scores):
        if score == max_score:
            answer.append(i + 1)
    
    return answer
