'''
Author: ccbao 1689940525@qq.com
Date: 2023-05-24 00:59:39
LastEditors: ccbao 1689940525@qq.com
LastEditTime: 2023-05-28 20:58:27
FilePath: /crawler/blog_spider.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import requests
from bs4 import BeautifulSoup
urls = [f"https://www.cnblogs.com/#p{page}" for page in range(50)]

def crawler(url):
    r = requests.get(url)
    return r.text
    # print(r.text)


def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a',class_='post-item-title')
    return [(link['href'], link.get_text()) for link in links]
    
    
if __name__ == '__main__':
    for result in parse(crawler(urls[1])):
        print(result)
    


# crawler(urls[1])