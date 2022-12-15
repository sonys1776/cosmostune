import aiohttp
import asyncio
from bs4 import BeautifulSoup
import openpyxl
import datetime
import os

posts = []
last_link = ""


async def get_post_description(url: str):
    try:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(), headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36', }, trust_env=True) as session:
            async with session.get(url) as response:
                soup = BeautifulSoup(await response.text(), "html.parser")
                description_soup = soup.select_one("div.entry-content") or soup.select_one(
                    "div.contents_style") or soup.select_one("div.article_view") or soup.select_one("article")
                text = description_soup.text
                while("\n\n\n" in text):
                    text = text.replace("\n\n\n", "\n\n")

                idx = text.find("공유하기")
                if idx != -1:
                    text = text[:idx]
                return text.replace("반응형", "")
    except:
        print("Error : 게시글 수집 실패 - ", url)
        return ""


async def main():
    global last_link
    print("=========================================")
    query = input("검색어를 입력하세요 (ex: 사과 효능): ").replace(" ", "%20")
    start = input("시작일을 입력하세요. (ex: 20011231): ")
    end = input("종료일을 입력하세요. (ex: 20220524): ")
    print("수집할 페이지 수를 입력하세요.")
    print("(ex : 5 입력 시 1~5페이지까지 수집)")
    print("(전체 게시물을 수집하려면 0을 입력하세요)")
    page = -1
    while(page == -1):
        try:
            page = int(input())
        except:
            print("ERROR : 정수로 입력해주세요.")

    if page == 0:
        i = 1
        while True:
            url = f"https://search.daum.net/search?w=blog&enc=utf8&q={query}&f=section&SA=tistory&p={i}&DA=STC&period=u&sd={start}235959&ed={end}000000"

            async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(), headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36', }, trust_env=True) as session:
                async with session.get(url) as response:
                    soup = BeautifulSoup(await response.text(), "html.parser")
                    blogs_soup = soup.select("ul.list_info > li")

                    for blog_soup in blogs_soup:
                        link = blog_soup.select_one("a.f_link_b").get("href")

                        print(f"{i}페이지 수집 중... {link}\t\t\t\t\t\t", end="\n")

                        posts.append({
                            "link": link,
                            "title": blog_soup.select_one("a.f_link_b").text,
                            "date": blog_soup.select_one("span.f_nb.date").text,
                            "description": await get_post_description(link),
                        })

                    if not posts or last_link == posts[-1]["link"]:
                        break

                    last_link = posts[-1]["link"]
            i += 1
    else:
        for i in range(1, page + 1):
            url = f"https://search.daum.net/search?w=blog&enc=utf8&q={query}&f=section&SA=tistory&p={i}&DA=STC&period=u&sd={start}235959&ed={end}000000"

            async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(), headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36', }, trust_env=True) as session:
                async with session.get(url) as response:
                    soup = BeautifulSoup(await response.text(), "html.parser")
                    blogs_soup = soup.select("ul.list_info > li")

                    for blog_soup in blogs_soup:
                        link = blog_soup.select_one("a.f_link_b").get("href")
                        print(f"\r{i}페이지 수집 중... {link}")

                        posts.append({
                            "link": link,
                            "title": blog_soup.select_one("a.f_link_b").text,
                            "date": blog_soup.select_one("span.f_nb.date").text,
                            "description": await get_post_description(link),
                        })

    if not os.path.exists("./포스트"):
        os.makedirs("./포스트")

    query = query.replace("%20", " ")

    print("=========================================")
    print("총 : ", len(posts), "개의 게시물를 수집하였습니다.")
    print("엑셀 파일 생성 중...")
    write_wb = openpyxl.Workbook()
    print("엑셀 시트 생성 중...")
    write_ws = write_wb.active
    print("엑셀 시트에 데이터 입력 중...")
    write_ws.append(["번호", "제목", "날짜", "링크", "본문"])

    total = ""
    for i in range(len(posts)):
        try:
            write_ws.append([i + 1, posts[i]['title'], posts[i]
                            ["date"], posts[i]['link'], posts[i]['description']])
            open(f"./포스트/{query}{i + 1}blog.txt", "w",
                 encoding="utf-8").write(posts[i]['description'])
            total += posts[i]['description'] + "\n\n"
        except Exception as E:
            print("ERROR : ", posts[i]['link'])
            print(E)

    with open(f"./{query}blog.txt", "w", encoding="utf-8") as f:
        f.write(total)

    write_wb.save(
        f"./포스트/{query} {datetime.datetime.now().strftime('%Y-%m-%d')}blog.xlsx")
    print("엑셀 파일 생성 완료")
    print("제작자 [Github : junah201]")
    print("=========================================")
    input()

if __name__ == "__main__":
    asyncio.run(main())
