expression = list(map(str, input().split('-')))

# 2. '+'가 포함된 문자열 처리
sums = []
for part in expression:
    numbers = map(int, part.split('+'))
    sums.append(sum(numbers))

# 3. 첫 번째 값 - (나머지 합)
result = sums[0] - sum(sums[1:])
print(result)
