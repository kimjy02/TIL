import sys
sys.stdin = open('input.txt')

'''
    저는 주 언어가 파이썬이고,
    알고리즘을 처음엔 C로 시작했지만,
    자바로 어느정도 알고림 하다가
    메인은 파이썬으로 사실 계속하고 있어요... 
    
    데이터트랙에서는 알고리즘 코드 자체를
    파이썬 방식으로 설명하고 있습니다.
    
    근데? 그래도 된다고 판단한 이유는?
    데이터 트랙은 IM 따고 들어왔음.
    -> 그리고, 후반부도 쭉, 파이썬으로 데이터 분석하고
    AI작업하고 기타등등 파이썬으로 엄청 써댈거임
    
    그래서 파이썬에 익숙해지는게 중요함

    파이썬 트랙에서는
    기본적으로 이러한 파이썬의 모든 기능을 다 봉인했을겁니다.
    
    왜? index로 다루는법부터,
    자료구조를 구현하고,
    데이터의 크기를 계산하고
    할줄 아는것부터 시작해야하니까.
'''


def search(x, y):
    '''
        return: (최대수익, (그 수익을 얻어낸 좌표 들)
    '''
    now_set = data[x][y:y+M]
    # 지금 있는 이 모든 값들을 다 제곱값으로 일단 계산해
    case = sum(map(lambda x: x*x, now_set))
    def perm(arr, r, cnt, acc):
        nonlocal case

        if cnt > C:
            acc -= arr[r-1] * arr[r-1]
            if acc > case:
                case = acc
            return

        if r == M:
            case = max(case, acc)
            return
        else:
            for i in range(r, M):
                item = arr[i]
                arr[i], arr[r] = arr[r], arr[i]
                perm(arr, r+1, cnt+item, acc+item*item)
                arr[i], arr[r] = arr[r], arr[i]


    # 근데 요래가지곤, 우리가 원하는 꿀의 양 C에 대한 조건 처리 못함

    acc = sum(now_set)  # 꿀 선택한 양
    if acc > C:
        case = 0
        # 다른 조사 -> 내 now_set에 대한 순열
        perm(data[x][y:y+M], 0, 0, 0)
    # x, y
    # x, y + 1
    # x, y + 2...
    # x, y + M
    print(now_set, case, list(zip([x] * M, range(y, y+M))))
    return case, list(zip([x] * M, range(y, y+M)))

T = int(input())
for tc in range(1):
    # 벌통 크기: N, 개수: M, 최대 양: C
    # 3 <= N <= 10, 1 <= M <= 5, N >= M, 10 <= C <= 30
    N, M, C = map(int, input().split())
    # 각 칸별 꿀의 양
    data = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    # 모든 가능한 M개 연속 구간의 최대 수익 구하기
    acc_list = []
    for x in range(N):
        for y in range(N-M+1):
            acc_list.append(search(x, y))
    # 각 좌표에서 얻을 수 있는 최댓값
    acc_list.sort(reverse=True) # 오름 차순 정렬
    print(acc_list)

    # 완전 탐색
    for i in range(len(acc_list)-1):
        for j in range(i+1, len(acc_list)):
            a, b = acc_list[i], acc_list[j]
            set_a, set_b = set(a[1]), set(b[1])
            sum_val = a[0] + b[0]

            # 두 구간 안겹치면 결과 갱신
            if not set_a & set_b and sum_val > result:
                result = sum_val
    print(result)
