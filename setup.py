import os

os.system('echo aaaa')


def finish():
    print("完成")
    os.system(clear)

def installSoftware():
    # os.system(clear)
    def steam():
        print("")
    def vscode():
        print("")
    print("请选择你要安装的软件")
    print("a steam\nb vscode \nc Github Desktop \nd matlab \ne typora\n\nq finish")
    option2 = {
    'a': steam,
    'b': vscode,

    'q': finish   
    
}
    optionInput = input("")
    option2[optionInput]0


def microsoftConfig():
    print("配置微软账户\n")
    print("回车填入 ")
    a = input("输入微软账户邮箱")
    print("回车填入主机名 ")
    b = input("输入主机名")
    os.system(clear)         #不知道怎么回到main
    
    
def finish():
    print("完成")
    os.system(clear)


option = {
    '0': installSoftware,
    '1': microsoftConfig,

    'q': finish   

}

    
print ("Hello.\n请选择要进行的配置\n")
print ("0 安装必备软件 \n1 配置 Microsoft 账户 \n2 \n\nq 退出")

optionInput = input("")
main = option[optionInput]
main()
    

