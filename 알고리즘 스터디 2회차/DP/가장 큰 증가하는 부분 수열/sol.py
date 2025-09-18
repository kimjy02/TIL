N = int(input())

A = list(map(int, input().split()))

max_part_total = 0

for i in range(len(A)):
    process_list = [A[i]]

    for j in range(i+1, len(A)):
        print(A[j])
        if process_list[-1] <= A[j]:
            process_list.append(A[j])
            print(process_list)
        else:
            max_part_total = max(max_part_total, sum(process_list))
            print(process_list, max_part_total)
            # process_list.pop()
            # process_list.append(A[j])


print(max_part_total)

