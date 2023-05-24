import time  ##调用time内置模块


def stor(file, cont):  # 日志记录，需要各个记录日志信息两个选项中的第一个传递传文件名参数，第二个就是其他记录变量信息传递给cont的参数。

    ##ymdHMS写出你想要的时间格式，time.time返回当前时间的时间戳，time.localtime格式化时间戳为本地的时间.
    strtim = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    ##time.strftime函数用于格式化时间，返回以可读字符串表示的当地时间
    with open(file, 'a+', encoding='utf8') as fp:  ##打开file文件参数，追加读写，设置utf8编码集，命名fp。
        fp.write(strtim + '  ' + cont + "\n")  ##fp追写、然后就是日志格式了；时间在前+拼接中间空格隔开+记录字段阶段给个换行。
