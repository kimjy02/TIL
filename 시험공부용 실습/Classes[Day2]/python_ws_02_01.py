class MovieTheater:
    def __init__(self, name, total_seats):
        self.name = name
        self.total_seats = total_seats
        self.reserved_seats = 0
    
    def __str__(self):
        print(self.name)

Mega = MovieTheater('메가박스', 100)
CGV = MovieTheater('CGV', 500)
Mega.__str__()
CGV.__str__()