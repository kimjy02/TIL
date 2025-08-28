'''
    # 상원이의 생일 파티
    1. 자신과 친한 친구들에게 모두 초대장을 주기로 함.
    2. 여기에 친한 친구(1번 친구들)의 친한 친구인 경우에도 초대장 주기로 함
    => 총 몇 명의 친구들에게 초대장을 주어야 하는지 구하는 프로그램
    
    상원이의 반 : N명 / 각 학생들은 1번 ~ N번 / 상원이가 1번
    
    입력
        1. T : 테스트 케이스 수
        2. N : 반 친구들 수 / M : 친한 친구 관계의 수
        3. a b : a번 학생과 b번 학생이 서로 친한 친구 관계에 있다는 의미

    출력
        - #{tc} {상원이의 생일 파티 초대장을 받는 친구의 수}
        <상원이의 친구가 없을 수도 있다는 점 / 상원이는 초대장을 받는 사람에 속하지 않는다는 점>

'''
import sys
sys.stdin = open('sample_input.txt')

def invitation(adj_list):
    total = 0
    visited = []
    visited.append(1)
    if len(adj_list.get(1)) == 0:
        return total
    else:
        total += len(adj_list.get(1))
        # print(f'상원이 친구 수 : {total}')
        visited.extend(adj_list.get(1))
        # print(visited)
        for person in adj_list.get(1):
            for another in adj_list.get(person):
                if another not in visited:
                    total += 1
                    visited.append(another)
                # print(f'상원이 친구 {person}번의 친구 수의 합 : {total}')

    return total


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    adj_list = {v : [] for v in range(1, N+1)}
    # print(adj_list)
    friend_info = [list(map(int, input().split())) for _ in range(M)]
    for lst in friend_info:
        adj_list[lst[0]].append(lst[1])
        adj_list[lst[1]].append(lst[0])
    # print(adj_list)
    # print(friend_info)
    print(f'#{tc} {invitation(adj_list)}')