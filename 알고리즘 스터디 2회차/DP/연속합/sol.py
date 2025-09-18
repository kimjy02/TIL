'''
    n개의 정수로 이루어진 임의의 수열
    이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 가장 큰 합 구하기
    단, 한 개 이상 선택해야 함
    
    ex) 10 -4 3 1 5 6 -35 12 21 -1 : 12+21=33
    
    [입력]
        1. 1 <= n : 정수 개수 <= 100000
        2. -1000 < n개의 정수 < 1000 
    
    [출력]
        연속된 몇 개의 수를 선택해서 구할 수 있는 가장 큰 합
'''
from collections import deque

n = int(input())

lst = deque(map(int, input().split()))

def function(lst):
    sum_list = []
    wait = 0
    if max(lst) <= 0:
        return max(lst)

    while lst:

        num = lst.popleft()
        if num >= 0 and len(lst) != 0 and lst[0] >= 0 :
            wait += num

        elif num >= 0 and ((len(lst) != 0 and lst[0] < 0) or len(lst) == 0):
            wait += num
            sum_list.append(wait)

        else:
            wait = 0
            sum_list.append(num)

        # print(lst)

    max_value = max(sum_list)
    max_idx = sum_list.index(max_value)

    i = 1
    semi_total = 0
    while True:
        if max_idx - (i+1) >= 0 and sum_list[max_idx-i]+sum_list[max_idx-(i+1)] >= 0:
            semi_total += sum_list[max_idx-i]+sum_list[max_idx-(i+1)]
            i += 2

        else: break

    i = 1
    while True:
        if max_idx + (i+1) <= len(sum_list)-1 and sum_list[max_idx+i]+sum_list[max_idx+(i+1)] >= 0:
            semi_total += sum_list[max_idx+i]+sum_list[max_idx+(i+1)]
            i += 2

        else: break

    return (semi_total + max_value)

print(function(lst))