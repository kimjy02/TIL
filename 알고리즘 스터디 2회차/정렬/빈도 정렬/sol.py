'''
    모든 암호를 깨는 방법 [빈도 조사]
    메시지 획득
        이 메시지는 숫자 N개로 이루어진 수열
            숫자는 모두 C보다 작거나 같음
            이 숫자를 자주 등장하는 빈도순대로 정렬

        만약 수열의 두 수 X와 Y가 있을 때,
        X가 Y보다 수열에서 많이 등장하는 경우에는
        X가 Y보다 앞에 있어야 한다.
        만약 횟수가 동일하다면, 먼저 나온 것이 앞에 있어야 함
        => 이렇게 정렬하는 방법을 빈도 정렬

    수열이 주어졌을 때, 빈도 정렬을 하는 프로그램을 작성

   [입력]
   1. N : 메시지의 길이 / C : 메시지 안 최대 숫자
      (1 <= N <= 1,000 / 1 <= C <= 1,000,000,000)
   2. 메시지 수열
'''
from collections import Counter

N, C = map(int, input().split())
messages = list(map(int, input().split()))

# 숫자별 빈도 횟수 기록용
counter = Counter(messages)

# print(counter)
# 처음 등장한 인덱스 번호 기록용
index = {}
for i, m in enumerate(messages):
    if m not in index:
        index[m] = i

# print(index)

# counter 딕셔너리를 빈도 수가 가장 큰 순서대로 정렬,
# 만약 빈도 수가 동일하다면 index 딕셔너리에 담긴 처음 등장하는 인덱스 번호 순서대로 정렬
sorted_items = sorted(counter.items(), key=lambda x: (-x[1], index[x[0]]))
# print(sorted_items)

# result = []
# for num, count in sorted_items:
#     result.extend([str(num)] * count)
#
# print(" ".join(result))

for num, count in sorted_items:
    print(f"{num} " * count, end="")
