'''
Author: ccbao 1689940525@qq.com
Date: 2023-05-24 00:59:56
LastEditors: ccbao 1689940525@qq.com
LastEditTime: 2023-05-24 01:18:39
FilePath: /crawler/multi_thread_craw.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import threading
import blog_spider
import time
def single_thread():   
    print("single thread started")
    for url in blog_spider.urls:
        blog_spider.crawler(url)
    print("single thread end")

def multi_thread():
    print("multi thread started")
    threads = []
    for url in blog_spider.urls:
        threads.append(
            threading.Thread(target=blog_spider.crawler,args=(url,)) # due to the tuple type of args, so you need add ,
        )
        
    for thread in threads:
        thread.start()
        
    for thread in threads:
        thread.join()
        
    print("multi thread end")



if __name__ == "__main__":
   start = time.time()
   single_thread()
   end = time.time()
   print(f"single thread cost: { end - start } seconds")
   
   
   
   start = time.time()
   multi_thread()
   end = time.time()
   print(f"multi thread cost: { end - start } seconds")
   
   