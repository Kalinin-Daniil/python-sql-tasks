import psycopg2

conn = psycopg2.connect('postgresql://postgres:@localhost:5432/test_db')


# BEGIN (write your solution here)
def add_movies(conn):
    """Adds two movies to the movies table."""
    cur = conn.cursor()
    cur.execute("INSERT INTO movies (title, release_year, duration) VALUES (%s, %s, %s)", ('Godfather', 1972, 175))
    cur.execute("INSERT INTO movies (title, release_year, duration) VALUES (%s, %s, %s)", ('The Green Mile', 1999, 189))
    conn.commit()
    cur.close()

def get_all_movies(conn):
    """Retrieves all movies from the movies table."""
    cur = conn.cursor()
    cur.execute("SELECT * FROM movies")
    movies = cur.fetchall()
    cur.close()
    return movies

conn_string = "your_connection_string_here" #  e.g., "dbname=your_dbname user=your_user password=your_password"

try:
    conn = psycopg2.connect(conn_string)
    print(get_all_movies(conn))
    add_movies(conn)
    print(get_all_movies(conn))
    conn.close()
except psycopg2.Error as e:
    print(f"PostgreSQL error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
# END
