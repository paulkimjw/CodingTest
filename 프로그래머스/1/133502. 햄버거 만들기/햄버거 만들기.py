def solution(ingredient):
    stack = []
    count = 0

    for num in ingredient:
        stack.append(num)
        # 스택의 마지막 4개 요소가 1231인지 확인
        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            # 1231이 발견되면 1231 요소들을 pop하고 count 증가
            stack.pop()  # 1
            stack.pop()  # 3
            stack.pop()  # 2
            stack.pop()  # 1
            count += 1

    return count