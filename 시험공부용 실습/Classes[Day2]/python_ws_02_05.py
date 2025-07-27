class Theater:
    def __init__(self, name, total_seats, reserved_seats):
        self.name = name
        self.total_seats = total_seats
        self.reserved_seats = reserved_seats
    
    def reserve_seat(self):
        if self.reserved_seats < self.total_seats:
            print('좌석 예약이 완료되었습니다.')
            self.reserved_seats += 1
        else:
            print('좌석 예약이 실패되었습니다.')

class MovieTheater(Theater):
    total_movies = 0

    @classmethod
    def add_movie(cls):
        cls.total_movies += 1
        print('영화를 추가했습니다.')
    
    @staticmethod
    def description(theater_obj):
        print(f'영화관 이름: {theater_obj.name}\n총 좌석 수: {theater_obj.total_seats}\n예약된 좌석 수: {theater_obj.reserved_seats}\n총 영화 수:{MovieTheater.total_movies}')

Mega = MovieTheater('메가박스', 100, 0)
Mega.reserve_seat()
Mega.reserve_seat()
Mega.add_movie()
Mega.description(Mega)