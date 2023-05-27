'''
Author: ccbao 1689940525@qq.com
Date: 2023-05-26 23:03:19
LastEditors: ccbao 1689940525@qq.com
LastEditTime: 2023-05-27 09:33:49
FilePath: /crawler/thread_pool.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import concurrent.futures
import blog_spider

# craw 
with concurrent.futures.ThreadPoolExecutor() as pool:
    htmls = pool.map(blog_spider.crawler, blog_spider.urls)
    htmls = list(zip(blog_spider.urls, htmls))
    for url,html in htmls:
        print(url, len(html))
        

print("craw over")

# parse 
with concurrent.futures.ThreadPoolExecutor() as pool:
    futures = {}
    for url,html in htmls:
        future = pool.submit(blog_spider.parse, html)
        futures[future] = url
        
        