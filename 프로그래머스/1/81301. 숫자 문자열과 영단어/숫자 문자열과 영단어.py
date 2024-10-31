def solution(s):
    answer = ""
    dic = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 
           'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    
    i = 0
    while i < len(s):
        if s[i].isdigit():  # 숫자인 경우 바로 추가
            answer += s[i]
            i += 1
        else:  # 영단어를 숫자로 변환
            for word, num in dic.items():
                if s[i:i+len(word)] == word:  # 영단어가 일치하면
                    answer += num
                    i += len(word)
                    break
    
    return int(answer)