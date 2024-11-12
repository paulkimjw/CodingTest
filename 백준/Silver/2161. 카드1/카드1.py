from collections import deque

n = int(input())
cards = deque(range(1, n + 1))  # 1부터 n까지의 숫자를 큐로 만듦
discarded = []  # 버린 카드를 저장할 리스트

while len(cards) > 1:
    discarded.append(cards.popleft())  # 맨 위의 카드를 버림
    cards.append(cards.popleft())  # 그 다음 카드를 밑으로 옮김

# 결과 출력
print(" ".join(map(str, discarded + [cards[0]])))  # 버린 카드와 마지막 남은 카드 한 줄로 출력