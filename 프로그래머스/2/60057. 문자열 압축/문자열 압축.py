def solution(s) :
    if len(s) == 1:
        return 1
    
    min_len = len(s)

    for i in range(1, len(s) //2 +1):
        answer = ''
        now = s[0:i]
        count = 1

        for j in range(i, len(s), i):
            next = s[j:j+i]
            if now  == next:
                count +=1
            else:
                if count > 1:
                    answer += str(count) + now
                else:
                    answer += now
                now = next
                count = 1

        if count > 1:
            answer += str(count) + now
        else :
            answer += now

        min_len = min(min_len, len(answer))

    return min_len
