from tkinter import *
from InstagramAPI import InstagramAPI
import time
from UserPostDetails import UserPostDetails

window = Tk()
window.geometry('600x600')
window.title("InstaClient")

userName = Label(window, text="UserName", font=("Arial Bold", 14))
userName.grid(column=10, row=10)
passWord = Label(window, text="Password", font=("Arial Bold", 14))
passWord.grid(column=150, row=10)

userName1 = Entry(window, width=30)
userName1.grid(column=10, row=30)

userName2 = Entry(window, width=30)
userName2.grid(column=10, row=50)

userName3 = Entry(window, width=30)
userName3.grid(column=10, row=70)

userName4 = Entry(window, width=30)
userName4.grid(column=10, row=90)

userName5 = Entry(window, width=30)
userName5.grid(column=10, row=110)

userName6 = Entry(window, width=30)
userName6.grid(column=10, row=130)

userName7 = Entry(window, width=30)
userName7.grid(column=10, row=150)

userName8 = Entry(window, width=30)
userName8.grid(column=10, row=170)

userName9 = Entry(window, width=30)
userName9.grid(column=10, row=190)

userName10 = Entry(window, width=30)
userName10.grid(column=10, row=210)

passWord1 = Entry(window, width=30)
passWord1.grid(column=150, row=30)

passWord2 = Entry(window, width=30)
passWord2.grid(column=150, row=50)

passWord3 = Entry(window, width=30)
passWord3.grid(column=150, row=70)

passWord4 = Entry(window, width=30)
passWord4.grid(column=150, row=90)

passWord5 = Entry(window, width=30)
passWord5.grid(column=150, row=110)

passWord6 = Entry(window, width=30)
passWord6.grid(column=150, row=130)

passWord7 = Entry(window, width=30)
passWord7.grid(column=150, row=150)

passWord8 = Entry(window, width=30)
passWord8.grid(column=150, row=170)

passWord9 = Entry(window, width=30)
passWord9.grid(column=150, row=190)

passWord10 = Entry(window, width=30)
passWord10.grid(column=150, row=210)

def startBtnClick():
    uname1 = userName1.get().strip()
    pwd1 = passWord1.get().strip()
    uname2 = userName2.get().strip()
    pwd2 = passWord2.get().strip()
    uname3 = userName3.get().strip()
    pwd3 = passWord3.get().strip()
    uname4 = userName4.get().strip()
    pwd4 = passWord4.get().strip()
    uname5 = userName5.get().strip()
    pwd5 = passWord5.get().strip()
    uname6 = userName6.get().strip()
    pwd6 = passWord6.get().strip()
    uname7 = userName7.get().strip()
    pwd7 = passWord7.get().strip()
    uname8 = userName8.get().strip()
    pwd8 = passWord8.get().strip()
    uname9 = userName9.get().strip()
    pwd9 = passWord9.get().strip()
    uname10 = userName10.get().strip()
    pwd10 = passWord10.get().strip()

    credentials = dict()

    if uname1 and pwd1:
        print("1st things")
        InstagramAPI1 = InstagramAPI(uname1,pwd1)
        login = InstagramAPI1.login()
        time.sleep(2)
        if login:
            credentials[uname1] = InstagramAPI1

    if not uname2 and pwd2:
        InstagramAPI2 = InstagramAPI(uname2, pwd2)
        login = InstagramAPI2.login()
        time.sleep(2)
        if login:
            credentials[uname2] = InstagramAPI2

    if not uname3 and pwd3:
        InstagramAPI3 = InstagramAPI(uname3, pwd3)
        login = InstagramAPI3.login()
        time.sleep(2)
        if login:
            credentials[uname3] = InstagramAPI3

    if not uname4 and pwd4:
        InstagramAPI4 = InstagramAPI(uname4, pwd4)
        login = InstagramAPI4.login()
        time.sleep(2)
        if login:
            credentials[uname4] = InstagramAPI4

    if not uname5 and pwd5:
        InstagramAPI5 = InstagramAPI(uname5, pwd5)
        login = InstagramAPI5.login()
        time.sleep(2)
        if login:
            credentials[uname5] = InstagramAPI5

    if not uname6 and pwd6:
        InstagramAPI6 = InstagramAPI(uname6, pwd6)
        login = InstagramAPI6.login()
        time.sleep(2)
        if login:
            credentials[uname6] = InstagramAPI6

    if not uname7 and pwd7:
        InstagramAPI7 = InstagramAPI(uname7, pwd7)
        login = InstagramAPI7.login()
        time.sleep(2)
        if login:
            credentials[uname7] = InstagramAPI7

    if not uname8 and pwd8:
        InstagramAPI8 = InstagramAPI(uname8, pwd8)
        login = InstagramAPI8.login()
        time.sleep(2)
        if login:
            credentials[uname8] = InstagramAPI8

    if not uname9 and pwd9:
        InstagramAPI9 = InstagramAPI(uname9, pwd9)
        login = InstagramAPI9.login()
        time.sleep(2)
        if login:
            credentials[uname9] = InstagramAPI9

    if not uname10 and pwd10:
        InstagramAPI10 = InstagramAPI(uname10, pwd10)
        login = InstagramAPI10.login()
        time.sleep(2)
        if login:
            credentials[uname10] = InstagramAPI10

    UserPostDetails.userPostDetails(credentials)

startBtn = Button(window, text="Start", command=startBtnClick)
startBtn.grid(column=10, row=230)

window.mainloop()