for tc in range(1, 11):
    N = int(input())
    password = input().split()          # 굳이 int로 바꿀 필요도 없음 (문자열로 처리해도 됨)
    M = int(input())
    cmd = input().split()

    idx = 0
    while idx < len(cmd):
        c = cmd[idx]

        if c == 'I':
            x = int(cmd[idx + 1])
            y = int(cmd[idx + 2])
            # 삽입할 값들
            vals = cmd[idx + 3 : idx + 3 + y]
            for i in range(y):
                password.insert(x + i, vals[i])
            idx += 3 + y

        elif c == 'D':
            x = int(cmd[idx + 1])
            y = int(cmd[idx + 2])
            # x 다음부터 y개 삭제인지, x부터 y개 삭제인지는 문제 정의에 맞춰 조정
            del password[x + 1 : x + 1 + y]
            idx += 3

        elif c == 'A':
            y = int(cmd[idx + 1])
            vals = cmd[idx + 2 : idx + 2 + y]
            password.extend(vals)
            idx += 2 + y

    print(f'#{tc}', *password[:10])
