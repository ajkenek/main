from fastapi import FastAPI, Depends
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from database import SessionLocal, Base

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Movie(Base):
    __tablename__ = "movies"
    movieId = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    genres = Column(String)

class Link(Base):
    __tablename__ = "links"
    movieId = Column(Integer, primary_key=True, index=True)
    imdbId = Column(Integer)
    tmdbId = Column(Integer)

class Tag(Base):
    __tablename__ = "tags"
    movieId = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, primary_key=True, index=True)
    tag = Column(String)
    timestamp = Column(Integer)

class Rating(Base):
    __tablename__ = "ratings"
    userId = Column(Integer, primary_key=True, index=True)
    movieId = Column(Integer, primary_key=True, index=True)
    rating = Column(Integer)
    timestamp = Column(Integer)

@app.get("/movies")
def get_movies(db: Session = Depends(get_db)):
    movies = db.query(Movie).all()
    return movies

@app.get("/links")
def get_links(db: Session = Depends(get_db)):
    links = db.query(Link).all()
    return links

@app.get("/tags")
def get_tags(db: Session = Depends(get_db)):
    tags = db.query(Tag).all()
    return tags

@app.get("/ratings")
def get_ratings(db: Session = Depends(get_db)):
    ratings = db.query(Rating).all()
    return ratings

@app.get("/movies")
def get_movies(db: Session = Depends(get_db)):
    movies = db.query(Movie).all()
    return movies