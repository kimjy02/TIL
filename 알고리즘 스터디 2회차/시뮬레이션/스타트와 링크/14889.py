N = int(input())

S = [list(map(int, input().split())) for _ in range(N)]

start = []
link = []
min_value = 10000000
def classification(idx):
    global min_value
    if len(start) == len(link) and len(start) == N//2:
        start_value = 0
        link_value = 0
        for i in start:
            for j in start:
                start_value += S[i][j]
        
        for i in link:
            for j in link:
                link_value += S[i][j]
        
        min_value = min(min_value, abs(start_value - link_value))
        return
        # print(f'start: {start}')
        # print(f'link : {link}')
        # return
    if len(start) != N//2:
        start.append(idx)
        classification(idx+1)
        start.pop()
    if len(link) != N//2:
        link.append(idx)
        classification(idx+1)
        link.pop()

classification(0)
print(min_value)