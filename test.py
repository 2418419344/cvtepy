'''
import random
import time

while True:
    pleary = int(input('请输入一个数字 1-石头， 2-剪刀， 3-布：'))
    commpuert =random.randint(1, 3)

    if pleary == 88:
        time.sleep(1)
        print('加载中.')
        time.sleep(1)
        print('加载中..')
        time.sleep(1)
        print('加载中...')
        time.sleep(3)
        print('靓仔再见！')
        break
    elif pleary > 3 or pleary < 1:
        print('请输入1-3')
    elif commpuert == 1 and pleary == 3 or commpuert == 2 and pleary == 1 or commpuert == 3 and pleary == 2:
        time.sleep(1)
        print('加载中.')
        time.sleep(1)
        print('加载中..')
        time.sleep(1)
        print('加载中...')
        time.sleep(3)
        print('玩家出拳：', pleary, '电脑出拳：', commpuert, '卧槽你赢了！')
    elif pleary == commpuert:
        time.sleep(1)
        print('加载中.')
        time.sleep(1)
        print('加载中..')
        time.sleep(1)
        print('加载中...')
        time.sleep(3)
        print('玩家出拳：', pleary, '电脑出拳：', commpuert, '平局，再来')
    else:
        time.sleep(1)
        print('加载中.')
        time.sleep(1)
        print('加载中..')
        time.sleep(1)
        print('加载中...')
        time.sleep(3)
        print('玩家出拳：', pleary, '电脑出拳：', commpuert, '你输了')
'''