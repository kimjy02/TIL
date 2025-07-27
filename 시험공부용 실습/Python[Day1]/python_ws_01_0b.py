numbers = list(range(1, 11))
for num in numbers:
    if num%2 == 0:
        print(num)
    elif num%2 == 1 and num != 5:
        print(f'{num}은(는) 홀수')
    elif num == 5:
        break
