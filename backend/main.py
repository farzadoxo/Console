import os
from config.init_db import init_db

if __name__ == "__main__":
    try:
        os.chdir(f'{os.getcwd()}')
        init_db()
        os.system('python3 manage.py runserver')
        
    except Exception as error:
        print(f"ERROR >>>> : {error}")