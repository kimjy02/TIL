import itertools

def calculator(k, cal):
    if cal == '+':
        number[k+1] += number[k]
    elif cal == '-':
        number[k+1] = number[k] - number[k+1]
    elif cal == '*':
        number[k+1] *= number[k]
    elif cal == '/':
        if number[k] < 0 and number[k]%number[k+1] !=0 :
            number[k+1] = (number[k] // number[k+1]) + 1
        else:
            number[k+1] = number[k] // number[k+1]


T = int(input())    # T : 테스트 케이스 개수

for m in range(T):

    N = int(input())    # N : 숫자 카드 개수

    cal_cnt = list(map(int, input().split()))

    num = list(map(int, input().split()))

    cal = ['+', '-', '*', '/']
    cal_result = []
    for i in range(4):
        for j in range(cal_cnt[i]):
            cal_result.append(cal[i])
    same_cal = list(itertools.permutations(cal_result))
    cal_result_uni = list(dict.fromkeys(same_cal))

    calculator_result = []
    for j in range(len(cal_result_uni)):
        total = 0
        number = num[:]
        for k in range(len(cal_result)):
            calculator(k, cal_result_uni[j][k])
        total = number[-1]
        calculator_result.append(total)

    print(f'#{m+1} {(max(calculator_result) - min(calculator_result))}')

