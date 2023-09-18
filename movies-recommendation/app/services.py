from http.client import HTTPException
import requests

def get_recommendations():
    reviews_url = f"http://reviews_service:8001/movies-reviews/reviews"  # reviews_service - name of reviews container
    reviews_response = requests.get(reviews_url, verify=False)
#     print(movie_response)
    if reviews_response.status_code != 200:
        raise HTTPException(status_code=404, detail="Review not found")
    reviews = reviews_response.json()

    # sort reviews by type
    sorted_recommendations = sorted(reviews, key=lambda k: k['rating'], reverse=True)
    top_recommendations = sorted_recommendations[:3]
    
    # keep only movie and review
    top_movies=[]
    for review in top_recommendations:
        new_movie = {"movie" : review["movie"], "rating" : review["rating"]}
        top_movies.append(new_movie)

    # return movie and review
    return top_movies

# TODO: grupiraj reviews po movie id, za sekoj movie presmetaj average rating
# TODO: spored average rating sortiraj i vrati top 3
