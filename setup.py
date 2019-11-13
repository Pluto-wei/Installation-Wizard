import os
import color
import download

os.system('echo aaaa')

def exe():
    None


def installSoftware():
    # os.system(clear) #错了姐姐

    def steam():
        print("downloading steam...")
        ad="https://media.st.dl.bscstorage.net/client/installer/SteamSetup.exe"
        download.downld(ad)
    def vscode():
        print("downloading vscode for win32-x64...")
        ad="https://aka.ms/win32-x64-user-stable"
        download.downld(ad)
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


def microsoftConfig():
    print("配置微软账户\n")
    print("回车填入 ")
    a = input("输入微软账户邮箱")
    print("回车填入主机名 ")
    b = input("输入主机名")#不知道怎么回到main  #用循环怎么样
    
    
def finish():
    color.printYellow("完成")
    os.system('cls')


option = {
    '0': installSoftware,
    '1': microsoftConfig,

    'q': finish  

}
  
color.printBlue ("Hello.\n请选择要进行的配置\n")
color.printRed ("0 安装必备软件 \n1 配置 Microsoft 账户 \n2 \n\nq 退出")


optionInput = input("")
exe = option[optionInput]
exe()
    

