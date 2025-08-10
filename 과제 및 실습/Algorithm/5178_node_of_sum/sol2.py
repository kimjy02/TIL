'''
    완전 이진 트리의 리프 노드에 1000 이하의 자연수가 저장되어 있고,
    리프 노드를 제외한 노드에는 자식 노드에 저장된 값의 합이 들어있다고 한다.

    다음은 리브 노드에 저장된 1, 2, 3이 주어졌을 때, 나머지 노드에 자식 노드의 합을 저장한 예

    N개의 노드를 갖는 완전 이진 트리의 노드 번호는 루트가 1번이 되며,
    같은 단계에서는 왼쪽에서 오른쪽으로 증가,
    단계가 꽉 차면 다음 단계의 왼쪽부터 시작된다.

    완전 이진 트리 특성상 1번부터 N번까지 빠지는 노드 번호는 없다.

    리프 노드의 번호와 저장된 값이 주어지면 나머지 노드에 자식 노드 값의 합을 저장한 후
    지정한 노드 번호에 저장된 값을 출력하는 프로그램을 작성하라.

    입력
        - 첫 번째 줄 : T - 테스트 케이스 수
        - 두 번째 줄 : N - 노드의 개수 / M - 리프 노드의 개수 / L - 값을 출력할 노드 번호
        - M개의 줄에 걸ㅊ쳐 리프 노드 번호와 1000 이하의 자연수가 주어짐

    출력
        - #T ans
'''

#import sys
#sys.stdin = open('sample_input.txt')

def calculator(N, list, L):
    if list[L] == 0 :
        if list[L*2] == 0:
            calculator(N, list, L*2)

        if L*2+1 <= N and list[L*2+1] == 0:
            calculator(N, list, L*2+1)

        if list[L*2] != 0 :
            if L*2+1 <= N:
                list[L] = list[L*2] + list[L*2+1]
                return
            else:
                list[L] = list[L*2]
                return

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    lst = [0 for i in range(N+1)]
    for _ in range(M):
        node, num = map(int, input().split())
        lst[node] = num
    # print(lst)
    calculator(N, lst, L)
    print(f'#{tc} {lst[L]}')