# def solution(n):
#     answer = n
#     for i in range(1,n//2+1) :
#         if n%i == 0:
#             answer += i
    
            
    
#     return answer

def solution(n):
    return n + sum([i for i in range(1,(n//2)+1) if n%i == 0])


