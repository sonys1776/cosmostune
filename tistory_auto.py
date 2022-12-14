import requests

client_id = '57f00a68dee88319f9d8b25a0e32226d'
client_secret = '57f00a68dee88319f9d8b25a0e32226d39f7bed09279e4478418e54a472ce3700d726af8'
access_token = 'a397dac25f6204be28abaff6a89b5842_a7e845a822b6064daeccf6178659877f'
code = '2ac2591086e25ac83430451dd3d6f725cc1fb292315423957b72a38606b1f8408161658c'
redirect_uri = 'https://info4yours.tistory.com'
blogName = 'info4yours'
tag = '대추, 대추차 효능'  # 등록할 태그값, 쉼표로 구분
output = 'json'  # 고정값
grant_type = 'authorization_code'  # 고정값
visibility = 0  # 0은 비공개, 3은 공개 발행
category = 1018259


def getToken():
    url = 'https://www.tistory.com/oauth/access_token?'
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri,
        'code': code,
        'grant_type': grant_type
    }
    r = requests.get(url, data)
    print(r.text)


def getCategory():
    url = 'https://www.tistory.com/apis/category/list?'
    data = {
        'access_token': access_token,
        'output': output,
        'blogName': blogName,
    }
    r = requests.get(url, data)
    print(r.text)


def postWrite(content):
    title = '대추차 효능 알아보기'
    url = 'https://www.tistory.com/apis/post/write?'
    data = {
        'access_token': access_token,
        'output': output,
        'blogName': blogName,
        'title': title,
        'content': content,
        'visibility': visibility,
        'category': category,
        'tag': tag,
    }
    r = requests.post(url, data=data)
    print('자동 포스팅 성공')
    return r.text


if __name__ == '__main__':
    # getToken()    #최초 토큰 발급시에만 수행
    # getCategory()  #최초 카테고리 확인시에만 수행

    #f = open("새파일.txt", 'r')
   # while True:
   #     lines = f.readline()
    #    if not lines:
   #         break
       # print(lines)
    #f.close()
   # postWrite(lines)

   postWrite('대추차 효능 1. 수족 냉증 개선 대추차는 뜨거운 음식이고 여성들의 냉증을 개선시키기 쉽다. 대추차 효능 2. 암 예방 대추가 다량 함유된 플라보노이드와 베타카로틴은 암을 유발하는 각종 유해성분을 외부로 배출해 암 예방 및 예방에 효과적이다. 대추차 효능 3. 면역력 강화 대추는 따뜻한 성질을 가진 과일로 몸에 흡수되면서 몸을 따뜻하게 한다. 특히 겨울철에는 면역력을 높이기 위한 보약으로 여겨지며 기관지와 폐 건강에 긍정적인 효과가 있어 호흡기 질환을 개선해 기침 감기를 예방할 수 있다. 대추차 효능 4. 노화 방지 활성산소는 노화를 유발할 뿐만 아니라 인체에 축적되면 각종 질병에 걸릴 확률이 높아진다. 대추에는 베타카로틴이 풍부해 이런 활성산소를 효과적으로 제거해 노화를 방지한다. 대추차 효능 5. 불면증 개선 대추는 신경을 이완시키고 근육을 이완시키기 위해 많은 개선을 한다는 것을 공유하려고 노력하고 있다. 대추차의 섭취를 안정시켜 숙면을 유도하고 불면증 치료에도 도움이 된다고 한다. 대추차 효능 6. 염증 제거 근육과 뼈를 효과적으로 이완시켜 몸의 경직된 근육을 개선하고 뭉친 근육을 풀어줍니다. 또한 항염증 및 진통 효과가 있어 관절염이나 류머티즘을 개선할 수 있습니다. 대추차 효능 7. 이뇨 작용 대추차에는 이뇨 효과가 있으며 효율적인 노폐물 제거를 촉진합니다. 또한  몸을 튼튼하게 하는 효과가 있고 심혈관 질환과 숙취 예방에 일정한 효과가 있다고 해요.')
