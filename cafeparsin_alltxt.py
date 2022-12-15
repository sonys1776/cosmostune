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
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(), headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36', },
                                         trust_env=True) as session:
            async with session.get(url) as response:
                soup = BeautifulSoup(await response.text(), "html.parser")
                description_soup = soup.select_one("#article")
                text = description_soup.text

                while ("\n \n" in text):
                    text = text.replace("\n \n", "\n\n")

                while ("\n\n\n" in text):
                    text = text.replace("\n\n\n", "\n")

                idx = text.find("공유하기")
                if idx != -1:
                    text = text[:idx]
                return text.replace("반응형", "")
    except Exception as E:
        print("Error : 게시글 수집 실패 - ", url)
        print(E)
        return ""


async def main():
    global last_link
    print("=========================================")
    query = input("검색어를 입력하세요 (ex: 사과 효능): ").replace(" ", "%20")
    page = int(input("몇 페이지까지 수집할까요? (ex: 1): "))

    i = 1
    while i <= page:
        url = f"https://m.cafe.daum.net/_search/article?query={query}&sort=accuracy&page={i}"

        print(url)

        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(), headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36', },
                                         trust_env=True) as session:
            async with session.get(url) as response:
                soup = BeautifulSoup(await response.text(), "html.parser")
                blogs_soup = soup.select(
                    "#slideArticleList > li")

                for blog_soup in blogs_soup:
                    link = f"https://m.cafe.daum.net{blog_soup.select_one('a.link_cafe').get('href')}"

                    print(f"{i}페이지 수집 중... {link}\t\t\t\t\t\t", end="\n")

                    posts.append({
                        "link": link,
                        "title": blog_soup.select_one("strong.tit_info").text,
                        "date": blog_soup.select_one("span.created_at").text,
                        "description": await get_post_description(link),
                    })

                if not posts or last_link == posts[-1]["link"]:
                    break

                last_link = posts[-1]["link"]
        i += 1

    if not os.path.exists("./포스트"):
        os.makedirs("./포스트")

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
            open(f"./포스트/{query}{i + 1}cafe.txt", "w",
                 encoding="utf-8").write(posts[i]['description'])
            total += posts[i]['description'] + "\n\n"
        except Exception as E:
            print("ERROR : ", posts[i]['link'])
            print(E)

    with open(f"./{query}cafe.txt", "w", encoding="utf-8") as f:
        f.write(total)

    write_wb.save(
        f"{query} {datetime.datetime.now().strftime('%Y-%m-%d')}cafe.xlsx")
    print("엑셀 파일 생성 완료")
    print("제작자 [Github : junah201]")
    print("=========================================")
    input()


if __name__ == "__main__":
    asyncio.run(main())