import os
import color
import download
#创建 调用颜色函数
import platform
import sys
import ctypes
__stdInputHandle = -10
__stdOutputHandle = -11
__stdErrorHandle = -12
__foreGroundBLUE = 0x09
__foreGroundGREEN = 0x0a
__foreGroundRED = 0x0c
__foreGroundYELLOW = 0x0e
stdOutHandle=ctypes.windll.kernel32.GetStdHandle(__stdOutputHandle)
def setCmdColor(color,handle=stdOutHandle):
    return ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
def resetCmdColor():
    setCmdColor(__foreGroundRED | __foreGroundGREEN | __foreGroundBLUE)
def printBlue(msg):
    setCmdColor(__foreGroundBLUE)
    sys.stdout.write(msg + '\n')
    resetCmdColor()
def printGreen(msg):
    setCmdColor(__foreGroundGREEN)
    sys.stdout.write(msg + '\n')
    resetCmdColor()
def printRed(msg):
    setCmdColor(__foreGroundRED)
    sys.stdout.write(msg + '\n')
    resetCmdColor()
def printYellow(msg):
    setCmdColor(__foreGroundYELLOW)
    sys.stdout.write(msg + '\n')
    resetCmdColor()
#over 好难啊看不懂ww

#添加 下载 指令
import urllib.request
def downld(ad):
    url=ad
    root="D://"
    path=root+url.split('/')[-1]
    urllib.request.urlretrieve(url,path)
    
def exe():
    None
#我懂了！！就跟main是一样的，原来给main赋一个函数值然后运行main函数，这里就把main换成exe，
#但是exe需要定义，定义的时候不需要有啥，反正后面要赋别的函数，，到时候运行就vans
#欸 我又迷惑了，python里没有main函数，那也要定义吗，我记得我上次没定义

def again():
    os.system('cls')
    main()
    
def finish():
    color.printYellow("完成")     #应该在这个后面加，输回车后清屏
    



def installSoftware():
    # os.system(clear) #错了姐姐 #我没有！  #好好好

    def steam():
        print("downloading steam...")
        ad="https://media.st.dl.bscstorage.net/client/installer/SteamSetup.exe"
        download.downld(ad)
    def vscode():
        print("downloading vscode for win32-x64...")
        ad="https://vscode.cdn.azure.cn/stable/86405ea23e3937316009fc27c9361deee66ffbf5/VSCodeUserSetup-x64-1.40.0.exe"
        download.downld(ad)
        
    def main2():
        color.printBlue("请选择你要安装的软件")
        color.printGreen("a steam\nb vscode \nc Github Desktop \nd matlab \ne typora\n\nq finish")
        option2 = {
        'a': steam,
        'b': vscode,
    
        'q': finish   
        }
        optionInput = input("")
        exe=option2[optionInput]
        exe()
        finish()      #如果回车
        os.system('cls')
    main2()       #这个地方其实想回到 安装软件那一行（上一级），有简单的方法吗（好像要加个循环，直到q跳出循环。。。明天再加）


def microsoftConfig():
    print("配置微软账户\n")
    print("回车填入 ")
    a = input("输入微软账户邮箱")
    print("回车填入主机名 ")
    b = input("输入主机名") 
    finish()                      #怎么设置如果用户输入回车那么执行下一句again
    again()                       #不知道怎么回到main  #用循环怎么样 #好的！
    

option = {
    '0': installSoftware,
    '1': microsoftConfig,

    'q': finish  

}
def main():
    color.printBlue ("Hello.\n请选择要进行的配置\n")
    color.printRed ("0 安装必备软件 \n1 配置 Microsoft 账户 \n2 \n\nq 退出")
    optionInput = input("")
    exe = option[optionInput]
    exe()
    
#从这里开始。。。也不知道对不对 不知道python里面顺序有什么讲究，出现晚了有的还执行不了  #为什么要main
main()
