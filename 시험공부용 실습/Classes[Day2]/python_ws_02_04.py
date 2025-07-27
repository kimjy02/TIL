class MovieTheater:
    total_movies = 0
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

    def add_movie(self):
        MovieTheater.total_movies += 1
        print('영화가 성공적으로 추가되었습니다.')

    @staticmethod
    def description():
        print('이 클래스는 영화관의 정보를 관리하고 좌석 예약 및 영화 추가 기능을 제공합니다.')
        print('영화관의 이름, 총 좌석 수, 예약된 좌석 수, 총 영화 수를 관리합니다.')

class VIPMovieTheater(MovieTheater):
    def __init__(self, vip_seats, name, total_seats):
        super().__init__(name, total_seats)
        self.vip_seats = vip_seats

    def reserve_vip_seat(self):
        if self.vip_seats != 0:
            self.vip_seats -= 1
            print('VIP 좌석 예약이 완료되었습니다.')
            return True
        else:
            return False

    def reserve_seat(self):
        success = self.reserve_vip_seat()
        if not success:
            super().reserve_seat()
            print('예약 가능한 VIP 좌석이 없습니다.')

Mega = MovieTheater('메가박스', 100)
CGV = MovieTheater('CGV', 150)
Mega.reserve_seat()
Mega.reserve_seat()
CGV.reserve_seat()
Mega.add_movie()
CGV.add_movie()
Mega.current_status()
CGV.current_status()
print(f'총 영화 수: {MovieTheater.total_movies}')
MovieTheater.description()
