n, w, L = map(int, input().split())

from collections import deque

truck = deque(map(int, input().split()))
bridge = deque([0] * w)
t = 0
bridge_weight = 0

while truck or bridge_weight:
    t += 1

    bridge_weight -= bridge.popleft()

    if truck and bridge_weight + truck[0] <= L:
        x = truck.popleft()
        bridge.append(x)
        bridge_weight += x
    else:
        bridge.append(0)

print(t)



