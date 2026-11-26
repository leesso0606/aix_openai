import os
import oracledb
from dotenv import load_dotenv

# 1. 오라클 불러오기
load_dotenv()
ora_conn = os.getenv('ora_conn')
# print(ora_conn)

# 2. db연결
conn = oracledb.connect(ora_conn)   # 아이콘을 더블클릭하여 프로그램 오픈
# print(conn)
cursor = conn.cursor()      # 입력창이 뜸
# print(cursor)

# 3. 쿼리 작성
sql = "select * from event"
cursor.execute(sql)

# 4. 데이터 벙보 전달
rows = cursor.fetchall()

# 5. 데이터 출력
for row in rows:
    print(row)

# 5-1 insert, delete, update 할 경우
# conn.commit()
# conn.rollback() 

# 6. db정보 닫기
cursor.close()
conn.close()