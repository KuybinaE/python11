import pymysql
from pymysql.cursors import DictCursor

def connection():
    return pymysql.connect(
        host = '10.11.13.118',
        port = 3306,
        user= 'rybin_python',
        password='111111',
        database= 'rybin_Climbers',
        cursorclass= DictCursor
    )