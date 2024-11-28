import psycopg2

conn = psycopg2.connect('postgresql://postgres:@localhost:5432/test_db')


# BEGIN (write your solution here)
def make_cars_table(conn):
    """Creates the cars table in the database."""
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS cars (
                id SERIAL PRIMARY KEY,
                brand VARCHAR(255) NOT NULL,
                model VARCHAR(255) NOT NULL
            )
        """)
        conn.commit()

def populate_cars_table(conn, cars):
    """Adds cars to the cars table."""
    with conn.cursor() as cur:
        for brand, model in cars:
            cur.execute("INSERT INTO cars (brand, model) VALUES (%s, %s)", (brand, model))
        conn.commit()

def get_all_cars(conn):
    """Retrieves all cars from the cars table, sorted by brand."""
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM cars ORDER BY brand")
        return cur.fetchall()

conn_string = "your_connection_string_here" 

try:
    with psycopg2.connect(conn_string) as conn:
        make_cars_table(conn)
        print(get_all_cars(conn))  
        cars = [('kia', 'sorento'), ('bmw', 'x5')]
        populate_cars_table(conn, cars)
        print(get_all_cars(conn)) 
except psycopg2.Error as e:
    print(f"PostgreSQL error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
# END
