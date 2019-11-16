import os
import color
import download
#创建 调用颜色函数    #我在color.py里改了有linux的 这里没有
import platform
import sys
import ctypes
__stdInputHandle = -10    #标准输入句柄
__stdOutputHandle = -11    #标准输出句柄
__stdErrorHandle = -12    #标准错误句柄
__foreGroundBLUE = 0x09    #前景色 CMD命令行字体颜色定义
__foreGroundGREEN = 0x0a
__foreGroundRED = 0x0c
__foreGroundYELLOW = 0x0e
__foreGroundWHITE = 0x0f
__backGroundDARKSKYBLUE = 0x30    #后景色 #这里改了 color.py没有
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
def printWhite(msg):    #新增
    setCmdColor(__backGroundDARKSKYBLUE | __foreGroundWHITE)
    sys.stdout.write(msg + '\n')
    resetCmdColor()

#添加 下载 指令
import urllib.request
def downld(ad):
    url=ad
    root="C://"
    path=root+url.split('/')[-1]
    urllib.request.urlretrieve(url,path)
def exe1():
    None   
def exe2():
    None

def again():
    main()
    
def finish():
    color.printYellow("完成")     #应该在这个后面加，输回车后清屏
    if input("输入回车")=="":
        os.system('cls')
    return 1



def installSoftware():
    # os.system(clear) #错了姐姐 #我没有！  #好好好
    inCtrl=0
    while inCtrl==0:
        def steam():
            print("downloading steam...")
            ad="https://media.st.dl.bscstorage.net/client/installer/SteamSetup.exe"
            download.downld(ad)
            color.printYellow("完成！")
            return 0;
            #name="SteamSetup.exe"    #想不到从ad上直接截下来的方法 好像能用split 害
            #download.install(name)    #失败
        def vscode():
            print("downloading vscode for win32-x64...")
            ad="https://vscode.cdn.azure.cn/stable/86405ea23e3937316009fc27c9361deee66ffbf5/VSCodeUserSetup-x64-1.40.0.exe"
            download.downld(ad)
            color.printYellow("完成！")
            return 0;
        def Github_Desktop():
            print("downloading Github_Desktop...")
            ad="https://desktop.githubusercontent.com/releases/2.2.3-3e4755f1/GitHubDesktopSetup.exe"
            download.downld(ad)
            color.printYellow("完成！")
            return 0;
        def typora():
            print("downloading typora...")
            #ad="https://www.typora.io/windows/typora-setup-x64.exe"
            #download.downld(ad)
            #color.printYellow("完成！")
            color.printYellow("Sorry，该网站禁止爬虫...")
            return 0;
        color.printBlue("请选择你要安装的软件")
        color.printGreen("a steam\nb vscode \nc Github Desktop \nd typora\n\nq finish")
        option2 = {
        'a': steam,
        'b': vscode,
        'c': Github_Desktop,
        'd': typora,
        'q': finish   
        }
        optionInput = input("")
        if optionInput != 'a'and optionInput != 'b'and optionInput != 'c'and optionInput != 'd'and optionInput != 'q' :
            color.printYellow("你是猪ma？")
        else:
            exe2=option2[optionInput]
            inCtrl=exe2()
     
    return 0

def microsoftConfig():
    print("配置微软账户\n")
    print("回车填入 ")
    a = input("输入微软账户邮箱")
    print("回车填入主机名 ")
    b = input("输入主机名") 
    finish()                      #怎么设置如果用户输入回车那么执行下一句again
    again()                       #不知道怎么回到main  #用循环怎么样 #好的！

def backgroundPicture():
    color.printYellow("对不起……我还没学会~")
    return 0


option = {
    '0': installSoftware,
    '1': microsoftConfig,
    '2': backgroundPicture,
    'q': finish  

}
def main():
    printBlue ("Hello.\n请选择要进行的配置\n")
    outCtrl=0
    while outCtrl==0:
        color.printRed ("0 下载必备软件包 \n1 配置 Microsoft 账户 \n2 指定登录界面背景图片 \n\nq 退出")
        optionInput = input("")
        exe1 = option[optionInput]
        outCtrl=exe1()
    
main()
