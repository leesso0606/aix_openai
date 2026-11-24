import os
from dotenv import load_dotenv

# .env 파일에서 불러오기
load_dotenv()
print('api key:',os.getenv('open_ai_key'))

print('id:', os.getenv('id'))