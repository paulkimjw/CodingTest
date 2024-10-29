def solution(t, p):
    count = 0
    length_p = len(p)  # p의 길이
    
    for i in range(len(t) - length_p + 1):  # 한 글자씩 이동
        substring = t[i:i + length_p]
        if int(substring) <= int(p):
            count += 1
    
    return count