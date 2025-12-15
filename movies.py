from fastapi import FastAPI
import csv

app = FastAPI()

class Movie:
    def __init__(self, id, title, genres):
        self.id = id
        self.title = title
        self.genres = genres

class  Link:
    def __init__(self, id: int, imdbId: int, tmbdId: int):
        self.id = id
        self.imdbId = imdbId
        self.tmbdId = tmbdId

class Rating:
    def __init__(self, userId, movieId, rating, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating
        self.timestamp = timestamp

class Tag:
    def __init__(self, userId, movieId, tag, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp

@app.get("/links")
def get_links():
    results = []
    with open('links.csv', mode='r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        next(reader)

        for row in reader:
            link = Link(id=row[0], imdbId=row[1], tmbdId=row[2])

            link_dict = link.__dict__

            results.append(link_dict)

        return results

@app.get("/movies")
def get_movies():
    results = []

    with open('movies.csv', mode='r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        next(reader)

        for row in reader:
            movie = Movie(id=row[0], title=row[1], genres=row[2])

            movie_dict = movie.__dict__

            results.append(movie_dict)

    return results

@app.get("/ratings")
def get_ratings():
    results = []
    with open('ratings.csv', mode='r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)

        for row in reader:
            rating = Rating(userId=row[0], movieId=row[1], rating=row[2], timestamp=row[3])
            results.append(rating.__dict__)

    return results

@app.get("/tags")
def get_tags():
    results = []
    with open('tags.csv', mode='r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)

        for row in reader:
            tag = Tag(userId=row[0], movieId=row[1], tag=row[2], timestamp=row[3])
            results.append(tag.__dict__)

    return results