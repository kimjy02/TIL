'''
    입력
        - 첫 번째 줄 : T - 테스트 케이스 수
        - 두 번째 줄 : V - 정점의 개수 (10 이하 10000 이상)
                     E - 간선의 개수
                     N - 공통 조상을 찾는 두 개의 정점 번호 중 첫 번째
                     M - 공통 조상을 찾는 두 개의 정점 번호 중 두 번쨰
        - 세 번째 줄 : 간선 정보 ( 부모 자식 순서 )

    출력
        - #tc {가장 가까운 공통 조상의 번호} {그것을 루트로 하는 서브 트리의 크기}
'''

# import sys
# sys.stdin = open('input.txt')

def foreparent(idx, parent):
    for i in range(1, len(adj_list)+1):
        for j in adj_list.get(i):
            if idx == j:
                parent.append(i)
                foreparent(i, parent)

def nearest_foreparent(N_parent, M_parent):
    global nearest_node
    if min(len(N_parent), len(M_parent)) == 1:
        nearest_node = N_parent[len(N_parent)-1]
    else:
        for i in range(min(len(N_parent), len(M_parent))):
            if N_parent[len(N_parent)-1-i] == M_parent[len(M_parent)-1-i]:
                pass
            else:
                nearest_node = N_parent[len(N_parent)-i]
                break

def subtree(nearest_node):
    global subtree_node
    if adj_list.get(nearest_node) != None:
        for i in adj_list.get(nearest_node):
            subtree_node.append(i)
            subtree(i)
    else:
        return


T = int(input())  # 테스트 케이스 수
for tc in range(1, T+1):
    V, E, N, M = map(int, input().split())  # 위 주석 참고
    adj_list = {i : [] for i in range(1, V+1)}
    info = list(map(int, input().split()))
    # print(info)
    for i in range(0, len(info), 2):
        adj_list[info[i]].append(info[i+1])
    # print(adj_list)
    N_parent = []
    M_parent = []
    foreparent(N, N_parent)
    foreparent(M, M_parent)
    # print(N_parent)
    # print(M_parent)
    nearest_node = 0
    nearest_foreparent(N_parent, M_parent)
    # print(nearest_node)
    subtree_node = []
    subtree(nearest_node)
    # print(subtree_node)
    print(f'#{tc} {nearest_node} {len(subtree_node)+1}')


# adj_list = {1:[1, 2, 3], 2:[4, 5, 6]}
# for i in adj_list.values():
#     print(i)
