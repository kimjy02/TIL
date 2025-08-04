def calculator(idx):
    if idx != -1:
        if tree[idx][1] == '+':
            tree[idx][1] = tree[tree[idx][2]-1][1] + tree[tree[idx][3]-1][1]
        elif tree[idx][1] == '-':
            tree[idx][1] = tree[tree[idx][2]-1][1] - tree[tree[idx][3]-1][1]
        elif tree[idx][1] == '*':
            tree[idx][1] = tree[tree[idx][2]-1][1] * tree[tree[idx][3]-1][1]
        elif tree[idx][1] == '/':
            tree[idx][1] = tree[tree[idx][2]-1][1] // tree[tree[idx][3]-1][1]
        calculator(idx-1)
    else:
        print(tree[idx+1][1])
# 테스트 케이스의 개수는 10개
for k in range(10):

    N = int(input())
    tree = []

    for i in range(N):
        info = input().split()
        info[0] = int(info[0])
        if len(info) == 4:
            info[2] = int(info[2])
            info[3] = int(info[3])
        else:
            info[1] = int(info[1])
        tree.append(info)
    print(f'#{k+1} ', end ='')
    calculator(N-1)
