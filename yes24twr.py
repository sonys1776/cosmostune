from base64 import encode
import requests
from bs4 import BeautifulSoup
import datetime as dt

client_id = '57f00a68dee88319f9d8b25a0e32226d'
client_secret = '57f00a68dee88319f9d8b25a0e32226d39f7bed09279e4478418e54a472ce3700d726af8'
access_token = 'a397dac25f6204be28abaff6a89b5842_a7e845a822b6064daeccf6178659877f'
code = '2ac2591086e25ac83430451dd3d6f725cc1fb292315423957b72a38606b1f8408161658c'
redirect_uri = 'https://info4yours.tistory.com'
blogName = 'info4yours'
tag = ''  # 등록할 태그값, 쉼표로 구분
output = 'json'  # 고정값
grant_type = 'authorization_code'  # 고정값
visibility = 0  # 0은 비공개, 3은 공개 발행
category = 1018259
x = dt.datetime.now()
today = str(x.year) + '-' + str(x.month) + '-' + str(x.day)


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
    title = 'YES24 종합 베스트 셀러 Top 10 (' + today + ')'
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
    # postWrite('불면증 완화 \n 일상생활, 과도한 업무와 학업으로 스트레스성 불면증을 시달리는 사람들이 많습니다. 대추는 긴장을 완화시켜주는 효과와 심신을 편안하게 해주는 효과가 있어서 섭취시에는 스트레스성 불면증을 완화하는데 큰 도움이 됩니다 \n 대추는 신경을 이완시키고 근육의 긴장을 풀어주는데도 많은 도움을 준다고 알려져 있는데요. 대추차를 섭취 시 안정됨으로써 숙면을 유도하고 불면증을 개선하는데도 뛰어난 효과가 있다고 합니다. \n 정신적으로는 스트레스나  긴장감을   완화시켜주는 대추즙 효능이 있는데  특히 따뜻한 대추차를 먹으면 긴장완화 큰 도움이 되며   이는 실제로 우리몸에  대추즙이 들어왔을때 몸을 이완시키는 효과가 있다고 합니다 \n 두번째 대추 효능은 불면증 및 신경 쇠약에 도움이 된다는 것입니다.갈락토오스, 맥아당, 자당이라는 당류성분이 많이 함유되어 있어서 신경을 안정시키는 데 도움을 줍니다.스트레스도 감소시키고 긴장감과 흥분을 가라앉혀 불면증 해소하고 우울증을 완화하는데도 좋습니다. \n 불면증 개선 \n 대추씨는 신경이 예민하거나 스트레스를 받을 경우 유용하게 사용된다고 합니다. 그리고 대추차로 끓여 먹으면 불면증을 개선하는 데에도 도움이 된다고 합니다. 따라서 무엇보다 대추에 있는 마그네슘 성분이 수면의 질을 향상해주는 데에 큰 도움이 된다고 하며 이 마그네슘 성분이 세로토닌을 많이 생성할 수 있게 도움을 줄 수 있다고 합니다. 때문에 대추가 내는 은은한 단맛으로 인해 불안감을 잠재우고 스트레스 해소를 도와주며 심리적 안정에 도움이 됩니다. 또 대추의 단맛은 우리에게 진정 작용을 해서 불안 및 우울이나 신경쇠약을 개선하고 히스테리를 가라앉히는 데 도움이 됩니다. 천연수면제라 불릴 만큼 불면증에 효과가 있다고 합니다. \n 불면증 개선도 대표적인 대추차 효능입니다. 대추는 우리의 신경과 근육을이완해주는 효과가 있어 심신을 안정시켜주고 스트레스 해소에 도움이 되어 불면증을 효과적으로 개선해줍니다. \n 불면증 \n  대추씨에는 신경을 이완시켜 잠을 잘 오게 하는 성분이 다량함유되어 있어 천연 수면제로 좋습니다.')

    url = 'http://www.yes24.com/24/Category/BestSeller?CategoryNumber=001&sumgb=06'
    res = requests.post(url)
    soup = BeautifulSoup(res.text, 'html5lib')

    # x = dt.datetime.now()
    # today = str(x.year) + '-' + str(x.month) + '-' + str(x.day)

    # blog_name = "info4yours"
    # title = "YES24 종합 베스트 셀러 Top 10 (" + today + ")"

    j = 1
    k = 2
    contentAll = ""
    for i in range(1, 11, 1):
        # 제목
        bookTitle_tag = '#category_layout > tbody > tr:nth-child(' + str(
            j) + ') > td.goodsTxtInfo > p:nth-child(1) > a:nth-child(1)'
        bookTitles = soup.select(bookTitle_tag)
        bookTitle = bookTitles[0].text
        # 저자/출판사/발행월
        auth_tag = '#category_layout > tbody > tr:nth-child(' + str(j) + ') > td.goodsTxtInfo > div'
        auths = soup.select(auth_tag)
        auth = auths[0].text.replace('\n', ' ').replace('\r', '').replace('\t', '').strip()
        # 가격/
        price_tag = '#category_layout > tbody > tr:nth-child(' + str(j) + ') > td.goodsTxtInfo > p:nth-child(3)'
        prices = soup.select(price_tag)
        price = prices[0].text.replace('\n', ' ').replace('\r', '').replace('\t', '').strip()
        # 요약
        summary_tag = '#category_layout > tbody > tr:nth-child(' + str(k) + ') > td:nth-child(2) > p.read'
        summarys = soup.select(summary_tag)
        summary = summarys[0].text.replace('\n', ' ').replace('\r', '').replace('\t', '').strip()
        # 이미지
        # category_layout > tbody > tr:nth-child(1) > td.image > div > a:nth-child(1) > img
        # category_layout > tbody > tr:nth-child(3) > td.image > div > a:nth-child(1) > img
        bookImg_tag = '#category_layout > tbody > tr:nth-child(' + str(j) + ') > td.image > div > a:nth-child(1) > img'
        bookImgs = soup.select(bookImg_tag)
        bookImg = bookImgs[0].text.replace('\n', ' ').replace('\r', '').replace('\t', '').strip()
        bookImg = (bookImgs[0].attrs['src'].split('/'))[4]

        content = '<h3 data-ke-size="size23"><b>' + str(i) + '. ' + bookTitle + '</b></h3>'
        content += '<ul style="list-style-type: disc;" data-ke-list-type="disc">'
        content += '<li>' + auth + '</li>'
        content += '<li>' + price + '</li>'
        content += '<li>' + summary + '</li>'
        content += '</ul>'
        content += '<figure data-ke-type="emoticon" data-ke-align="alignCenter" data-emoticon-isanimation="false"><img src="https://image.yes24.com/goods/' + \
                   bookImg + '/L"  width="300" alt="' + bookTitle + '"/></figure>'
        content += '<P>.</P>'
        contentAll += content
        j = j + 2
        k = k + 2

    postWrite(contentAll)