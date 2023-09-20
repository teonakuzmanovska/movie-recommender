# Movie Recommendation Docker Services

This is a composition of microservices for movie recommendation. It consists of 3 services:
- movies service (CRUD operations for movies)
- reviews service (CRUD operations for movie review)
- recommendation service (logic for creating movies recommendations based on movie reviews)

## Getting Started

These instructions will help you set up and run the Movie Recommendation Service using Docker.

### Prerequisites

- Docker installed on your system

### Installation

1. Open terminal
3. Navigate to your desired location
2. Clone this repository:

   `git clone https://github.com/yourusername/movie-recommendation-service.git`

### Running

1. Open docker desktop
2. Navigate to the project directory in terminal
3. Run `docker compose up`

### Accessing The Endpoints
- `http://localhost:8000/docs` : Access the endpoint of movies service
- `http://localhost:8001/docs` : Access the endpoint of reviews service
- `http://localhost:8002/docs` : Access the endpoint of recommendations service



