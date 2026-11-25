import oracledb
import os
from dotenv import load_dotenv

# .env에서 정보 가져오기
load_dotenv()
print(os.getenv('ora_id'))
ora_conn=os.getenv('ora_connect')


# 오라클 db접속
# localhost : ip접속
# 1. 아이디, 패스워드 따로 접속
# conn = oracledb.connect(user='ora_user', password='1111',dsn='localhost:1521/XE')
# 2. ip 주소로 한번에 접속
# conn = oracledb.connect('ora_user/1111@localhost:1521/XE')
# 3. .env를 사용하여 정보 가져와서 접속
conn = oracledb.connect(ora_conn)


cursor = conn.cursor()
sql = 'select * from stuscore'
cursor.execute(sql)

rows = cursor. fetchall()
print(rows)

# 한줄씩 정보 가져오기
for row in rows:
    print('{},{},{},{},{},{},{},{},{},{},{}'.format(*row))