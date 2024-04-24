# def solution(array, commands):
#     answer = []
#     for command in commands:
#         temp_array = array[command[0]-1:command[1]]
#         temp_array.sort()
#         if len(temp_array) >= command[2]:
#             answer.append(temp_array[command[2]-1])
#         else:
#             answer.append(None)
#     return answer

def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(sorted(array[i-1:j])[k-1])
    return answer


### i,j,k = command 이렇게도 값을 넣을수 있다는점 ㄷㄷㄷㄷㄷ
