from collections import Counter

def most_frequent_letter(word):
    # 모든 문자를 대문자로 변환
    word = word.upper()
    
    # 알파벳 빈도수 계산
    frequency = Counter(word)
    
    # 가장 많이 사용된 알파벳 찾기
    most_common = frequency.most_common()
    
    # 최빈값이 여러 개 있는지 확인
    if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
        return '?'
    else:
        return most_common[0][0]

# 입력 받기
word = input().strip()
print(most_frequent_letter(word))
