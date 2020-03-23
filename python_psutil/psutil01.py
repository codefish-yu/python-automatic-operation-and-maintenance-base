import psutil

#cpu数
print (psutil.cpu_count())

#查看虚拟内存
print(psutil.virtual_memory())
#查看虚拟内存利用率
print(psutil.virtual_memory().percent)
#查看虚拟内存总量:G为单位
print(float(psutil.virtual_memory().total/1024/1024/1024))
#查看磁盘
print(psutil.disk_partitions())
#显示cpu完整信息
print(psutil.cpu_times())