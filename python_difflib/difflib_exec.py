'''
ｐython自动化运维：ｄifflib模块
实战：比对文件内容差异
'''
import sys
import difflib

#将需要比对的两个原始文件作为环境配置参数引入
try:
    textfile1 = 'nginx.conf'
    textfile2 = 'nginx1.conf'
except:
    print('text argv')
    sys.exit()

#读取文件内容的函数
def readfile(file_path):
    f = open(file_path,'r')
    text = f.readlines()
    f.close()
    return text

#读取文件内容
text_file1 = readfile(textfile1)
text_file2 = readfile(textfile2)

#比对
d = difflib.Differ()
diff = '\n'.join(list(d.compare(text_file1,text_file2)))
print(diff)



