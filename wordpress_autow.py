#from wordpress_xmlrpc import Client, WordPressPost
#from wordpress_xmlrpc.methods.posts import NewPost
from wordpress_xmlrpc import Client
from wordpress_xmlrpc import WordPressPost
from wordpress_xmlrpc.methods import posts

from base64 import encode
import requests
from bs4 import BeautifulSoup
import datetime as dt

if __name__ == "__main__":
    url = 'http://www.yes24.com/24/Category/BestSeller?CategoryNumber=001&sumgb=06'
    res = requests.post(url)
    soup = BeautifulSoup(res.text, 'html5lib')

    #x = dt.datetime.now()
    #today = str(x.year) + '-' + str(x.month) + '-' + str(x.day)

    #blog_name = "nocrazy"
    #title = "YES24 종합 베스트 셀러 Top 10 (" + today + ")"

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
        content += '<P></P>'
        contentAll += content
        j = j + 2
        k = k + 2

x = dt.datetime.now()
today = str(x.year) + '-' + str(x.month) + '-' + str(x.day)

# Wordpress posting
client = Client("https://nagunaeinfo.kr/xmlrpc.php", "a3joy2u", "Bsj44Nwrpu*QB*q")
postx = WordPressPost()
postx.title = 'YES24 종합 베스트 셀러 Top 10 [' + today + ']'# 제목
postx.slug = 'wordpress-auto-posting'   # https://xxx.com/wordpress-auto-posting // 주소
postx.content = contentAll # 본문
postx.terms_names = {
    'post_tag': 'wordpress auto posting with python',   # tag (쉼표로 구분)
    'category' : ['이슈정보']  # category
}
postx.post_status = 'draft'   # publish: 바로 발행 // draft: 임시저장
client.call( posts.NewPost(postx) )