T = int(input())

for tc in range(1, T+1):
    N = int(input())

    count = [0 for _ in range(10)]
    num = 1
    while 0 in count:
        now_number = num * N
        now_number = list(str(now_number).strip())
        # print(now_number)
        for n in now_number:
            count[int(n)] += 1
        num += 1
        # print(count)
    answer = ''.join(now_number)
    print(f'#{tc} {answer}')

# count = [0 for _ in range(10)]
# count[0] += 1
#
# if 0 in count:
#     print(count)
# else:
#     print('X')
#
# print(count)