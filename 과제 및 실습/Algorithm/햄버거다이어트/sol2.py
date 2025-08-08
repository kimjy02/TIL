'''
    출력값 : 주어진 제한 칼로리 이하의 조합 중에서 가장 맛에 대한 점수가 높은 햄버거 점수
    제약조건
        - 같은 재료를 여러 번 사용할 수 없음
        - 햄버거의 선호도 = 조합된 재료들의 맛에 대한 점수의 합
        - 햄버거 조합의 제한은 칼로리를 제외하고는 없다.

'''
def calories_calculator(start, taste_sum, calory_sum):
    global max_score

    if calory_sum > L:
        return
    max_score = max(max_score, taste_sum)

    if taste_sum > max_score:
        max_score = taste_sum

    for idx in range(start, len(calories)):
        calories_calculator(idx + 1, taste_sum + tastes[idx], calory_sum + calories[idx])

T = int(input())  # T : 테스트 케이스 수

for cnt in range(T):
    N, L = map(int, input().split())  # N : 재료의 수, L : 제한 칼로리
    tastes = []
    calories = []
    for _ in range(N):
        T, K = map(int, input().split())     # T : 맛에 대한 점수 , K : 칼로리
        tastes.append(T)
        calories.append(K)

    max_score = 0
    calories_calculator(0, 0, 0)
    print(f'#{cnt+1} {max_score}')
