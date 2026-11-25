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

# while True:
#     kor = int(input("국어 점수 입력값 이상 점수를 검색함 (예로 50)"))
#     if kor.strip()=='':break
#     sql = f'select * from stuscore where kor>={kor}'
#     cursor.execute(sql)

#     rows = cursor.fetchall()
#     print(rows)
#     print("인원:",len(rows))

# cursor.close()
# print("종료")

# ----------------------------------

# kor+eng+math/3 평균 80 점 이상인 사람을 출력하시오

# while True:
#     avg = int(input("입력한 평균점수 이상인 사람을 출력합니다."))
#     if avg.strip() =="": break
#     sql = f"select * from stuscore where avg>={avg}"
#     cursor.execute(sql)

#     rows = cursor.fetchall()
#     print("2차배열")
#     print(rows)
#     print()
#     print("1차배열")
#     for row in rows:
#         print(row)
# cursor.close()
# print("종료")

# a 가 들어가 있는 학생을 모두 출력하시오--------------------------------------

# while True:
#     kor = input("입력 글자가 들어간 학생을 출력하시오.")
#     if kor=='':break
#     sql = f" select * from stuscore where lower(name) like '%{kor}%'"
#     cursor.execute(sql)

#     rows = cursor.fetchall()
#     print(rows)
#     print("인원:",len(rows))

# cursor.close()
# print("종료")

# 국어, 영어, 수학 : 역순정렬로 정렬하시오---------------------------------------

# while True:
#     data = input("정렬할 과목을 입력하세요.(kor, eng, math)>>")
#     if data.strip() == '국어': i='kor'
#     elif data.strip() == '영어': i='eng'
#     elif data.strip() == '수학': i = 'math'
#     else :break

#     sql = f"select * from stuscore order by {i} desc"
#     cursor.execute(sql)

#     rows = cursor.fetchall()
#     print(rows)
#     print("인원:",len(rows))
# cursor.close()
# print("종료")





