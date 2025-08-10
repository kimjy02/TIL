'''
    이진 트리에서 임의의 두 정점의 가장 가까운 공통 조상을 찾고,
    그 정점을 루트로 하는 서브 트리의 크기를 알아내는 프로그램을 작성하라.
    ex)
            1
           / \
          2   3
         /   /  \
        4   5     6
       /   / \   / \
      7   8  9  10 11
     /              \
    12              13
    위 이진 트리에서 정점 8과 13의 공통 조상 : 정점 3과 1 [2개]
    이 중 8, 13에 가장 가까운 것 : 정점 3
    정점 3을 루트로 하는 서브 트리의 크기(서브 트리에 포함된 정점의 수) : 8

    입력
        - 첫 번째 줄 : T - 테스트 케이스 수
        - 케이스의 첫 번째 줄 : V - 정점의 개수 / E - 간선의 개수 / N, M - 공통 조상을 찾는 두 개의 정점 번호
        - 케이스의 두 번째 줄 : E개의 간선 나열 [간선은 항상 부모 자식 순서로 표기]
            - ex) 위 예시를 이용하면 5 8 순서로 표기
        - 정점의 번호는 1부터 V까지의 정수 / 루트 정점은 항상 1번

    출력
        - #tc {가장 가까운 공통 조상의 번호} {그것을 루트로 하는 서브 트리의 크기}
'''

import sys
sys.stdin = open('input.txt')


def forefather_N(idx):
    global adj_list
    for k in range(len(adj_list)):
        lst = adj_list.get(k)
        if lst == None:
            pass
        else:
            for j in range(len(lst)):
                if lst[j] == idx:
                    parent[0].append(k)
                    forefather_N(k)
                else:
                    pass


def forefather_M(idx):
    global adj_list
    for k in range(len(adj_list)):
        lst = adj_list.get(k)
        if lst == None:
            pass
        else:
            for j in range(len(lst)):
                if lst[j] == idx:
                    parent[1].append(k)
                    forefather_M(k)
                else:
                    pass

def sub_tree_count(idx):
    global sub_tree_cnt
    global adj_list
    if len(adj_list.get(idx)) > 0:
        sub_tree_cnt += len(adj_list.get(idx))
        node_list = adj_list.get(idx)
        for i in range(len(node_list)):
            sub_tree_count(node_list[i])
    else:
        pass


T = int(input())    # T : 테스트 케이스 개수

for tc in range(1, T+1):
    V, E, N, M = map(int, input().split()) # V : 정점의 개수 / E : 간선의 개수 / N, M : 공통 조상을 찾는 두 개의 정점 번호
    forefather = []
    # print(V_num_list)
    adj_list = {i: [] for i in range(1, V+1)}
    # for i in range(1, V+1):
    #     adj_list[i] = []
    # print(adj_list)

    info = list(map(int, input().split()))  # info : 간선 정보

    for i in range(0, len(info), 2):       # 인접 리스트 생성
        adj_list[info[i]].append(info[i+1])
    print(adj_list)

    parent = [[] for i in range(2)]
    # print(parent)
    forefather_N(N)
    forefather_M(M)
    print(parent)

    for i in range(-1, -(min(len(parent[0]),len(parent[1]))+1), -1):
        if min(len(parent[0]),len(parent[1])) == 1:
            nearest_node = parent[0][i]
            break
        if parent[0][i] == parent[1][i]:
            pass
        else :
            nearest_node = parent[0][i+1]
            break
    # print(nearest_node)

    # for i in range(len(parent[0])):
    #     for j in range(len(parent[1])):
    #         if parent[0][i] == parent[1][j]:
    #             forefather.append(parent[0][i])
    #             break
    #         else:
    #             pass
    # nearest_node = max(forefather)

    sub_tree_cnt = 1
    sub_tree_count(nearest_node)


    print(f'#{tc} {nearest_node} {sub_tree_cnt}')




# adj_list = {
#     1: [2, 3],
#     2: [4],
#     3: [5, 6],
#     4: [7],
#     5: [9, 8],
#     6: [11, 10],
#     7: [12],
#     8: [],
#     9: [],
#     10: [],
#     11: [13],
#     12: [],
#     13: []
# }
# parent = []
# for i in range(len(adj_list)):
#     lst = adj_list.get(i)
#     if lst == None:
#         pass
#     else:
#         for j in range(len(lst)):
#             if lst[j]==8:
#                 parent.append(i)
#             else:
#                 pass
# print(parent)