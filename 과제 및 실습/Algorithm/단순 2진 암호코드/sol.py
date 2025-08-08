# 단순 2진 암호코드
'''
    암호코드 : 8개의 숫자로 구성
        - 숫자 하나는 7개의 비트로 암호화되어 주어짐.
            => 암호코드 전체의 가로 길이는 56 (8 X 7)
                - 길이가 56이 아닌 코드 X
        - 0 : 0001101
        - 1 : 0011001
        - 2 : 0010011
        - 3 : 0111101
        - 4 : 0100011
        - 5 : 0110001
        - 6 : 0101111
        - 7 : 0111011
        - 8 : 0110111
        - 9 : 0001011

        - 올바른 암호코드
            - (홀수 자리의 합 X 3) + (짝수 자리의 합) = 10의 배수
            - ex) 88012346 : ((8+0+2+4)X3)+(8+1+3+6) = 60
        - 올바르지 않은 암호코드
            - ex) 19960409 : ((1+9+0+0)X3)+(9+6+4+9) = 58

    입력
        - 첫 번째 줄 : T - 테스트 케이스 수
        - 두 번째 줄 : N - 배열의 세로 크기 , M - 배열의 가로 크기
        - 3 ~ (N + 3)번째 줄 : 각 배열 값

    출력
        - #T answer
        - 잘못된 암호코드일 경우 0 출력
'''

# import sys
# sys.stdin = open('input.txt')

def password_solution(num):    # 7개의 비트를 숫자로 바꾸는 함수
    global num_list
    zero = [0,0,0,1,1,0,1]
    one = [0,0,1,1,0,0,1]
    two = [0,0,1,0,0,1,1]
    three = [0,1,1,1,1,0,1]
    four = [0,1,0,0,0,1,1]
    five = [0,1,1,0,0,0,1]
    six = [0,1,0,1,1,1,1]
    seven = [0,1,1,1,0,1,1]
    eight = [0,1,1,0,1,1,1]
    nine = [0,0,0,1,0,1,1]
    for i in range(len(num)):
        if num[i] == zero:
            num_list.append(0)
        elif num[i] == one:
            num_list.append(1)
        elif num[i] == two:
            num_list.append(2)
        elif num[i] == three:
            num_list.append(3)
        elif num[i] == four:
            num_list.append(4)
        elif num[i] == five:
            num_list.append(5)
        elif num[i] == six:
            num_list.append(6)
        elif num[i] == seven:
            num_list.append(7)
        elif num[i] == eight:
            num_list.append(8)
        elif num[i] == nine:
            num_list.append(9)

    return num_list     # 8개의 숫자를 리스트로 반환

def eight_password_divide(idx, num):  # 56개의 수가 들어있는 리스트를 8개씩 7개로 2차원 배열로 바꾸기
    # global number_list
    # if idx == 8:
    #     pass
    # else:
    #     for n in range(7):
    #         number_list[idx][n] = num[n]
    #     # print(number_list)
    #     for n in range(7):
    #         num.pop(0)
    #     eight_password_divide(idx+1, num)
    # return number_list
    return [num[i*7:(i+1)*7] for i in range(8)]


T = int(input())  # 테스트 케이스 수

for tc in range(1, T+1):
    N, M = map(int, input().split())
    num_list = []
    # number_list = [[0]*7 for i in range(8)]
    for _ in range(N):
        arr = list(map(int, input().strip()))
        if len(set(arr)) == 1:
            pass
        elif len(set(arr)) == 2 and len(num_list) == 0:
            unused_cnt = M - 56
            one_number = []
            for i in range(M):
                if arr[i] == 1:
                    one_number.append(i)
            last_idx = max(one_number)
            L = len(arr) - (last_idx + 1) # arr 리스트에서 필요한 번호 뒤 0 개수
            S = unused_cnt - L # arr 리스트에서 받을 값의 첫 번째 인덱스 번호
            num_56 = arr[S : last_idx + 1]
            number_list = eight_password_divide(0, num_56)
            num_list = password_solution(number_list)
            # print(num_list)
            if ((num_list[0]+num_list[2]+num_list[4]+num_list[6])*3 + num_list[1]+num_list[3]+num_list[5]+num_list[7]) % 10 == 0:
                print(f'#{tc} {sum(num_list)}')
            else:
                print(f'#{tc} 0')

        else:
            pass

