def solution(k, dungeons):
    def dfs(k, dungeons, visited):
        max_dungeons = 0
        
        for i in range(len(dungeons)):
            if not visited[i] and k >= dungeons[i][0]:
                visited[i] = True
                max_dungeons = max(max_dungeons, 1 + dfs(k - dungeons[i][1], dungeons, visited))
                visited[i] = False
        
        return max_dungeons
    
    visited = [False] * len(dungeons)
    return dfs(k, dungeons, visited)




# 	1.	DFS(깊이 우선 탐색) 함수: dfs 함수는 현재 피로도 k, 던전 정보 dungeons, 방문 여부를 저장하는 visited 리스트를 인자로 받습니다.
# 	2.	탐험 가능한 던전 탐색: 모든 던전을 순회하면서 아직 방문하지 않았고 탐험 가능한 던전(k >= dungeons[i][0])을 찾습니다. 해당 던전을 방문하고 소모 피로도를 차감한 후, 재귀적으로 다음 던전을 탐험합니다.
# 	3.	최대 던전 수 갱신: 각 재귀 호출에서 탐험 가능한 던전 수를 계산하고 최대 값을 갱신합니다.
# 	4.	방문 초기화: 현재 던전 탐험이 끝나면 방문 여부를 초기화하여 다음 순서를 탐험할 수 있도록 합니다.