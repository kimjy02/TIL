def get_minimum_coins_backtrack(coins, change):
    coins.sort(reverse=True)
    min_coins = change     # 최소 동전 개수
    result = {}     # 최저의 조건을 모은 result

    def backtrack(remain, target, curr_comb, acc):
        nonlocal min_coins,result
        '''
            remain : 0으로 만들어야 하는 남은 금액
            target : 현재 어느 동전을 사용할 것인가에 대한 index 
            curr_comb : 지금까지 만들어진 조합
            acc : 지금까지 사용한 동전의 개수
        '''
        # 기저 조건 : 남은 금액이 없다!
        if remain == 0:
            if acc < min_coins :     # 누적값이 min_coins보다 작을 때만!
                min_coins = acc      # 최솟값 갱신
                # curr_comb -> 딕셔너리 형태 (참조형)
                result = dict(curr_comb)
            return
        # 가지치기
        if acc >= min_coins:
            return
        # 유도 조건 : 남은 동전들에 대해서 모두 시도
        for idx in range(target, len(coins)):
            coin = coins[idx]
            if coin <= remain:
                # 여기서 만큼은 그리디하게 생각했을 때,
                # 100원을 1번, 2번, 3번, ... 반복 조사는의미없음
                # 200원 거슬러야 하는데 100원 거술러주고 남은걸
                # 50원으로 처리하라고 하면 2번 돼서
                # 어차피 조사하러 가봣자, 내가 원하는 최솟값 못 구함
                max_count = remain // coin
                curr_comb[coin] = max_count
                backtrack(remain - coin * max_count, idx + 1, curr_comb, acc + max_count)
                curr_comb[coin] -= max_count
    backtrack(change, 0, {}, 0)
    return result

# 사용 예시
coins = [1, 5, 10, 50, 100, 400, 500]  # 동전 종류
change = 882  # 잔돈

result = get_minimum_coins_backtrack(coins, change)
for coin, count in result.items():
    if count > 0:
        print(f"{coin}원: {count}개")
    