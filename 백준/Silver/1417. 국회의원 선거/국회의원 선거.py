import heapq

n = int(input())
dasom_votes = int(input())
other_votes = []

for _ in range(n - 1):
    heapq.heappush(other_votes, -int(input()))  # 최대 힙 구현을 위해 음수로 저장

bribed_count = 0

while other_votes and -other_votes[0] >= dasom_votes:
    max_votes = -heapq.heappop(other_votes)
    max_votes -= 1
    dasom_votes += 1
    bribed_count += 1
    heapq.heappush(other_votes, -max_votes)

print(bribed_count)