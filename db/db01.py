#  파이썬에서 오라클 데이터를 조회하는 코딩 순서
# 오라클 데이터를 파이썬으로 가져오는 이유 : 보안도 있지만 오라클이 견디지 못함. 그리고 오라클에서 html(단말)로 바로 출력 못함.

import os
import oracledb
import dotenv
from dotenv import load_dotenv

#1. oracle 접속정보 - sql 더블클릭
load_dotenv()
ora_conn= os.getenv('ora_conn')
conn = oracledb.connect(ora_conn)

# 커서 연결 - sql 명령어 창 연결
cursor = conn.cursor()

# 실행문
# sql = 'select * from students'

# sql = 'select * from students where no=1'

sql = '''select school,grade,max(kor+eng+math) from students
group by school,grade
order by school'''

cursor.execute(sql)

# 데이터 연결
#  rows 타입은 [()]
rows = cursor.fetchall()
print(rows)
cursor.close()

# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# # row타입 ()
# row = cursor.fetchone()
# print(row)