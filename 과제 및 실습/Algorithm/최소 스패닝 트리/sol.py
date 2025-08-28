'''
    그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하라.
    최소 스패닝 트리 : 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리
    입력으로 주어지는 그래프는 하나의 연결 그래프임이 보장됨

    입력
        1. T : 테스트 케이스 수 (1 <= T <= 10)
        2. V : 정점의 개수 / E : 간선의 개수  (1 <= V <= 100,000 / 1 <= E <= 200,000)
        3. A B C : A번 정점과 B번 정점이 가중치인 C인 간선으로 연결되어 있다는 의미 (-1,000,000 <= C <= 1,000,000)

    출력
        - #{tc} {최소 스패닝 트리의 가중치}
'''

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_list = {v : [] for v in range(1, V+1)}
    informations = [list(map(int, input().split())) for _ in range(E)]
    for info in informations:
