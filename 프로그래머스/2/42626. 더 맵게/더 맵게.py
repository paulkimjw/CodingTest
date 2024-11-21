import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        # 섞을 음식이 부족할 경우, 더 이상 진행할 수 없으므로 -1 반환
        if len(scoville) < 2:
            return -1
        
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        new_scoville = min1 + (min2 * 2)
        heapq.heappush(scoville, new_scoville)
        
        answer += 1

    return answer