# # sys
# import sys
# # open을 사용해서 input 파일을 연다.
# sys.stdin = open('input.txt')

num = int(input())



from collections import Counter
# 리스트, 문자열, 튜플 등 반복 가능한 객체 안의 요소 개수를 세서 딕셔너리 형태로 반환

# 이 문제는 10개의 TC를 가진다.
for k in range(num):
    tc = input()     # 테스트케이스 번호 입력
    lst = [int(num) for num in str(tc)]     # 6개의 숫자를 하나씩 리스트에 추가
    
    counter = Counter(lst)
    triplet = 0
    run = 0

    # 먼저 triplet(같은 숫자 3개)
    for key in list(counter.keys()) :
        while counter[key] >= 3:
            triplet += 1
            counter[key] -= 3
    
    # run(연속된 숫자 3개)
    # 0~7까지 순회하면서 i, i+1, i+2가 모두 1개 이상 있을 경우 run
    for i in range(8):
        while counter[i] >= 1 and counter[i+1] >= 1 and counter[i+2] >= 1 :
            run += 1
            counter[i] -= 1
            counter[i+1] -= 1
            counter[i+2] -= 1

    if (triplet == 2) or (run == 2) or (triplet == 1 and run == 1) :
        print(f'#{(k+1)} true')
    else :
        print(f"#{k+1} false")
