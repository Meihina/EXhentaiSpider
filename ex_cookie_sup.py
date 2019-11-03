import tkinter  # 导入TKinter模块
import json

def loadFont():
    f = open("ex_cookies.json", encoding='utf-8')
    cookie = json.load(f)
    return cookie


def tk_cookier():

    def getuser_aw():
        cookie = {
            "igneous": igneous.get(),
            "ipb_member_id": id.get(),
            "ipb_pass_hash": hash.get(),
            "s": k.get(),
            "sk": sk.get(),
        }
        with open('ex_cookies.json', 'w', encoding='utf-8') as f:
            json.dump(cookie, f, indent=4)
        ytm.destroy()

    ytm = tkinter.Tk()  # 创建Tk对象
    ytm.title("EXhentai")  # 设置窗口标题
    ytm.geometry("500x200")  # 设置窗口尺寸

    l1 = tkinter.Label(ytm, text="请输入cookies,以igneous,id,hash,k,sk的顺序(不知道的请用chrome方式查询)")  # 标签
    l1.pack()  # 指定包管理器放置组件

    igneous = tkinter.Entry(ytm)
    id = tkinter.Entry(ytm)
    hash = tkinter.Entry(ytm)
    k = tkinter.Entry(ytm)
    sk = tkinter.Entry(ytm)
    igneous.pack()
    id.pack()
    hash.pack()
    k.pack()
    sk.pack()

    tkinter.Button(ytm, text="确定", command=getuser_aw).pack()  # command绑定获取文本框内容方法

    ytm.mainloop()  # 进入主循环



    # "igneous": "0ca092e8d",
    # "ipb_member_id": "2470365",
    # "ipb_pass_hash": "ec7ae285e201c2ee01e9e223f51063ab",
    # "s": "259ecd6c7",
    # "sk": "ac7jqbvn5o6ppw3ogm3280fbl9xj",