import requests
import time
start_url = "http://books.toscrape.com/catalogue/page-{}.html"

def scrape_page(url):
    try:
        response = requests.get(url)
        if requests.codes.ok is response.status_code:
            return response.url
        else:
            return None
    except Exception as e:
        print(e)
        return None

def scarpe_index(page):
    return start_url.format(page)

if __name__ == '__main__':
    start_time = time.time()
    for i in range(1,11):
        url = scarpe_index(i)
        info = scrape_page(url)
        print(info)
    end_time = time.time()
    print(start_time,end_time)
    print("times:",(start_time-end_time))