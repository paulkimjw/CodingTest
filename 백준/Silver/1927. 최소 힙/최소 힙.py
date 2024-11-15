import sys
import heapq

input = sys.stdin.readline
n = int(input())
min_heap = []

for _ in range(n):
    i = int(input())
    if i == 0:
        if len(min_heap) == 0:
            print(0)
        else:
            # 힙에서 최솟값 꺼내기
            print(heapq.heappop(min_heap))
    else:
        # 힙에 값 추가하기
        heapq.heappush(min_heap, i)