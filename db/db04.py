#  파이썬에서 오라클 데이터를 조회하는 코딩 순서

import os
import oracledb
import dotenv
from dotenv import load_dotenv

#1. oracle 접속정보 - sql 더블클릭
load_dotenv()
ora_conn= os.getenv('ora_conn')
conn = oracledb.connect(ora_conn)

# 검색
# kor_loan_status 테이블에서 지역별로 그룹핑 후 주택담보 대출을 출력하시오
cursor = conn.cursor()

sql = '''select region, sum(loan_jan_amt) from kor_loan_status where gubun = '주택담보대출' group by region'''
cursor.execute(sql)

rows = cursor.fetchall()
for row in rows:
    print('{}:{}'.format(*row))

print("종료")
cursor.close()