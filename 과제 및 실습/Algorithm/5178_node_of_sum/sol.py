# # import sys
# #
# # sys.stdin = open('sample_input.txt')
#
#
T = int(input())  # 테스트 케이스 수

for j in range(T):
    # N : 노드의 개수 / M : 리프 노드의 개수 / L : 값을 출력할 노드 번호
    N, M, L = map(int, input().split())

    # 트리 구조 기본 세팅
    tree = [0] * (N+1)

    for i in range(M) :
        idx, value = map(int, input().split()) # 리프 노드 번호, 그 노드에 들어갈 자연수
        tree[idx] = value

    # 리프 노드부터 위로 진행
    for num in range(len(tree), 1, -1):
        # 자식 노드가 2개인 경우
        if tree[num-1] == 0 and len(tree)-1 >= (num-1) * 2 + 1:
            tree[num-1] = tree[(num-1) * 2] + tree[(num-1) * 2 + 1]
        # 자식 노드가 1개인 경우
        elif tree[num-1] == 0 and len(tree)-1 < (num-1) * 2 + 1:
            tree[num - 1] = tree[(num - 1) * 2]
        else:
            pass

    print(f'#{j+1} {tree[L]}')
