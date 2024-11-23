import heapq

n, k = map(int, input().split())
arr = list(map(int, input().split()))
heapq.heapify(arr)

while k > 1:  # K번째 이전까지 pop하기 위해
    heapq.heappop(arr)
    k -= 1

print(heapq.heappop(arr))  # K번째 원소 출력