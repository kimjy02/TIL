# movies리스트를 순회하며 영화 제목과 평점을 가진 딕셔너리 객체로 만들고 새로운 리스트에 담는다.
# get_high_rated_movies 함수를 정의하여, threshold 매개변수를 받아서 평점이 threshold 이상인 영화를 리스트로 반환한다.
# 사용자로부터 평점 기준을 입력받아, get_high_rated_movies 함수를 호출하여 해당 평점 이상인 영화를 출력한다.

# 아래에 코드를 작성하시오.
movies = ['Inception', 'Interstellar', 'Dunkirk', 'Tenet']
ratings = [9, 8.5, 7.5, 6]
movies_rating = [{'title': title, 'rating': rating} for title, rating in zip(movies, ratings)]

def get_high_rated_movies(threshold):
    print(f"Movies with a rating of {threshold:.1f} or higher:")
    for movie in movies_rating:
        if movie['rating'] >= threshold:
            print(movie['title'])

get_high_rated_movies(threshold=float(input('Enter the rating threshold: ')))
