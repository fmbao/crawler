'''
Author: ccbao 1689940525@qq.com
Date: 2023-05-24 17:53:03
LastEditors: ccbao 1689940525@qq.com
LastEditTime: 2023-05-24 18:08:09
FilePath: /crawler/lock_concurrent.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import threading

lock = threading.Lock()

class Account:
    def __init__(self,balance):
        self.balance = balance
        
def draw(account, amount):
    with lock:
        if account.balance >= amount:
            print(threading.current_thread().name,"取钱成功")
            account.balance -= amount
            print(threading.current_thread().name,"余额 ", account.balance)
            
        else:
            print(threading.current_thread().name,"取钱失败， 余额不足")
        
        
        
if __name__ == "__main__":
    account = Account(1000)
    ta = threading.Thread(name='ta',target=draw,args=(account,800))
    tb = threading.Thread(name='tb',target=draw,args=(account,800))
    ta.start()
    tb.start()
    
    