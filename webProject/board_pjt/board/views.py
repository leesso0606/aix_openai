from django.shortcuts import render
import oracledb
from dotenv import load_dotenv
from pathlib import Path
import os
from board.models import Board

# 전역변수
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
env_file = BASE_DIR/'.env'
load_dotenv(env_file)
ora_conn = os.getenv('ora_conn')
print(env_file)

# SQLite
def blist2(request):
    qs = Board.objects.all()
    context={'blist':qs}
    return render(request,'blist2.html',context)





def blist (request):
    #  접속
    conn = oracledb.connect(ora_conn)
    cursor = conn.cursor()
    sql = '''select bno,nickname,btitle,bcontent,bgroup,bstep,bindent,bhit,bdate
            from board a,member b where a.id = b.id'''
    cursor.execute(sql)
    # 컬럼정보 - 대문자(소문자로 출력하고 싶으면 .lower())
    # columns = [col[0].lower() for col in cursor.description]
    columns = [col[0] for col in cursor.description]
    rows=cursor. fetchall()
    row_list = [dict(zip(columns, row)) for row in rows]

    print("확인:",columns)
    cursor.close()
    conn.close()
    context = {'blist':row_list}
    return render(request, 'blist.html', context)