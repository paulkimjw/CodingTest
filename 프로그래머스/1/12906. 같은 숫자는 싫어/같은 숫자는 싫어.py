def solution(arr):
    result = []
    for i in range(len(arr)):
        if i == 0:
            result.append(arr[i])
        elif arr[i] == arr[i-1]:
            continue
        else:
            result.append(arr[i])
    
    return result
