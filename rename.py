# _*_ coding: UTF-8 _*_
import os,shutil,re,glob
#文件目录
path =r''
file_filter=r"*.mp4"
#要替换的字符串
strToReplace="要替换掉的字符串"
#替换成的字符串，留空就相当于删掉
replace=""

filelist = os.listdir(path) #该文件夹下所有的文件（包括文件夹）
os.chdir(path)
for temp in glob.glob(file_filter):
    (filename,extension) = os.path.splitext(temp)
    newName=re.sub(strToReplace,replace,filename)+extension
    os.rename(temp,newName)#重命名
print("-----完成-----")

