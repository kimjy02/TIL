movies = ['Inception', 'Interstellar', 'Dunkirk', 'Tenet']

def get_movie_recommendation():
    rating = int(input("Enter your movie rating (0-10): "))
    if rating >= 9:
        print('Recommended movie: Inception')
    elif rating >= 8 and rating < 9:
        print('Recommended movie: Interstellar')
    elif rating >= 7 and rating < 8:
        print('Recommended movie: Dunkirk')
    else:
        print('Recommended movie: Tenet')

get_movie_recommendation()