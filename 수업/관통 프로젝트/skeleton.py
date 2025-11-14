import requests
from bs4 import BeautifulSoup
from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

TOPIC = "stock-ticks"

def get_stock_price(code):
    url = f"https://finance.naver.com/item/sise.naver?code={code}"
    headers = {"User-Agent": "Mozilla/5.0"}

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    # 현재가
    price = soup.select_one(".no_today .blind").text.strip()

    # 전일 대비
    diff = soup.select_one(".no_exday .blind").text.strip()

    # 등락률
    rate = soup.select(".no_exday .blind")[1].text.strip()

    return {
        "symbol": code,
        "price": price.replace(",", ""),
        "diff": diff.replace(",", ""),
        "rate": rate,
        "timestamp": time.time(),
    }

while True:
    data = get_stock_price("005930")
    producer.send(TOPIC, data)
    print("Send Kafka:", data)

    time.sleep(1)   # 1초 간격으로 실시간처럼 수집
