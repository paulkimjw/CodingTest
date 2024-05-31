#9655 돌게임

def stone_game(n):
    if n% 2 == 1:
        return "SK"
    else :
        return "CY"
    
    
n = int(input().strip())
print(stone_game(n))

    
    