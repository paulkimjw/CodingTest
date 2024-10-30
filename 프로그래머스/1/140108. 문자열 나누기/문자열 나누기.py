def solution(s):
    count = 0  # 분리된 문자열 개수를 셀 변수
    i = 0      # 문자열을 순회하기 위한 인덱스
    
    while i < len(s):
        x = s[i]  # 첫 번째 글자 저장
        x_count = 0
        other_count = 0
        
        # 왼쪽에서 오른쪽으로 진행하며 x와 다른 글자의 개수를 셈
        while i < len(s):
            if s[i] == x:
                x_count += 1
            else:
                other_count += 1
            i += 1
            
            # x와 다른 글자 수가 같아지면 멈추고 분리
            if x_count == other_count:
                break

        count += 1  # 분리된 문자열 개수 증가
    
    return count