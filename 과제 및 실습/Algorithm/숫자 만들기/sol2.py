'''
    수식을 계산할 떼 연산자의 우선 순위는 고려하지 않고 왼쪽에서 오른쪽으로 차례로 계산한다.
    ex) [3, 5, 3, 7, 9]가 적힌 숫자판과 ['+' 2개, '-' 1개, '/' 1개]의 연산자 카드가 주어진 경우
        이 경우, 조합할 수 있는 결과는 총 12개, 최댓값과 최솟값의 차이를 출력

    제약 조건
        1. 시간 제한 : 최대 50개 테스트 케이스를 모두 통과하는 데 10초
        2. 게임 판에 적힌 숫자의 개수 N : 3 이상 12 이하의 정수
        3. 연산자 카드 개수의 총 합은 항상 N - 1이다.
        4. 게임 판에 적힌 숫자는 1 이상 9 이하의 정수
        5. 수식을 완성할 때 각 연산자 카드를 모두 사용해야 함
        6. 숫자와 숫자 사이에는 연산자가 1개만 들어감
        7. 완성된 수식을 계산할 때 연산자의 우선 순위는 고려하지 않고, 왼쪽에서 오른쪽으로 차례로 계산한다.
        8. 나눗셈을 계산할 땐 소수점 이하는 버린다.
        9. 입력으로 주어지는 숫자의 순서는 변경 X
        10. 연산 중의 값은 -100,000,000 이상 100,000,000 이하임이 보장됨

    입력
        첫 줄 : T - 총 테스트 케이스 개수
        다음 줄 : T개의 테스트 케이스
            테스트 케이스 첫번째 줄 : N - 숫자의 개수
            테스트 케이스 두번째 줄 : '+' '-' '*' '/' 순서대로 연산자 카드의 개수가 공백을 두고 주어짐
            테스트 케이스 세번째 줄 : 수식에 들어가는 N개의 숫자가 순서대로 공백을 두고 주어짐

    출력
        #t 답
            - 답 : 수식으로 얻은 결과값 중 최댓값과 최솟값의 차이
'''

import sys
sys.stdin = open('sample_input.txt')


def dfs(idx):
    global operator
    global num_list
    global total
    # global N
    if idx == N - 1:
        result_list.append(total)
        return

    next_num = num_list[idx+1]
    old_total = total

    if operator[0] > 0 :
        total += num_list[idx+1]
        operator[0] -= 1
        # print(total)
        dfs(idx+1)
        operator[0] += 1
        total = old_total

    if operator[1] > 0 :
        total -= num_list[idx+1]
        operator[1] -= 1
        # print(total)
        dfs(idx+1)
        operator[1] += 1
        total = old_total

    if operator[2] > 0 :
        total *= num_list[idx+1]
        operator[2] -= 1
        # print(total)
        dfs(idx+1)
        operator[2] += 1
        total = old_total

    if operator[3] > 0 :
        if total < 0 and total % num_list[idx+1] != 0:
            total = (total // num_list[idx+1])+1
        else:
            total = total // num_list[idx+1]
        operator[3] -= 1
        # print(total)
        dfs(idx+1)
        operator[3] += 1
        total = old_total

T = int(input()) # T : 테스트 케이스 개수

for tc in range(1, T + 1):
    N = int(input())    # N : 숫자의 개수
    operator = list(map(int, input().split()))    # operator : 연산자 +-*/ 순서대로 개수
    num_list = list(map(int, input().split()))    # num_list : 수식에 들어가는 N개의 숫자
    result_list = []
    total = num_list[0]
    dfs(0)
    print(f'#{tc} {max(result_list) - min(result_list)}')