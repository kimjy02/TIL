import sys
sys.stdin = open('input.txt')

from collections import deque

def BFS(start_vertex):
    visited = set()
    # 후보군을 저장
    # deque는 첫번째 인자로 iterable 객체를 받는다.
    queue = deque([(start_vertex, 0)])  # (노드, 단계)
    visited.add(start_vertex)

    level_dict = {}  # 각 노드의 깊이(cnt)를 저장
    level_dict[start_vertex] = 0

    while queue:
        node, cnt = queue.popleft()

        # 내 인접 리스트에서 인접 정점 찾아서 순회
        for neighbor in adj_list.get(node, []):
            # 해당 정점 아직 방문한적 없다면
            if neighbor not in visited:
                visited.add(neighbor)   # 방문 예정 표시
                queue.append((neighbor, cnt + 1))  # 다음 레벨로
                level_dict[neighbor] = cnt + 1
                # print(cnt)
    # print(level_dict)
    max_depth = max(level_dict.values())

    deepest_nodes = [node for node, depth in level_dict.items() if depth == max_depth]

    return max(deepest_nodes)

for k in range(10):
    L, S = map(int, input().split())  # L : 데이터 길이, S : 시작점
    nodes = list(map(int, input().strip().split()))     # {from, to, from, to, ...}

    adj_list = {}

    # 0번 idx는 from, 1번 idx는 to, 2번 idx는 from, ...
    for i in range(0, len(nodes), 2) :    # 2씩 증가하면서 from, to 저장
        if nodes[i] not in adj_list.keys():  # from (dict의 key)가 존재하지 않으면
            adj_list[nodes[i]] = []          # 빈 리스트 추가

        adj_list[nodes[i]].append(nodes[i+1])  # from의 value list에 추가

    print(f'#{k+1} {BFS(S)}')