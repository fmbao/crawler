'''
Author: ccbao 1689940525@qq.com
Date: 2023-05-28 20:50:36
LastEditors: ccbao 1689940525@qq.com
LastEditTime: 2023-05-28 20:57:52
FilePath: /crawler/async_spider.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import asyncio
import aiohttp
import blog_spider

async def async_craw(url):
    print("craw url: " ,url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            result = await resp.text()
            print(f"craw url: {url}, {len(result)}")
            
loop = asyncio.get_event_loop()

tasks = [
    loop.create_task(async_craw(url))
    for url in blog_spider.urls
]

import time
start = time.time()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()

print("use time seconds: ",end - start) 