""" A simple movie database application """

from flask import Flask, render_template 
import movies_sqlite as db

app = Flask(__name__) 


@app.route('/')
def index():
    db_path = 'movies.db'
    conn = db.open_database(db_path)
    query = "SELECT * FROM movies ORDER BY release_date DESC LIMIT 5;"
    rows = db.retrieve_data_with_query(conn, query)
    db.close_database(conn)
    return render_template('index.html', rows=rows)

@app.route('/movies')
def movies():
    db_path = 'movies.db'
    conn = db.open_database(db_path)
    query = "SELECT * FROM movies ORDER BY release_date DESC;"
    rows = db.retrieve_data_with_query(conn, query)
    db.close_database(conn)
    return render_template('movies.html', rows=rows)

@app.route('/movie_detail/<int:movie_id>')
def movie_detail(movie_id):
    db_path = 'movies.db'
    conn = db.open_database(db_path)
    # Query to get the movie details
    query = f"SELECT * FROM movies WHERE movies.id = {movie_id};"
    rows = db.retrieve_data_with_query(conn, query)

    # Stars query to get the stars associated with the movie
    query_stars = f"SELECT stars.*, connections.role FROM stars,movies,connections WHERE connections.movie_id = {movie_id} AND connections.star_id = stars.id AND connections.movie_id = movies.id;"
    stars = db.retrieve_data_with_query(conn, query_stars)
    #print(f"Retrieved rows: {stars}")  # Debugging line
    db.close_database(conn)
    return render_template('movie_detail.html', rows=rows, stars=stars)

@app.route('/stars')
def stars():
    db_path = 'movies.db'
    conn = db.open_database(db_path)
    query = "SELECT * FROM stars ORDER BY stage_name;"
    rows = db.retrieve_data_with_query(conn, query)
    db.close_database(conn)
    return render_template('stars.html', rows=rows)

@app.route('/star_detail/<int:star_id>')
def star_detail(star_id):
    db_path = 'movies.db'
    conn = db.open_database(db_path)
    # Query to get the star details
    query = f"SELECT * FROM stars WHERE stars.id = {star_id};"
    rows = db.retrieve_data_with_query(conn, query)

    # Movies query to get the movies associated with the star
    query_movies = f"SELECT movies.*, connections.role FROM movies,stars,connections WHERE connections.star_id = {star_id} AND connections.movie_id = movies.id AND connections.star_id = stars.id ORDER BY movies.release_date DESC;"
    movies = db.retrieve_data_with_query(conn, query_movies)
    db.close_database(conn)
    return render_template('stars_detail.html', rows=rows, movies=movies)

if __name__ == '__main__':
    app.run(debug=True) 