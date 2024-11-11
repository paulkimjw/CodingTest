def solution(arr):
    result = []
    for i in range(len(arr) - 1):
        if arr[i] != arr[i + 1]:
            result.append(arr[i])
    # 마지막 요소를 추가해주는 부분
    result.append(arr[-1])
    return result