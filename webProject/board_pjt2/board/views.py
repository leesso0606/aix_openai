from django.shortcuts import render
import oracledb
from dotenv import load_dotenv
from pathlib import Path
import os
# Create your views here.
# 전역변수
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
env_file = BASE_DIR/'.env'
load_dotenv(env_file)
ora_conn = os.getenv('ora_conn3')
print(env_file)


def blist(request):
    #  접속
    conn = oracledb.connect(ora_conn)
    cursor = conn.cursor()
    sql = '''select bno, nickname, btitle,bcontent, bgroup,bstep,bindent, bhit, bdate\
        from board_board a, member_member b where a.id=b.id'''
    cursor.execute(sql)
    columns = [col[0].lower() for col in cursor.description]
    rows=cursor. fetchall()
    row_list = [dict(zip(columns, row)) for row in rows]
    cursor.close()
    conn.close()
    context = {'blist':row_list}
    return render(request, 'blist.html', context)