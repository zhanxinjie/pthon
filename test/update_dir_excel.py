"""
使用win32api模块中的ShellExecute()函数来运行其他程序,格式如下
ShellExecute(hwnd, op, file, args, dir, show)
hwnd:父窗口的句柄，如果没有父窗口，则为0
op  :要运行的操作，为open,print或者为空
file:要运行的程序，或者打开的脚本
args:要向程序传递的参数，如果打开的是文件则为空
dir :程序初始化的目录
show:是否显示窗口
使用ShellExecute函数，就相当于在资源管理器中双击文件图标，系统会打开相应程序运行。
"""
"""
commands = {
'关机'：'shutdown -s -t 1',
'重启'：'shutdown -r',
'打开百度'：[r'C:\chrome.exe',"http://www.baidu.com"],
'关闭浏览器'：'taskkill /F/IM chrome.exe',
'打开QQ'：r'D:\QQ\Bin\QQ.exe',
'关闭QQ'：'taskkill /F/IM QQ.exe',
'歌曲'：[r'C:\wmplayer.exe',r'E:\m_one.mp3'],
'关闭音乐'：'taskkill /F/IM wmplayer.exe',
'打开迅雷'：[r'C:\ThunderStart.exe'],
'关闭迅雷'：'taskkill /F/IM Thunder.exe',
}


"""


"""
DataFrame.to_excel(excel_writer, sheet_name='Sheet1', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, startrow=0, startcol=0, engine=None, merge_cells=True, encoding=None, inf_rep='inf', verbose=True, freeze_panes=None)
该函数主要参数为:excel_writer。
excel_writer:写入的目标excel文件，可以是文件路径、ExcelWriter对象;
sheet_name:被写入的sheet名称，string类型，默认为'sheet1';
na_rep:缺失值表示，string类型;
header:是否写表头信息，布尔或list of string类型，默认为True;
index:是否写行号，布尔类型，默认为True;
encoding:指定写入编码，string类型。
"""

"""
pip install pypiwin32
pip install xlsxwriter
pip install pandas
pip install pyinstaller
pip install gitpython

pyinstaller.exe -F 文件路径/要打包的文件.py
"""
from time import sleep
import datetime
import os
# from os.path import join, getsize
import win32api
# import xlsxwriter
import pandas as pd
# import re
from git import Repo

allFileNum = 0

def git_pull(file_name):
    # 创建版本库对象
    repo = Repo(file_name)
    # 获取默认版本库
    remote = repo.remote()
    # git pull
    remote.pull()
    print('更新了本地git库')

def replace_data(file_name,file_new_name):
    pass


def pandas_replace_data1(file_name,file_new_name):
    df = pd.read_excel(file_name)  # 这个会直接默认读取到这个Excel的第一个表单
    df['所在目录/文件名'] = df['所在目录/文件名'].str.replace('C:', '')
    print('已去掉盘符')
    # df1 = df['所在目录/文件名'].str.contains('C:').fillna('') #测试是否包含‘C:’
    # df1 = df['所在目录/文件名'].str.split(r'C:').str[1] #分列
    # df.to_excel(file_name, index=False, encoding='utf-8')
    # writer = pd.ExcelWriter(file_name)
    writer = pd.ExcelWriter(file_new_name)
    df.to_excel(writer, index=False, encoding='utf-8')
    writer.save()
    print('已写入到excel文件中')

    # df = pd.read_excel(file_name, sheet_name='FileList')  # 可以通过sheet_name来指定读取的表单
    # df = pd.read_excel(file_name, sheet_name=['FileList', 'FileList2'])  # 可以通过表单名同时指定多个
    # df = pd.read_excel('lemon.xlsx',sheet_name=0)#可以通过表单索引来指定读取的表单
    # df = pd.read_excel('lemon.xlsx',sheet_name=['FileList',1])#可以混合的方式来指定
    # df = pd.read_excel('lemon.xlsx',sheet_name=[1,2])#可以通过索引 同时指定多个
    # data=df.head()#默认读取前5行的数据
    data = df.values  # 获取所有的数据
    # data = df.loc[[1,2,3]].values  # loc/iloc读取指定多行的话，就要在loc[]里面嵌套列表指定行数
    # data = df.iloc[1, 2]  # 读取第一行第二列的值，这里不需要嵌套列表
    # data = df.loc[:, ['所在目录/文件名', '大小']].values  # loc/iloc读所有行的title以及data列的值，这里需要嵌套列表
    # data = df.loc[[1, 2], ['所在目录/文件名', '大小']].values  # loc/iloc读取第一行第二行的title以及data列的值，这里需要嵌套列表
    # print("输出行号列表", df.index.values)
    # print("输出列标题", df.columns.values)
    # print("输出值\n", df['所在目录/文件名'].values)
    # print("输出值", df.sample(3).values)  # 这个方法类似于head()方法以及df.values方法
    print(print("获取到所有的值:\n{0}".format(data)))  # 格式化输出

