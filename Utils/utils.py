from random import randint
from flask import request
from datetime import datetime


def create_6_number_string():
    number = ''
    for i in range(0, 7):
        if i == 3:
            number = number + ' '
        else:
            number = number + str(randint(0, 9))

    return number


def add_addresse_to_db(coordinate, infos, path_to_picts):
    if not request.cookies.get('token'):
        return 401
    try:
        uname = db.select('''SELECT USER_NAME FROM USERS WHERE TOKEN=%s''', (request.cookies.get('token'),), 1)
        mean = 0
        db.execute('''INSERT INTO POSTS(COORDINATES, INFOS, AUTHOR_NAME, AUTHOR_IP, AUTHOR_TOKEN, DATE, MEANNESS) VALUES 
        (%s, %s, %s, %s, %s, %s, %s)''', (coordinate, infos, path_to_picts, uname[0], request.remote_addr,
                                          request.cookies.get('token'), datetime.now(), mean))

        return 200
    except Exception as e:
        print(e)
        return e