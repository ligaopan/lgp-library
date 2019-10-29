import base64
import os
    
class demo_library():    
    def Base_64(self,PATH,IMGNAME):
#         base_dir =os.path.dirname(__file__)#获取当前文件夹的绝对路径
#         base_dir = os.path.abspath(os.path.dirname(base_dir))
#         print(base_dir)
#         a='3.jpg'
        file_path = os.path.join(PATH,IMGNAME) #获取base_dir+'/image'文件夹内的文件
        f=open(file_path,'rb') #二进制方式打开图文件
        lsReadImage_f=base64.b64encode(f.read())#读取文件内容，转换为base64编码
        f.close()#关闭文件
        return    lsReadImage_f


  