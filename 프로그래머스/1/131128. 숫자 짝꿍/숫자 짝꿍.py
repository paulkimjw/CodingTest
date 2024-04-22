def solution(X, Y):
    #X와 Y에서 공통된 숫자를 찾기 위해 set() 연산을 사용
    xy = set(X) & set(Y)
    
    #공통된 숫자가 없으면 -1을 반환
    if not xy:
        return "-1"
    
    #공통된 숫자가 0만 있으면 0을 반환
    elif len(xy) == 1 and "0" in xy:
        return "0"
    
    #각 공통된 숫자를 X와 Y에서 나타나는 횟수중 더 작으 수만큼 반복하여 문자열 생성
    result = [n* min(X.count(n), Y.count(n))for n in xy]
    
    # result 문자열을 내림차순으로 정렬하여 반환
    return "".join(sorted(result, reverse = True))
