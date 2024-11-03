N, M = map(int, input().split())  # 두 값을 정수로 변환하여 N과 M에 할당
s = []  # 빈 리스트 선언
for i in range(N):
    s.append(input().split())  # 입력값을 리스트 형태로 추가

for i in range(M):
    q = "".join(input().split())  # 입력값을 문자열로 변환 (공백 제거)
    matches = []
    for j in range(N):
        t = int(s[j][0])
        song_start = "".join(s[j][2:5])  # 첫 세 음을 문자열로 변환 (공백 제거)
        if q == song_start:  # 첫 3개의 음과 비교
            matches.append(s[j][1])  # 노래 제목 추가
    
    if len(matches) == 0:
        print("!")
    elif len(matches) == 1:
        print(matches[0])
    else:
        print("?")