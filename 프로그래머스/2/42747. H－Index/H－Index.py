def solution(citations):
    citations.sort(reverse=True)  # 내림차순 정렬
    answer = 0
    
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            answer = i + 1
        else:
            break
            
    return answer