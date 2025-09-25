T = int(input())
for _ in range(T):
    N = int(input())
    day_money = list(map(int, input().split()))
    total = 0
    max_value = 0

    for price in reversed(day_money):
        if price > max_value :
            max_value = price
        else:
            total += max_value - price

    print(total)
    # while day_money:
    #     max_value = max(day_money)
    #     if len(day_money) == 1:
    #         break
    #
    #     for i in range(0, (day_money.index(max_value))):
    #         total += max(day_money) - day_money[i]
    #
    #     for i in range(day_money.index(max_value)+1):
    #         day_money.pop(0)
    #
    # print(total)