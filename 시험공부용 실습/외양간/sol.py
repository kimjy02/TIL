import sys
sys.stdin = open('input.txt')


import heapq
'''
 * 첫 번째 줄: 테스트 케이스의 수 T
  * 각 테스트 케이스의 첫 번째 줄: 외양간의 수 N, 총 기간 M (1 ≤ N, M ≤ 50)
  * 다음 N개의 줄: 각 외양간의 일일 손실량 Li와 수리 기간 Di (1 ≤ Li, Di ≤ 25)
  * 다음 M개의 줄: d번째 날 밤에 공격받는 외양간의 번호 Ad (1 ≤ Ad ≤ N)
'''
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 외양간은 1번부터 [[loss, day], [loss, day] ... ]
    # data = [-1] + [list(map(int, input().split())) for _ in range(N)]
    # data = [list(map(int, input().split())) for _ in range(N)]
    # data.insert(0, 0) .pop(0) -> O(N)
    data = {}
    for idx in range(1, N+1):
        L, D = map(int, input().split())
        data[idx] = {'L': L, 'D': D}

    attack = [int(input()) for _ in range(M)]

    result = 0
    '''
       매일밤 (M일 동안) 공격을 받고, 수리를 한다.
       시작은 밤부터 시작하나? 오전부터 시작하나?
        - 세상은 아침부터 시작한다. 거기에 맞춰서 논리를 짜보자.
        - 자, 아침이밝았다. 농부는 무엇을 하느냐?
            - 외양간을 수리 할 것인지를 결정해야한다. 
            - 지금 수리가능한지 알아야겠네?
    '''
    # 1. 수리가 가능한가? - 1번에 1개 수리가능함
    can_fixed = True
    # 1-1. 수리가 가능한가? - 수리할 외양간이 있어야 함.
    broken_barns = set()    # 공격 당한 외양간은 다시 공격당할 일 없음.
    # broken_barns = [0] * (N+1)  # <- visited 처럼?
    
    # 완료되는 날의 정보를 저장
    '''
        repair = {
            '수리 완료되는 날짜': '수리되는 외양간 번호'
        }
    '''
    repair = {}

    # 데일리 로스율이 높은 애들부터 최대힙으로 처리
    hq = [] # 수리 대상여부를 판별할 후보군

    for day in range(1, M+1):   # 공격 시작!
        # 오전: 수리가 완료되거나, 새로운 수리를 시작
        # 1. 오늘 수리가 완료되는 경우가 있나?
        if day in repair:
            # 고장난 외양간 목록에서 그 수리 완료된 대상을 삭제
            fixed_barn = repair[day]
            broken_barns.remove(fixed_barn)
            can_fixed = True
        
        # 2. 수리가 가능한가?
            # 2-1. 수리 가능 여부 + 수리할 대상이 있는가
        if can_fixed and hq:  # 누구를 수리할건데?
            # 최대힙이 되도록 자료를 삽입 했다면
            # daily_loss, loss, barn = heapq.heappop(hq)
            _, _, barn_idx = heapq.heappop(hq)

            duration = data[barn_idx]['D']
            repair[day + duration] = barn_idx
            can_fixed = False

        # 오후 : 공격받고, 로스율 계산
        attack_idx = attack[day-1]   # 데이터는 0번부터 받았는데, 날짜 계산은 1더했으니까

        # 3. 공격 받기
        if attack_idx not in broken_barns:
            broken_barns.add(attack_idx)

            # 공격 받자마자 수리 후보군 hq에 삽입
            # daily_loss, loss, barn = heapq.heappop(hq)
            L = data[attack_idx]['L']
            D = data[attack_idx]['D']
            # 최대힙
            heapq.heappush(hq, (-L/D, -L, attack_idx))

        # 4. 하루 동안의 손실
        d_l = 0
        for barn_idx in broken_barns:
            d_l += data[barn_idx]['L']

        result += d_l

    print(f'#{tc} {result}')