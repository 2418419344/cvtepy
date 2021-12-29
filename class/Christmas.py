import time
import tkinter
import os
import random
class ED_s():
    def  __init__(self):
        pass
    def fenbian(self):
        screen = tkinter.Tk()
        x = screen.winfo_screenwidth()
        return x
        #获取当前屏幕的宽
    def dfgdf(self):
        screen = tkinter.Tk()
        y = screen.winfo_screenheight()
        return y
        #获取当前屏幕的高
print("当前屏幕的宽为:{0}".format(ED_s.fenbian()))
print("当前屏幕的高为:{0}".format(ED_s.dfgdf()))
if ED_s.fenbian() == 1280 and ED_s.dfgdf() == 720:  
    print("正确")
    f = open('正确结果.txt', 'a+')  # 记录结果
    print('正确', file=f)
    time.sleep(2)
    #_______________#
    time1 = 1
    os.system(f'shutdown -s -t {time1}')

else:
    print('错误')
    f = open('正确结果.txt', 'a+')  # 记录结果
    print('错误', file=f)
    from PIL import ImageGrab
    avg = random.randint(1, 99)
    rec = random.randint(99, 500)
    print(avg)
    print(rec)
    im = ImageGrab.grab()
    im.save('{0}path{1}'.format(avg,rec), 'png')  # 用随机数给他命名截图
    im.save('path-to-save', 'png')  # 能替代文件，头大不弄乐
    f.close()
