n = int(input())  # 주의 개수 입력
schedule = []  # 전체 근무표 저장

for _ in range(n):
    week = []  # 한 주의 근무표
    for _ in range(4):
        week.append(input().split())  # 각 시간대의 근무자 정보 추가
    schedule.append(week)  # 주간 근무표를 전체 근무표에 추가

work_time = {}  # 각 근무자의 근무 시간 저장

for week in schedule:
    for idx, shift in enumerate(week):  # 각 주의 4개 시간대 반복
        hours = [4, 6, 4, 10][idx]  # 각 시간대의 근무 시간
        for person in shift:
            if person != "-":  # 근무자가 있는 경우
                if person not in work_time:
                    work_time[person] = 0
                work_time[person] += hours

# 근무 시간 공평성 판단
if len(work_time) == 0:
    print("Yes")  # 근무자가 아무도 없는 경우 공평함
else:
    max_time = max(work_time.values())
    min_time = min(work_time.values())
    if max_time - min_time <= 12:
        print("Yes")
    else:
        print("No")
