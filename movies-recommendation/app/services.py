from http.client import HTTPException
import requests

def get_all_reviews():
    reviews_url = f"http://reviews_service:8001/movies-reviews/reviews"  # reviews_service - name of reviews container
    reviews_response = requests.get(reviews_url, verify=False)
#     print(movie_response)
    if reviews_response.status_code != 200:
        raise HTTPException(status_code=404, detail="Review not found")
    reviews = reviews_response.json()

    return reviews

def group_revies_by_movies():
    # Create a dictionary to store reviews grouped by movie_id
    reviews = get_all_reviews()
    reviews_by_movie = {}

    for review in reviews:
        movie_id = review["movie_id"]
        rating = review["rating"]
        
        # Check if there's an entry for the movie in reviews_by_movie
        if movie_id in reviews_by_movie:
            reviews_by_movie[movie_id].append(rating)
        else:
            # Create a new entry with the first rating for the movie
            reviews_by_movie[movie_id] = [rating]

    # Return dictionary where keys are movie_ids, and values are lists of ratings for each movie.
    return reviews_by_movie

def calculate_average_ratings():
    # Create a dictionary to store average ratings for each movie
    reviews_by_movie = group_revies_by_movies()
    average_ratings = {}

    for movie_id, ratings in reviews_by_movie.items():
        if ratings:
            # Calculate the average rating for the movie
            average_rating = sum(ratings) / len(ratings)
        else:
            # If there are no ratings, set the average rating to 0
            average_rating = 0

        # Store the average rating in the dictionary
        average_ratings[movie_id] = average_rating

    return average_ratings

def separate_average_ratings():
    # Create a list to store separate dictionaries
    average_ratings = calculate_average_ratings()
    separate_dicts = []

    for movie_id, average_rating in average_ratings.items():
        movie_dict = {"movie_id": movie_id, "average_rating": average_rating}
        separate_dicts.append(movie_dict)

    return separate_dicts

def get_recommendations():
    # Sort recommendations by ratings and return top 3 recommendations
    separate_dicts = separate_average_ratings()
    sorted_recommendations = sorted(separate_dicts, key=lambda x: x["average_rating"], reverse=True)
    top_recommendations = sorted_recommendations[:3]

    return top_recommendations

