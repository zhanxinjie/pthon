'''
Python提取Word中的图片
1.思路
在网上查找了半天，基本都是提取word中文字的，没有找到可以把word中的图片提取出来的方法。一个巧合的情况下，发现将word的后缀名改为zip，然后解压该zip，可以看到原来word是这样存储的：
图片就存放在固定的文件夹下：/word/media/；
那么我们就只需要批量的修改文件后缀名，并且解压之后将图片拷贝到需要存放的地方，然后将该文件夹清空留作下次的路径，并且将文件从zip改回docx即可。（注意：doc不支持这个方法，如果需要提取doc格式的图片，可以先转为docx,再提取即可）
'''
import zipfile
import os
import shutil

def word2pic(path,zip_path,tmp_path,store_path):
    '''
    :param path:源文件
    :param zip_path:docx重命名为zip
    :param tmp_path:中转图片文件夹
    :param store_path:最后保存结果的文件夹（需要手动创建）
    :return:
    '''
    #将docx文件重命名为zip文件
    os.rename(path,zip_path)
    #进行解压
    f = zipfile.ZipFile(zip_path, "r")
    #将图片提取并保存
    for file in f.namelist():
        f.extract(file,tmp_path)
    #释放该zip文件
    f.close()

    #将docx文件从zip还原为docx
    os.rename(zip_path,path)
    #得到缓存文件夹中图片列表
    pic = os.listdir(os.path.join(tmp_path,'word/media'))

    #将图片复制到最终的文件夹中
    for i in pic:
        #根据word的路径生成图片的名称
        new_name = path.replace('\\' , '_')
        new_name = new_name.replace(':' , '') + '_' + i
        shutil.copy(os.path.join(tmp_path + '/word/media',i),os.path.join(store_path,new_name))

    #删除缓冲文件夹中的文件，用以储存下一次的文件
    for i in os.listdir(tmp_path):
        #如果是文件夹则删除
        # print(os.listdir(tmp_path))
        if os.path.isdir(os.path.join(tmp_path, i)):
            shutil.rmtree(os.path.join(tmp_path, i))

if __name__ == "__main__":
    # #源文件
    path = r'.\临床技能中心管理平台V2.0.0技术白皮书-20180706.docx'
    #docx重命名为zip
    zip_path =r'.\临床技能中心管理平台V2.0.0技术白皮书-20180706.zip'
    #中转图片文件夹
    tmp_path =r'.\tem'
    #最后保存结果的文件夹
    store_path =r'.\测试'
    if os.path.exists(store_path):
        print("文件夹已存在，请重新创建新文件夹！")
        raise SystemExit()
    else:
        os.mkdir(store_path)
    m = word2pic(path, zip_path, tmp_path, store_path)


