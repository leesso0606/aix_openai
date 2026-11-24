from django.shortcuts import render
from django.http import JsonResponse
from pathlib import Path
from dotenv import load_dotenv
import openai
from openai import OpenAI
import os

# Create your views here.

# 가고싶은 여행지를 입력하세요.>>경주
# [경주 여행코스]
# ## 경주 1박 2일 버스여행 코스  
# **기준:** 경주고속·시외버스터미널 도착 / 시내버스와 도보 이용

# ### 1일 차｜경주 역사유적과 야경
# - **오전:** 터미널 도착 → 버스 또는 도보로 **대릉원**
# - **점심:** 황리단길에서 **경주 쌈밥·한정식**
# - **오후:** **첨성대 → 계림 → 교촌마을 → 월정교**  
#   대부분 도보로 이동 가능합니다.
# - **간식:** 황남빵, 찰보리빵 또는 교리김밥
# - **저녁:** 황리단길 식당에서 한우물회·국밥
# - **야간:** 버스로 **동궁과 월지** 이동, 야경 관람
# - **숙소:** 황리단길·대릉원 인근 한옥 게스트하우스 또는 호텔  
#   *도보 관광과 식사가 편리합니다.*

# ### 2일 차｜불국사와 보문관광단지
# - **아침:** 숙소 조식 또는 황리단길 카페
# - **오전:** 시내버스 **10번·11번 계열** 이용 → **불국사** 관람  
#   약 40~50분 소요
# - **점심:** 불국사 주변 **산채정식·두부전골**
# - **오후:** 버스로 **보문관광단지** 이동  
#   보문호 산책, 경주세계문화엑스포공원 또는 카페 이용
# - **귀가:** 보문단지 → 경주터미널 버스 이동 → 귀가

# ### 버스여행 팁
# - 교통카드를 준비하고, 배차 간격이 길 수 있어 **카카오맵·경주버스정보**에서 실시간 확인하세요.
# - 동궁과 월지는 해 질 무렵 방문하면 좋습니다.
# - 짐은 터미널 보관함이나 숙소에 맡기면 편리합니다.
# - 석굴암까지 방문하려면 불국사에서 별도 버스를 이용하며, 이동시간을 1~2시간 더 잡으세요.
# 완료

# ajax
def ajax_data(request):
    # 1. 파일 불러오기
    BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
    envFile = BASE_DIR/'.env'
    # print(BASE_DIR)
    # print(envFile)

    load_dotenv(envFile)
    api_key = os.getenv('open_ai_key')
    # print("키확인:",api_key)

    # 2.chat gpt 연결해서 진행
    while True:
        txt_input = request.POST.get('data','').strip()
        if txt_input: break
        print('여행지를 입력하셔야 검색이 가능합니다.')
        print()

    #  3. OpenAI client 연결부분 - 글자생성, 이미지생성, 음성생성, 동영상생성 등 가능, 토큰이 많이들뿐
    client = OpenAI(api_key = api_key)
    try:
        response = client.responses.create(
            model = "gpt-5.6",
            instructions = (
                "당신은 여행설계 전문가 입니다."
                "여행 일정을 1박2일 코스를 설계해 주세요."
                "[버스여행]으로 알려주세요."
                "여행자가 이해하기 쉽게 간략하게 답합니다."
            ),
            input = f"{txt_input}를 가지고 [1박2일]- 버스여행, 여행지, 숙소, 식사 등을 제안해주세요.",
            max_output_tokens= 1000,
        )
    except openai.APIConnectionError as error:
        print(f'인터넷연결, 방화벽 문제 등 확인요청:{error}')
    except openai.RateLimitError as error:
        print(f'요청량 또는 프로젝트 사용한도 확인:{error}')
    except openai.APIError as error:
        print(f'인증, 권한 등 api 오류 확인 : {error}')

    #4. 결과확인
    result = response.output_text.strip()
    if not result:
        raise RuntimeError("응답결과 내용이 없습니다.")
    print(f'[{txt_input} 여행코스]')
    print(result)
    print("완료")
    context={'result':result}
    return JsonResponse(context)






#  
def tour(request):
    return render(request, 'tour.html')