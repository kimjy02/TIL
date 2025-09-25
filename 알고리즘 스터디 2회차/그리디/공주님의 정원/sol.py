N = int(input())

flowers = []
for _ in range(N):
    flowers.append(list(map(int, input().split())))

# print(flower)

for flower in flowers:
    if flower[0] == 3 and flower[1] == 1:
