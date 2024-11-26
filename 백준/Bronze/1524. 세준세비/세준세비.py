n = int(input())
for i in range(n):
    input()
    a, b = map(int, input().split())
    s_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    # 내림차순 정렬
    s_list.sort(reverse=True)
    b_list.sort(reverse=True)

    # 두 팀중 한쪽 팀의 병사가 전멸할때 까지 라운드 진행
    while s_list and b_list:
        if s_list[0] >= b_list[0]:
            b_list.pop(0)
        elif s_list[0] < b_list[0]:
            s_list.pop(0)
    if s_list:
        print('S')
    elif b_list:
        print('B')
    else:
        print('C')