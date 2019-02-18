import requests
from bs4 import BeautifulSoup
import json
import winsound
import time

URL = 'https://www.surveyrewardz.com/offers/end_new'

def getHeader():
    headers = {'authority': 'www.surveyrewardz.com', 
                'method':   'GET',
                'path':     '/offers/end_new',
                'scheme':   'https',
                'accept':   'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,imag',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }

    return headers

def getCookies():
    cookies = {}
    f = open('cookies.json', 'r')
    content = json.loads(f.read())
    for d in content:
        cookies[d['name']] = d['value']
    
    return cookies

def main():
    while(True):
        headers = getHeader()
        cookies = getCookies()
        r = requests.get(URL, headers=headers, cookies=cookies)
        status = r.status_code
        soup = BeautifulSoup(r.text, 'html.parser')
        message = soup.find("h3", "text-center router-message").text.replace('\\n', '').strip()

        if status == 200:
            if 'Sorry' in message:
                #print("MESSAGE: " + message)
                time.sleep(15)
            else:
                title = soup.find("p", "router-content-title").text.replace('\n', '').strip()
                value = soup.find("strong").text.replace('\\n', '').strip()
                print("MESSAGE: " + message)
                print("SURVEY NAME: " + title)
                print("VALUE: " + value)
                winsound.PlaySound('untitled.wav', winsound.SND_FILENAME)
                time.sleep(60)


if __name__ == "__main__":
    main()