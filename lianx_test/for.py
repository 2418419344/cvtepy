def ws():
    import os
    from os import startfile
    # 文件夹目录
    path=("C:\\Users\\user\\PycharmProjects\\pythonProject1\\venv")

    # 获取文件夹中所有的文件(名)，以列表形式返货
    lists=os.listdir(path)
    print(f"未经处理的文件夹列表:{lists}" )

    # 按照key的关键字进行生序排列，lambda入参x作为lists列表的元素，获取文件最后的修改日期，
    # 最后对lists以文件时间从小到大排序
    lists.sort(key=lambda x:os.path.getmtime((path+"\\"+x)))
    # 获取最新文件的绝对路径，列表中最后一个值,文件夹+文件名
    file_new = os.path.join(path, lists[-1])
    print(f"时间排序后的的文件夹列表：{lists}")
    print("\n%s" % file_new)
    print(file_new)
    os.startfile(fr'{file_new}')#根据获取最新路径进行打开
