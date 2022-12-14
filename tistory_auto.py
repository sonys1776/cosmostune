import requests

client_id = '57f00a68dee88319f9d8b25a0e32226d'
client_secret = '57f00a68dee88319f9d8b25a0e32226d39f7bed09279e4478418e54a472ce3700d726af8'
access_token = 'a397dac25f6204be28abaff6a89b5842_a7e845a822b6064daeccf6178659877f'
code = '2ac2591086e25ac83430451dd3d6f725cc1fb292315423957b72a38606b1f8408161658c'
redirect_uri = 'https://info4yours.tistory.com'
blogName = 'info4yours'
tag = '사과, 사과 효능'  # 등록할 태그값, 쉼표로 구분
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
    title = '사과 효능'
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

   postWrite(' 사과 효능 1. 대장암 예방  사과는 다른 과일에 비해 펙틴이 많이 함유돼 있어 지방산을 증가시켜 대장암을 예방하고 발암성 성분을 배출해 대장에 머물면서 장에서 항암 성분을 생산할 수 있도록 돕는다고 합니다. 그리고 사과 껍질에는 안토시아닌과 카테킨이 다량 함유돼 있어 폴리페놀과 동일한 항산화 특성을 갖고 있어 활성산소를 제거해 암 예방에 탁월하다고 합니다. 사과 효능 2. 동맥경화 예방 사과는 자주 섭취하게 되면 콜레스테롤 수치를 내려가게 한다고 합니다. 왜냐하면 수용성 섬유질을 포함하기 때문에 이는 콜레스테롤 지방을 낮추는 효과가 있기 때문이라고 합니다.사과 효능 3. 노화 방지 사과는 갈아서 주스로 마시게 되면 좋은 호르몬 기능을 유지하고 심신을 안정시켜 건강한 숙면을 유지하며 동시에 피부를 아름답게 만드는데 도움을 줍니다. 그리고 자외선 때문에 피부가 안좋을때 사과를 먹으면 효과가 있다고 합니다. 사과 효능 4. 면역력 경화 사과는 비타민 C가 많이 들어 있어 피로 회복에 매우 도움이 되고 스트레스와 빈혈 개선에도 도움이 된다고 할 수 있습니다. 사과 효능 5. 체중 감량 사과가 제공하는 섬유질은 칼로리를 태우지 않고 여러분을 배부르게 해줍니다. 이것은 우리 몸이 설탕이나 정제된 곡물보다 복잡한 섬유질을 소화하는 데 더 많은 시간을 보내 포만감이 지속되어 체중을 줄이는 효과가 있다고 합니다. 사과 효능 6. 당뇨병 예방 사과는 다른 과일과는 다르게 혈당이 높은 사람에게도 섬유질과 폴리페놀이 풍부하기 때문에 당뇨를 예방하는데 효과가 있다고 합니다. 사과 효능 7. 고혈압 예방 사과는 100g 당 100mg 이상의 칼륨을 함유하고 있어 나트륨을 몸 밖으로 배출하는 효과가 있고, 이 기능은 혈압 상승을 막아주어 고혈압을 예방하는 효과가 있다고 합니다. 사과 효능 8. 치아 건강 사과는 치아 건강에 도움이 된다고 합니다. 왜냐하면 사과를 먹을 때 여러번 반복해서 섭취하다보면 자연 칫솔 기능을 하여 치아 건강에 도움이 된다고 합니다.')
