def solution(s):
    # 문자 소문자화
    s = s.lower()
    print(s)
    # .count 함수 사용
    if s.count('y') == s.count('p'):
        return True
    else:
        return False