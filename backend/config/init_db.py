import sqlite3
import os
import datetime

def init_db(db_name: str = "db.sqlite3"):
    """Create the database and todos table if it doesn't already exist."""

    current_dir = os.getcwd()
    db_path = os.path.join(current_dir, 'DATABASE_FILE', db_name)

    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    # Establish a connection to the SQLite database
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()

    # inject data
        try:
            apps = ['games','tricks','dashboard']
            os.chdir(f'{os.getcwd()}')
        # make migrations
            for i in apps:
                os.system(f'python manage.py makemigrations {i}')
            
            os.system('python manage.py migrate')
            cur.execute("""INSERT INTO games_esrb (id , sign , ageRange )
                            VALUES ( 1 , 'A' , '18+'),
                                    ( 2 , 'M' , '17+'),
                                    ( 3 , 'T' , '12+'),
                                    ( 4 , 'E10' , '10+'),
                                    ( 5 , 'E' , '-')""")

            cur.execute("""INSERT INTO games_genre (id , title )
                            VALUES ( 1 , 'Action'),
                                    ( 2 , 'Simulation'),
                                    ( 3 , 'RPG'),
                                    ( 4 , 'Shooter'),
                                    ( 5 , 'Sports')""")

            cur.execute(f"""INSERT INTO games_publisher 
                            VALUES ( 1 , 'Rockstar Games' , '{datetime.datetime.now()}' , '/'),
                                    ( 2 , 'EA' , '{datetime.datetime.now()}' , '/'),
                                    ( 3 , 'Sony' , '{datetime.datetime.now()}' , '/'),
                                    ( 4 , 'Microsoft' , '{datetime.datetime.now()}' , '/'),
                                    ( 5 , 'Konami' , '{datetime.datetime.now()}' , '/')""")

            cur.execute(f"""INSERT INTO games_platform 
                            VALUES ( 1 , 'Playstation5' , '{datetime.datetime.now()}' , '/' , 3),
                                    ( 2 , 'Xbox series X' , '{datetime.datetime.now()}' , '/' , 4)""")
            

            cur.execute(f"""INSERT INTO games_game
                            VALUES ( 1 , 'Red dead redemption 2' , '{datetime.datetime.now()}' , '/' , 2 , 1 , 1),
                                    ( 2 , 'FC25' , '{datetime.datetime.now()}' ,'/' , 5 , 5 , 2)""")
            
            cur.connection.commit()



        except Exception as error:
            print(f"ERROR >>>> {error}")

if __name__ == "__main__":
    init_db()