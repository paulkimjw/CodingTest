def solution(nums):
    unique_pokemons = set(nums)  # 중복 제거한 포켓몬 종류
    max_pokemon_count = len(nums) // 2  # 최대 가져갈 수 있는 포켓몬 수
    return min(len(unique_pokemons), max_pokemon_count)  # 둘 중 더 작은 값 반환