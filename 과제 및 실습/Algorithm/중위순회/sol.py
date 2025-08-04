def inorder_traversal(idx):
    if idx <= N and tree[idx]:
        inorder_traversal(idx * 2)
        print(tree[idx], end='')
        inorder_traversal(idx * 2 + 1)

for j in range(10):

    N = int(input())
    tree = [0] * (N+1)

    for i in range(N):
        info = input().split()
        idx = int(info[0])
        tree[idx] = info[1]
    print(f'#{j+1} ',end ='' )
    inorder_traversal(1)
    print()