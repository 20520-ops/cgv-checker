import os
import requests
from bs4 import BeautifulSoup

THEATER_CODE = "0013"  # 용산아이파크몰
TARGET_DATE = "20260902"
MOVIE_TITLE = "오디세이"

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def send_telegram(text):
    if BOT_TOKEN and CHAT_ID:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.get(url, params={"chat_id": CHAT_ID, "text": text})

def check_open():
    url = f"http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode={THEATER_CODE}&date={TARGET_DATE}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    try:
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        for imax in soup.select("span.imax"):
            container = imax.find_parent("div", class_="col-times")
            if container and container.find("a") and MOVIE_TITLE in container.find("a").text.strip():
                return True
    except Exception as e:
        print(f"오류 발생: {e}")
    return False

if __name__ == "__main__":
    if check_open():
        send_telegram(f"🚨 [CGV 용산] 9/2일자 '{MOVIE_TITLE}' IMAX 예매가 오픈되었습니다!")
