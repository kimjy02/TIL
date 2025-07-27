movies =['Inception', 'Interstellar', 'Dunkirk', 'Tenet']
ratings = [9, 8.5, 7.5, 6]
movie_rating =[]
for movie, rating in zip(movies, ratings):
    movie_rating.append({
        'title':movie, 'rating':rating
    })
print(movie_rating)

def get_high_rated_movies():
    threshold = round(float(input('Enter the rating threshold: ')),1)
    print(f'Movies with a rating {threshold} or higher:')
    for movie in movie_rating:
        if movie['rating'] >= threshold:
            print(movie['title'])
        else:
            continue
    
get_high_rated_movies()