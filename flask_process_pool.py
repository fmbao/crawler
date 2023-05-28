'''
Author: ccbao 1689940525@qq.com
Date: 2023-05-28 13:15:40
LastEditors: ccbao 1689940525@qq.com
LastEditTime: 2023-05-28 13:26:27
FilePath: /crawler/flask_process_pool.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import flask 
from concurrent.futures import ProcessPoolExecutor
import math
import json
app = flask.Flask(__name__)



def is_prime(n):
    if n <2:
        return False
    if n == 2:
        return True
    if n % 2 ==0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3,sqrt_n+1,2):
        if n % i == 0:
            return False
    return True


@app.route('/is_prime/<numbers>')
def api_is_prime(numbers):
    numbers_list = [int(x) for x in numbers.split(',')]
    results = process_pool.map(is_prime,numbers_list)
    return json.dumps(dict(zip(numbers_list,results)))

# app.run()    


# process_pool = ProcessPoolExecutor()

if __name__ == "__main__":
    process_pool = ProcessPoolExecutor()
    app.run()