def file_all_name(file_dir):
    '''
    :param file_dir:
    :return:
    '''
    for root, dirs, files in os.walk(file_dir):
        print("root",root)  # root是指当前目录路径(文件夹的绝对路径)
        print("dirs",dirs)  # dirs是指路径下所有的子目录(文件夹里的文件夹)
        print("files",files)  # files是指路径下所有的文件(文件夹里所有的文件)
    # for files in os.listdir(file_dir):  # 不仅仅是文件，当前目录下的文件夹也会被认为遍历到
    #     print("files", files)

def get_FileSize(filePath):
    fsize = os.path.getsize(filePath)
    # fsize = fsize/float(1024*1024)#单位：MB
    fsize = fsize/float(1024)#单位：KB
    return round(fsize,1)

def printPath(level, path):
    global allFileNum
    ''''' 
    打印一个目录下的所有文件夹和文件 
    '''
    # 所有文件夹，第一个字段是次目录的级别
    dirList = []
    # 所有文件
    fileList = []
    # 返回一个列表，其中包含在目录条目的名称(google翻译)
    files = os.listdir(path)
    # print(files)
    # 先添加目录级别
    dirList.append(str(level))
    for f in files:
        if(os.path.isdir(path + '/' + f)):
            # 排除隐藏文件夹。因为隐藏文件夹过多
            if(f[0] == '.'):
                pass
            else:
                # 添加非隐藏文件夹
                dirList.append(f)
        if(os.path.isfile(path + '/' + f)):
            # 添加文件
            fileList.append(f)
    # 当一个标志使用，文件夹列表第一个级别不打印
    i_dl = 0
    for dl in dirList:
        if(i_dl == 0):
            i_dl = i_dl + 1
        else:
            # 打印至控制台，不是第一个的目录
            print('-' * (int(dirList[0])), dl)

            # 打印目录下的所有文件夹和文件，目录级别+1
            printPath((int(dirList[0]) + 1), path + '/' + dl)
    for fl in fileList:
        # 打印文件
        FileSize = get_FileSize(os.path.join(path,fl))
        FileSize = get_FileSize(os.path.join(path,fl))
        print('-' * (int(dirList[0])), fl)
        print(FileSize,'KB')
        # 随便计算一下有多少个文件
        allFileNum = allFileNum + 1

def main(dir_path,software_path,file_name):
    '''
    :param dir_path:目标目录的路径
    :param software_path:ListFile这个软件的路径
    :param file_name: 生成的文件名
    :param file_new_name: 新的文件名
    :return:
    '''
    #dir_path下所有的文件
    content = os.listdir(dir_path)
    print(content)

    while True:
        git_pull(dir_path)
        new_content = os.listdir(dir_path)
        if new_content !=content:
            #打开ListFile这个软件
            win32api.ShellExecute(0,'open',software_path,'',dir_path,0)
            sleep(10)
            #关闭自动打开的wps文件
            try:
                os.system("taskkill /F /IM wps.exe")
                print("已关闭WPS程序！")
                sleep(10)
                # os.system("taskkill /F /EXCEL.exe")
                # print("已关闭EXCEL程序！")
            except:
                continue
            # replace_data(file_name,file_new_name)
            # 删除原有的文件
            if os.path.exists(file_new_name):
                os.remove(file_new_name)
                os.rename(file_name, file_new_name)
                print('已移除文件，且成功修改文件名!!!')
            else:
                os.rename(file_name, file_new_name) // 修改文件名
                print('已成功修改文件名!!!')
            break;
        else:
            print("该目录没有变动！")
        sleep(3)


if __name__ == '__main__':
    file_dir = r"E:\mep-doc"
    #目标目录的路径
    dir_path = r"E:\mep-doc"
    # dir_path = r"C:\Users\Administrator\Desktop\1232"
    #ListFile这个软件的路径
    software_path = os.path.join(dir_path, r"ListFile.exe")
    #生成的文件名
    file_name = os.path.join(dir_path, r"FileList.xlsx")
    #新的文件名
    file_new_name = os.path.join(dir_path, r"20.文件一览表.xlsx")
    #运行主程序
    main(dir_path,software_path,file_name)
    # file_all_name(file_dir)
    # replace_data(file_name,file_new_name)

    printPath(1, file_dir)
    print('总文件数 =', allFileNum)


