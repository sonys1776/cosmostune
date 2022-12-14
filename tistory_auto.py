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

   # postWrite('<h3>사과 효능 1. 대장암 예방</h3> <p>사과는 파이토케미칼 성분이 들어있어 항산화 특성이 뛰어나 암 발생 위험을 줄여준다고 합니다. 특히 사과마다 성분이 순해 껍질째 먹으면 유용한 기능을 발휘한다고 합니다.</p>

<h3>사과 효능 2. 동맥경화 예방</h3>

<p>사과는 섬유질이 풍부하여 동맥경화를 예방합니다. 왜냐하면 식이섬유는 혈관에 축적된 나쁜 콜레스테롤을 제거하고, 이로운 효과가 있는 콜레스테롤을 증가시키며, 동맥경화를 예방하기 때문입니다.</p>

<h3>사과 효능 3. 노화 방지</h3>

<p>사과를 먹으면 아름다워진다 말이 전해지면서 비타민C가 많이 포함되어 우리 몸에 있는 반점과 주근깨가 생기는 것을 막고 항상 얼굴을 밝게 해주고 피부를 생기 있게 해주는 역할을 합니다.</p>

<h3>사과 효능 4. 면역력 경화</h3>

<p>사과는 면역력을 높이는 데 효과가 있다고 합니다. 왜냐하면 면역력을 돕는 비타민C가 상당량 들어 있고 이것은 하루 필요 섭취량을 충족하기 때문입니다.</p>

<h3>사과 효능 5. 체중 감량</h3>

<p>사과는 섬유질이 풍부한 음식이고 체중을 낮추는데 효과적입니다. 여러분은 사과의 섬유질을 섭취함으로써 몸 안의 콜레스테롤을 낮출 수 있습니다.</p>

<h3>사과 효능 6. 당뇨병 예방</h3>

<p>사과는 혈당 수치 증가를 제한하는데 효과가 있다고 합니다. 왜냐하면 사과는 수용성 섬유질을 함유하고 있어 몸 안의 수분을 흡수하고 음식물이 위에 오래 머물게 되고 소장 내 영양분 흡수가 늦어지게 되는데 그렇게 되면 혈당 수치의 증가가 낮아진다고 합니다.</p>

<h3>사과 효능 7. 고혈압 예방</h3>

<p>사과는 고혈압을 예방하는데 도움이 된다고 합니다. 왜냐하면 다른 과일들보다 사과는 칼륨이 풍부하기 때문에 나트륨을 몸 밖으로 빼내 고혈압을 돕고, 혈관을 건강하게 만드는 데 효과가 있다고 합니다.</p>

<h3>사과 효능 8. 치아 건강</h3>

<p>사과는 치아를 튼튼하게 하는 효과가 있어 천연 치솔이라고 불립니다. 왜냐하면 사과를 먹을때 통째로 먹다보면 잇몸을 튼튼하게 하고 입안의 침 분비를 일으켜 충치를 일으키는 각종 플라그를 제거하고 잇몸 염증을 개선하는데 도움이 되기 때문이라고 합니다.</p>


')