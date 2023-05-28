'''
Author: ccbao 1689940525@qq.com
Date: 2023-05-27 13:31:14
LastEditors: ccbao 1689940525@qq.com
LastEditTime: 2023-05-27 13:44:37
FilePath: /crawler/thread_process_cpu_bound.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

PRIMES = [1155555552223443340] * 10000

def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 ==0:
        return False
    sqrt_n = int(math.floor(math.sqrt(x)))
    for i in range(3,sqrt_n+1,2):
        if x % i==0:
            return False
    return True

def single_thread():
    for num in PRIMES:
        is_prime(num)
        
        
def multi_thread():
    with ThreadPoolExecutor() as pool:
        pool.map(is_prime,PRIMES)
        
def multi_process():
    with ProcessPoolExecutor() as pool:
        pool.map(is_prime,PRIMES)
        
if __name__ == "__main__":
    start = time.time()
    single_thread()
    end = time.time()
    print("single_thread, cost: ", end - start," s")
    
    start = time.time()
    multi_thread()
    end = time.time()
    print("multi_thread, cost: ", end - start," s")
    
    
    start = time.time()
    multi_process()
    end = time.time()
    print("multi process, cost: ", end - start," s")