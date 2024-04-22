def solution(s):
    answer = True
    l=[]
    for i in s:
        if i=='(':
            l.append(i)
        else:
            if len(l)==0 or l.pop()!='(':
                return False
    if len(l)==0:
        return True
    return False