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

# sql = " select * from stuscore"
# cursor.execute(sql)

# print(cursor.description) # 데이터의 컬럼명과, 타입을 알수 있음.
# columns = [col[0] for col in cursor.description]    # 컬러명 추출
# print(columns)  

# 3. 쿼리 작성
#  employees, emprank, not-equi를 사용하여 월급 등급을 출력하시오
# emp_name, salary, erank, low_salary, high_salary, hire_date 정보 출력
# --0~3999 E등급
# --4000~6999 D
# --7000~9999 C
# --10000~11999 B
# --12000~30000 A

# 디장고 -> html 정보 이동시 키:값 으로 전달됨(딕셔너리(dict) 타입) 
# sql = "select emp_name, salary, erank, low_salary, high_salary, hire_date from employees, emprank\
#         where salary between low_salary and high_salary"
sql = "select name, kor+eng+math total, sw from stuscore"
cursor.execute(sql)
# 컬러명 추출 -['NAME', 'TOTAL', 'SW']
columns = [col[0] for col in cursor.description]    
print(columns)

# # 4. 데이터 정보 전달
rows = cursor.fetchall()

# 4-1. 딕셔너리 형태로 변환
rows = [dict(zip(columns,row)) for row in rows]
print(rows)
# context = {'stulist':rows} -> 디장고 view에서 받는 정보 출력하는 것처럼.


# # 5. 데이터 출력
# for row in rows:
#     print(row)
# print(len(rows))

# 5-1 insert, delete, update 할 경우
# conn.commit()
# conn.rollback() 

# 6. db정보 닫기
cursor.close()
conn.close()