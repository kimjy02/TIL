# 테스트 케이스 수 입력
T = int(input())

for i in range(T):
    # 6장의 카드 수를 리스트로 입력
    lst = list(map(int, input().strip()))
    # 0~9 사이의 숫자 카드 개수 세기
    num = [0] * 10
    for j in lst:
        num[j] += 1
    baby_gin = 0
 
    # triplet 개수 세기
    for k in range(10):
        while num[k] >= 3:
            num[k] -= 3
            baby_gin += 1
    
    # run 개수 세기
    for l in range(8):
        while num[l] >= 1 and num[l + 1] >= 1 and num[l + 2] >= 1:
            num[l] -= 1
            num[l + 1] -= 1
            num[l + 2] -= 1
            baby_gin += 1
 
    if baby_gin == 2:
        print(f'#{i + 1} true')
    else:
        print(f'#{i + 1} false')
