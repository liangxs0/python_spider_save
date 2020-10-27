import requests
from pyquery import PyQuery
import logging
import re
from urllib.parse import urljoin #拼接url地址
import time
import pymongo

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s:%(message)s"
)

#构建一个头信息，以免被浏览器认为是一个机器人
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"
}
proxies = {

}

start_url = "http://www.zongheng.com/rank/details.html?rt=1&d=1&i=2&p={}"

total_page = 2

#获取页面的html文本
def scrape_page(url):
    logging.info("scraping %s..",url)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code is requests.codes.ok:
            return response.text
        logging.error("get %s is not 200", url)
        return None
    except requests.RequestException as e:
        logging.error("scraping error %s", e)
        return None

#构造url,返回url的页面文本
def scrape_index(page):
    index_url = start_url.format(page)
    return scrape_page(index_url)#返回当前url的页面文本

#解析获取每个书籍详情的url
#html指一级页面文本
def parse_index(html):
    doc = PyQuery(html)#构造pyquery对象
    #divs 根据标签获取class = rankpage_box的代码块返回子节点
    divs = doc(".rankpage_box").children(".rank_d_list")
    #循环拿出每个子节点的内容
    for div in divs.items():
        #根据class属性定位到a标签
        a = div(".rank_d_book_img a")
        #获取a标签中的href的属性值
        href = a.attr("href")
        yield href#返回herf

#获取详情页面的文本信息
def scrape_detail(url):
    return scrape_page(url)

#解析页面信息
def parse_detail(html):
    logging.info("detail get...")
    doc = PyQuery(html)
    # book_detail = doc(".book-top").children(".book-main")#定位块儿
    book_side = doc(".book-top").children(".book-side")
    # book_info = book_detail(".book-detail")
    book_info = doc(".book-top .book-main .book-detail .book-info")
    book_name = book_info.children(".book-name").text()
    type = book_info.children(".book-label .label").text()
    status = book_info.children(".book-label .state").text()
    numbers = book_info.children(".nums")
    clicknumbers = [num("i").text()  for num in numbers.items()][0].split(" ")[2]
    intro = book_info.children(".book-dec").text()
    img_url = book_info.siblings(".book-img img").attr("src")
    author = book_side.children(".book-author .au-name a").text()
    return {
        "bookname":book_name,
        "author":author,
        "type":type,
        "status":status,
        "intro":intro,
        "clicknumbers":clicknumbers,
        "imageurl":img_url,
    }

def save(data):
    #根据bookname在数据库进行查询，如果说bookname已经存在
    #就更新这个bookname中的数据，否则就插入一条新的数据
    #这是update_one中 upsert=True的作用
    collection.update_one({
        "bookname":data.get("bookname")
    },{"$set":data}, upsert=True)

def image_save(data):
    url = data["imageurl"]
    image_name = data["bookname"]
    image = requests.get(url, headers=headers)
    if image.status_code is not requests.codes.ok:
        return None
    with open(f"image/{image_name}.jpeg", "wb") as f:
        f.write(image.content)

if __name__ == '__main__':
    #数据库链接
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client.books
    collection = db["info"]

    for i in range(1, total_page):
        html = scrape_index(i)
        if html is None:
            logging.info(f"{i} page is error")
            continue
        urls = parse_index(html)

        for url in urls:
            detail_html = scrape_detail(url)
            if detail_html is None:
                logging.info("url requests is error")
                continue
            detail_info = parse_detail(detail_html)
            save(detail_info)
            image_save(detail_info)
            time.sleep(5)


