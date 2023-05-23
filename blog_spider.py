'''
Author: ccbao 1689940525@qq.com
Date: 2023-05-24 00:59:39
LastEditors: ccbao 1689940525@qq.com
LastEditTime: 2023-05-24 01:19:02
FilePath: /crawler/blog_spider.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import requests
urls = [f"https://www.cnblogs.com/#p{page}" for page in range(50)]

def crawler(url):
    r = requests.get(url)
    # print(r.text)


crawler(urls[1])