def solution(n):
    n = list(str(n))
    n.reverse()  # 리스트 자체를 뒤집음
    return [int(d) for d in n]  # 문자열을 다시 정수로 바꿔줌