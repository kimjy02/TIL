class MovieTheater:
    def __init__(self, name, total_seats):
        self.name = name
        self.total_seats = total_seats
        self.reserved_seats = 0
    
    def __str__(self):
        print(self.name)

    def reserve_seat(self):
        if self.reserved_seats < self.total_seats:
            self.reserved_seats += 1
            print('좌석 예약이 완료되었습니다.')
        else:
            print('좌석 예약이 실패되었습니다.')
    
    def current_status(self):
        print(f'총 좌석 수: {self.total_seats}\n예약된 좌석 수:{self.reserved_seats}')

Mega = MovieTheater('메가박스', 100)
Mega.reserve_seat()
Mega.reserve_seat()
Mega.reserve_seat()
Mega.current_status()