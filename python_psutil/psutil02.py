import psutil

#程序清单，是个列表
print(psutil.pids())
#查看程序总运行数
print(len(psutil.pids()))

#查看某个进程的信息
print(psutil.Process(2244))
#查看磁盘在哪个目录下
print(psutil.Process().exe())
#查看该进程连接的是哪一台远程服务器
print(psutil.Process(2244).connections())