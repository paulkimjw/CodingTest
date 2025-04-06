def solution(s):
    last_seen = {}  # 각 문자의 마지막 등장 인덱스 저장
    answer = []
    
    for i, ch in enumerate(s):
        if ch in last_seen:
            distance = i - last_seen[ch]
            answer.append(distance)
        else :
            answer.append(-1)
        last_seen[ch] = i
    
    return answer

    
    
    