import heapq

n, h_centi, t = map(int, input().split())
giants = []

# 최대 힙 생성 (음수로 변환하여 사용)
for _ in range(n):
    height = int(input())
    heapq.heappush(giants, -height)

used = 0

while t > 0:
    tallest = -heapq.heappop(giants)  # 가장 큰 값 추출 (원래 값으로 변환)
    
    if tallest < h_centi:
        # 모든 거인이 센티보다 작아진 경우
        heapq.heappush(giants, -tallest)
        break
    
    if tallest == 1:
        # 더 이상 줄일 수 없는 경우
        heapq.heappush(giants, -tallest)
        break

    # 뿅망치를 사용하여 키를 절반으로 줄임
    new_height = tallest // 2
    heapq.heappush(giants, -new_height)
    used += 1
    t -= 1

# 결과 출력
tallest = -heapq.heappop(giants)
if tallest < h_centi:
    print("YES")
    print(used)
else:
    print("NO")
    print(tallest)