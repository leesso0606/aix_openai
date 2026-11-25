#  파이썬에서 오라클 데이터를 조회하는 코딩 순서

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

# insert-3가지 방법

# 1. 문자열 변수에 ''를 붙여서 처리
# no=2
# name = '홍길동'
# school = '디지털고'
# height=190
# kor=90
# eng=90
# math=90
# total=270
# avg=90
# specialty='python'
# rank=''

# sql = f"insert into stuscore2 values({no},'{name}','{school}',{height},{kor},{eng},{math},{total},{avg},'{specialty}','{rank}')"
# cursor.execute(sql)

# 2. 
# sql = "insert into stuscore2 (no,name,school) values(:no,:name,:school)"
# cursor.execute(sql,no=3, name="홍길자",school="신림고")
# print('저장완료')
# cursor.close()

# 3.
# in_list=[4,'홍홍홍','구로고']
# sql = "insert into stuscore2(no,name,school) values(:1,:2,:3)"
# cursor.execute(sql,in_list)
# cursor.close()



# ----------------------------------------

# # update
# sql = "update stuscore2 set height=:height, specialty=:specialty where no!=:no"
# cursor.execute(sql, no=1,height=190,specialty='c' )
# print('저장완료')
# cursor.close()
#------------------------------

# delete

sql="delete stuscore2 where no=:no"
cursor.execute(sql,no=2)
cursor.close()





print('프로그램 종료')
conn.commit() # 오라클에서 commit 와 같음. 이걸 해야 오라클 DB에 저장됨./ 커밋 안하면 다른 곳에서 오라클 저장, 수정 등 못함.
conn.close()
