seat_list = [['O']*3 for i in range(3)]
seat_list[0][2] = 'X'
seat_list[1][0] = 'X'
seat_list[1][2] = 'X'
seat_list[2][0] = 'X'
seat_list[2][2] = 'X'
print('현재 좌석 배치:')
for seat in seat_list:
    print(" ".join(seat))