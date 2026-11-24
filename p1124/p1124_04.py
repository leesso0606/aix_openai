# 경제 전문가입니다.
# 2027년 주식 시세가 어떻게 될지 알려주는 프로그램을 구현하세요.
# 반도체주, 전력시설주, 우주항공주
# 500자 이내로 짧게

import os
from pathlib import Path
from dotenv import load_dotenv
import openai
from openai import OpenAI

# 파일 불러오기(디장고에서 .env불러올때 사용)
BASE_DIR = Path(__file__).resolve().parent.partent
envFile = BASE_DIR/'.env'

load_dotenv()
api_key = os.getenv('open_ai_key')


# 2. 챗지피티 연결

while True:
    txt_input = input("관심있는 관련주를 입력하세요(예: 반도체주)").strip()
    if txt_input : break
    print("입력되지 않았습니다.검색어를 입력해주세요.")
    print()

# 3. openai client 연결부분
client = OpenAI(api_key=api_key)

try:
    response = client.responses.creat(
        model = 'gpt-5.6',
        instructions = (
            "당신은 경제 전문가입니다."
            "당신에게 질문하는 사용자는 일반인 입니다."
            "2027년 주식 시세가 어떻게 될지 알려주는 프로그램을 간략하게 구현하세요."
            "관련주의 모든 주식을 먼저 말할 필요는 없습니다. 사용자가 질문하면 그때 말해주세요."

        ),
        input = f"{txt_input}에 대한 2027년 주식시세 예측을 말해주세요.",
        max_output_tokens = 1000,
    )
except openai.APIConnectionError as error:
    print(f'인터넷연결, 방화벽 문제 등 확인요청:{error}')
except openai.RateLimitError as error:
    print(f'요청량 또는 프로젝트 사용한도 확인:{error}')
except openai.APIError as error:
    print(f'인증, 권한 등 api 오류 확인 : {error}')


# 4. 결과 확인
result = response.output_text.strip()
if not result:
    raise RuntimeError("응답결과 내용이 없습니다.")

print(f'[2027년 {txt_input} 예측 ]')
print(result)
print("완료")