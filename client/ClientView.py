from tkinter import *
from InstagramAPI import InstagramAPI
import time
from ClientScheduler import ClientScheduler
import sys

def handleStartBtn():
    pwd1 = ents[0][1].get().strip()
    uname1 = ents[1][1].get().strip()
    pwd2 = ents[2][1].get().strip()
    uname2 = ents[3][1].get().strip()
    pwd3 = ents[4][1].get().strip()
    uname3 = ents[5][1].get().strip()
    pwd4 = ents[6][1].get().strip()
    uname4 = ents[7][1].get().strip()
    pwd5 = ents[8][1].get().strip()
    uname5 = ents[9][1].get().strip()
    pwd6 = ents[10][1].get().strip()
    uname6 = ents[11][1].get().strip()
    pwd7 = ents[12][1].get().strip()
    uname7 = ents[13][1].get().strip()
    pwd8 = ents[14][1].get().strip()
    uname8 = ents[15][1].get().strip()
    uname9 = ents[16][1].get().strip()
    pwd9 = ents[17][1].get().strip()
    pwd10 = ents[18][1].get().strip()
    uname10 = ents[19][1].get().strip()

    time1 = ents[20][1]
    proxy = ents[21][1]
    file = ents[22][1]

    credentials = dict()

    if uname1 and pwd1:
        InstagramAPI1 = InstagramAPI(uname1, pwd1)
        login = InstagramAPI1.login()
        time.sleep(2)
        if login:
            credentials[uname1] = InstagramAPI1

    if uname2 and pwd2:
        InstagramAPI2 = InstagramAPI(uname2, pwd2)
        login = InstagramAPI2.login()
        time.sleep(2)
        if login:
            credentials[uname2] = InstagramAPI2

    if uname3 and pwd3:
        InstagramAPI3 = InstagramAPI(uname3, pwd3)
        login = InstagramAPI3.login()
        time.sleep(2)
        if login:
            credentials[uname3] = InstagramAPI3

    if uname4 and pwd4:
        InstagramAPI4 = InstagramAPI(uname4, pwd4)
        login = InstagramAPI4.login()
        time.sleep(2)
        if login:
            credentials[uname4] = InstagramAPI4

    if uname5 and pwd5:
        InstagramAPI5 = InstagramAPI(uname5, pwd5)
        login = InstagramAPI5.login()
        time.sleep(2)
        if login:
            credentials[uname5] = InstagramAPI5

    if uname6 and pwd6:
        InstagramAPI6 = InstagramAPI(uname6, pwd6)
        login = InstagramAPI6.login()
        time.sleep(2)
        if login:
            credentials[uname6] = InstagramAPI6

    if uname7 and pwd7:
        InstagramAPI7 = InstagramAPI(uname7, pwd7)
        login = InstagramAPI7.login()
        time.sleep(2)
        if login:
            credentials[uname7] = InstagramAPI7

    if uname8 and pwd8:
        InstagramAPI8 = InstagramAPI(uname8, pwd8)
        login = InstagramAPI8.login()
        time.sleep(2)
        if login:
            credentials[uname8] = InstagramAPI8

    if uname9 and pwd9:
        InstagramAPI9 = InstagramAPI(uname9, pwd9)
        login = InstagramAPI9.login()
        time.sleep(2)
        if login:
            credentials[uname9] = InstagramAPI9

    if uname10 and pwd10:
        InstagramAPI10 = InstagramAPI(uname10, pwd10)
        login = InstagramAPI10.login()
        time.sleep(2)
        if login:
            credentials[uname10] = InstagramAPI10

    clientScheduler = ClientScheduler(time1, proxy, file, credentials)
    clientScheduler.schedulerInitialize()

def startBtnClick():
    handleStartBtn()

def handleStopBtn():
    sys.exit()

def makeform(root):
   entries = []
   count = 0
   for field in range(1, 15):
      row = Frame(root)
      row.pack(side=TOP, padx=5, pady=2)
      if count < 10:
          userNameLab = Label(row, text="Username", fg="#383a39", bg="#a1dbcd", font=("Helvetica", 12))
          passwordLab = Label(row, text="Password", fg="#383a39", bg="#a1dbcd", font=("Helvetica", 12))
          userNameLab.pack(side=LEFT)

          passworsEnt = Entry(row, width=40)
          entries.append(('password'+str(field), passworsEnt))
          userNameEnt = Entry(row, width=40)
          entries.append(('username'+str(field), userNameEnt))
          passworsEnt.pack(side=RIGHT, fill=X)
          passwordLab.pack(side=RIGHT)
          userNameEnt.pack(side=LEFT, fill=X)

      if count == 10:
        timeLab = Label(row, text="Time", fg="#383a39", bg="#a1dbcd", font=("Helvetica", 12))
        timeLab.pack(side=LEFT)
        timeEnt = Entry(row, width=60)
        timeEnt.pack(side=RIGHT, fill=X)
        entries.append(('time' + str(field), timeEnt))

      if count == 11:
        proxyLab = Label(row, text="Proxy", fg="#383a39", bg="#a1dbcd", font=("Helvetica", 12))
        proxyLab.pack(side=LEFT)
        proxyEnt = Entry(row, width=60)
        proxyEnt.pack(side=RIGHT, fill=X)
        entries.append(('proxy' + str(field), proxyEnt))

      if count == 12:
        filesLab = Label(row, text="Files", fg="#383a39", bg="#a1dbcd", font=("Helvetica", 12))
        filesLab.pack(side=LEFT)
        filesEnt = Entry(row, width=60)
        filesEnt.pack(side=RIGHT, fill=X)
        entries.append(('files' + str(field), filesEnt))

      if count == 13:
          b1 = Button(window, text='Start', command=startBtnClick)
          b1.pack(side=RIGHT, padx=5, pady=2)
          # b2 = Button(window, text='Stop', command=handleStopBtn)
          # b2.pack(side=RIGHT, padx=5, pady=2)

      count = count + 1
   return entries

window = Tk()
window.configure(background="#a1dbcd")
window.title("InstaClient")
photo = PhotoImage(file="insta-client-logo.gif")
logo = Label(window, image=photo)
logo.pack(side=TOP)

ents = makeform(window)

window.mainloop()