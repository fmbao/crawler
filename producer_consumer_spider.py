'''
Author: ccbao 1689940525@qq.com
Date: 2023-05-24 11:52:56
LastEditors: ccbao 1689940525@qq.com
LastEditTime: 2023-05-24 13:42:26
FilePath: /crawler/producer_consumer_spider.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import time
import random
import threading
import queue
import blog_spider



def do_crawl(url_queue: queue.Queue, html_queue: queue.Queue):
    while True:
        url = url_queue.get()
        html = blog_spider.crawler(url)
        html_queue.put(html)
        print(threading.currentThread().name,f"craw {url}", "url_queue.size = ",url_queue.qsize())
        time.sleep(random.randint(1,2))
        
        
def do_parse(html_queue: queue.Queue,fout):
    while True:
        html = html_queue.get()
        results = blog_spider.parse(html)
        for rsult in results:
            fout.write(str(rsult) + '\n')
        print(threading.currentThread().name,"results.size", len(results) ,"html_queue.size = ",html_queue.qsize())
        time.sleep(random.randint(1,2))
            
            
if __name__ == "__main__":
    url_queue = queue.Queue()
    html_queue = queue.Queue()
    
    for url in blog_spider.urls:
        url_queue.put(url)
        
    for idx in range(3):
        t = threading.Thread(target=do_crawl,args=(url_queue,html_queue))
        t.start()
        
    fout = open("result.txt",'w')
    for idx in range(2):
        t = threading.Thread(args=do_parse,args=(html_queue,fout))
        t.start()
        
        