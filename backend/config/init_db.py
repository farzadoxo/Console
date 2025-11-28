import sqlite3
import os
import datetime

def init_db(db_name: str = "db.sqlite3"):
    """Create the database and todos table if it doesn't already exist."""

    os.makedirs('backend/DATABASE_FILE',exist_ok=True)
    os.chdir(f'{os.getcwd()}/backend/DATABASE_FILE')
    connection = sqlite3.connect(f'db.sqlite3')
    cursor = connection.cursor()

    apps = ['games','tricks','dashboard','publishers','platforms']

    os.chdir(f'../')
    for i in apps:
        os.system(f'python3 manage.py makemigrations {i}')

    os.system('python3 manage.py migrate')

    try:
        cursor.execute("""INSERT INTO games_esrb (id , sign , ageRange )
                        VALUES ( 1 , 'A' , '18+'),
                                ( 2 , 'M' , '17+'),
                                ( 3 , 'T' , '12+'),
                                ( 4 , 'E10' , '10+'),
                                ( 5 , 'E' , '-')""")

        cursor.execute("""INSERT INTO games_genre (id , title )
                        VALUES ( 1 , 'Action'),
                                ( 2 , 'Simulation'),
                                ( 3 , 'RPG'),
                                ( 4 , 'Shooter'),
                                ( 5 , 'Sports')""")

        cursor.execute(f"""INSERT INTO publishers_publisher 
                        VALUES ( 1 , 'Rockstar Games' , '{datetime.datetime.now()}' , 'This company started at september', '/'),
                                ( 2 , 'EA' , '{datetime.datetime.now()}' , 'This company started at september' , '/'),
                                ( 3 , 'Sony' , '{datetime.datetime.now()}' , 'This company started at september' , '/'),
                                ( 4 , 'Microsoft' , '{datetime.datetime.now()}' , 'This company started at september' , '/'),
                                ( 5 , 'Konami' , '{datetime.datetime.now()}' , 'This company started at september' , '/')""")

        cursor.execute(f"""INSERT INTO platforms_platform 
                        VALUES ( 1 , 'Playstation5' , '{datetime.date.today().strftime('%Y-%m')}' , 'This platform created by bill gates in 1998 and release in 2000' , '/', 3),
                                ( 2 , 'Xbox series X' , '{datetime.date.today().strftime('%Y-%m')}' , 'This gaming console created by sont co at japan' ,'/', 4)""")
        

        cursor.execute(f"""INSERT INTO games_game
                        VALUES ( 1 , 'Red dead redemption 2' , '{datetime.datetime.now()}' , '/' , 2 , 1 , 1),
                                ( 2 , 'FC25' , '{datetime.datetime.now()}' ,'/' , 5 , 2 , 5)""")
        

        cursor.execute(f"""INSERT INTO tricks_trick
                        VALUES ( 1 , 'how to play the rdr2' ,'sl;dkfsl;dfl;skdf;lks;ldkf;sldkf;ksdkf;;', '{datetime.datetime.now()}' , 1 , 1)""")
        
        
        cursor.connection.commit()
    
    except Exception as error:
        print(f"ERROR >>> {error}")


    connection.close()


if __name__ == "__main__":
    init_db()