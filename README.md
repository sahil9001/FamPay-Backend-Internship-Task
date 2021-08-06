# Fampay Backend Internship assignment (2021)

# Project Goal

 To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

# Basic Requirements:

- [x]  Server should call the YouTube API continuously in background (async) with some interval (say 10 seconds) for fetching the latest videos for a predefined search query and should store the data of videos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs and any other fields you require) in a database with proper indexes.

- [x]  A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
- [x]  A basic search API to search the stored videos using their title and description.
- [x]  Dockerize the project.
- [x]  It should be scalable and optimised.

# Bonus Points:

- [x]  Add support for supplying multiple API keys so that if quota is exhausted on one, it automatically uses the next available key.
- Make a dashboard to view the stored videos with filters and sorting options (optional)
- [x]  Optimise search api, so that it's able to search videos containing partial match for the search query in either video title or description.
    - Ex 1: A video with title *`How to make tea?`* should match for the search query `tea how`



# API Endpoints:

- GET / : Fetches the latest videos sorted in reverse chronological order of their publishing datetime.

- GET /search?q={search_query} : Searches the stored videos using their title and description.

- GET /search?q={search_query}&page={page_number} : Searches the stored videos using their title and description.

# TechStack:

- Python 3.6
- Django
- Django Rest Framework
- Docker
- Redis
- Celery

# Setup:

- Clone the repository

- Place `.env` file in the root directory of the project.

  - .env file should contain the following variables:
    - `DEBUG` = True
    - `SECRET_KEY` = django-insecure-k4xrycd%uo^x)suu-emn+0m=#!=_2f7!$ouj#!jk2t#*97lo=8
    - `SEARCH_URL` = "https://www.googleapis.com/youtube/v3/search"
    - `CELERY_BROKER_URL` = 'redis://redis:6379/0'
    - `YOUTUBE_API_KEY` = <YOUR_YOUTUBE_API_KEY_1>,<YOUR_YOUTUBE_API_KEY_2>

- Install [Docker](https://www.docker.com/get-started) (latest version).

- Run `docker-compose build` to build the docker images.

- Run `docker-compose up` to start the containers and app.


# Working:


We first setup the docker containers and then run the app. After this once the application has pulled the python requirements, the redis server starts along with the python app. Then celery worker is started to run the celery tasks, as to schedule this every 30 seconds a instance of celery-beat is started.

### Pictorial Representation
<p align="center">
  <img src="https://github.com/sahil9001/FamPay-Backend-Internship-Task/blob/master/images/Untitled%20Diagram.png" />
</p>


## Adding data to database:

- Celery beat is used to run the tasks in the background. This instance automatically adds the data fetched by the API to the database. For reference, go [here](https://github.com/sahil9001/FamPay-Backend-Internship-Task/blob/master/search_api/tasks.py).

- If the data is already present in the database, it won't be added again, else it will be added.

- Data is continuosly updated every 30 seconds as it fetches it from the API.


## API working:

- Used DRF to create the API endpoints and filters to filter out the data according to the timespan and the search query.

- For a GET request to `http://localhost:8000/` endpoint, it returns the latest videos sorted in reverse chronological order of their publishing datetime.

- For a GET request to `http://localhost:8000/search?q={search_query}` endpoint, it returns the stored videos using their title and description.