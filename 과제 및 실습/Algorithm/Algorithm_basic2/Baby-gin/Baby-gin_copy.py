num = int(input())


# 이 문제는 10개의 TC를 가진다.
for k in range(num):
    tc = input()     # 테스트케이스 번호 입력
    lst = [int(num) for num in str(tc)]     # 6개의 숫자를 하나씩 리스트에 추가
    
    sorted_list = sorted(lst)
    triplet = 0
    run = 0
    i = 0
    set_sorted_list = []
    for n in sorted_list:
        if n not in set_sorted_list:
            set_sorted_list.append(n)
    while i < (len(set_sorted_list)-2) and len(set_sorted_list) >= 3:
        if (set_sorted_list[i+1] == (set_sorted_list[i]+1)) and (set_sorted_list[i+2] == (set_sorted_list[i]+2)) :
            triplet += 1
            sorted_list.remove(set_sorted_list[i])
            sorted_list.remove(set_sorted_list[i+1])
            sorted_list.remove(set_sorted_list[i+2])
            set_sorted_list.pop(i)
            set_sorted_list.pop(i)
            set_sorted_list.pop(i)
            set_sorted_list = []
            for n in sorted_list:
                if n not in set_sorted_list:
                    set_sorted_list.append(n)
        else :
            i += 1
    
    j = 0
    while j < (len(sorted_list)-2) and len(sorted_list) > 0:
        if (sorted_list[j+1] == sorted_list[j]) and (sorted_list[j+2] == sorted_list[j]) :
            run += 1
            sorted_list = sorted_list[:j] + sorted_list[j+3:]
        else:
            j += 1

    if (triplet == 2) or (run == 2) or (triplet == 1 and run == 1) :
        print(f'#{(k+1)} true')
    else :
        print(f"#{k+1} false")

# num = [1, 2, 3, 1, 2, 3]
# set_num = set(num)
# for val in set_num:
#     num.remove(val)

# print(num)