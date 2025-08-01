def perm(selected, remain):  
    '''
    Args:
        selected: 선택된 값 목록
        remain: 선택되지 않고 남은 값 목록
    '''
    # 모든 요소를 선택할 것이니... 나머지가 없을 때까지
    if len(selected) == 3:
    # if len(remain) == 3:
    # if not remain:
        print(*selected)
    else:    # 아직 선택할 수 있는 요소들이 남아 있다면!
        for idx in range(len(remain)):     # 그 요소를 모두 순회하면서
            # idx 번쨰의 요소를 선택
            select_item = remain[idx]
            # 선택된 idx번째를 제외한 remain을 만들자. (진짜 나머지 리스트)
            remain_list = remain[:idx] + remain[idx+1:]
            perm(selected + [select_item], remain_list)
# 초기 호출로 빈 리스트와 [1, 2, 3] 리스트 사용
perm([], [1, 2, 3, 4, 5, 6])
