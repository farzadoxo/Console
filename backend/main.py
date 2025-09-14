import os
from config.init_db import init_db

if __name__ == "__main__":
    try:
        init_db()
        os.chdir(path=f'{os.getcwd()}')
        print(os.getcwd())
        os.system('python manage.py runserver')
        
    except Exception as error:
        print(f"ERROR >>>> : {error}")