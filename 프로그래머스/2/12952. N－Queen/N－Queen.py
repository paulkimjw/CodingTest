#백트레킹 문제

def solution(n):
    answer = 0
    board = [-1] * n  # 각 행(row)에서 퀸이 위치한 열(column)을 저장

    def is_valid(row, col):
        for prev_row in range(row):
            prev_col = board[prev_row]
            # 같은 열이거나, 대각선 위치에 있으면 불가능
            if prev_col == col or abs(prev_col - col) == abs(prev_row - row):
                return False
        return True

    def backtrack(row):
        nonlocal answer
        if row == n:  # 모든 행에 퀸을 배치한 경우
            answer += 1
            return
        
        for col in range(n):
            if is_valid(row, col):  # 유효한 위치인지 확인
                board[row] = col  # 퀸 배치
                backtrack(row + 1)  # 다음 행 탐색
                board[row] = -1  # 백트래킹 (원상 복구)

    backtrack(0)  # 첫 번째 행부터 탐색 시작
    return answer