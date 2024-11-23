n = int(input())
for i in range(n):
    s = {}
    m = int(input())
    for j in range(m):
        input_str = input()  # 예시: "yonsei 10"
        key, value = input_str.split()  # 공백을 기준으로 문자열 분리
        s[key] = int(value)  # 딕셔너리에 키와 값을 추가 (기존 값이 있으면 덮어씀)
    max_key = max(s, key=s.get)
    print(max_key)