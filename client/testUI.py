from tkinter import *

root = Tk()
root.title("InstaClient")

topFrame = Frame(root)
topFrame.pack()
leftFrame = Frame(root)
leftFrame.pack(side=LEFT)
rightFrame = Frame(root)
rightFrame.pack(side=RIGHT)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

photo = PhotoImage(file="instagram-logo.gif")
logo = Label(topFrame, image=photo)
logo.pack(side=TOP)

lblInst = Label(topFrame, text="Instagram users:", fg="#383a39", bg="#a1dbcd", font=("Helvetica", 16))
lblInst.pack(side=TOP)

leftFrameLabel1 = Label(leftFrame, text="Username", fg="#383a39", bg="#a1dbcd", font=("Helvetica", 16))
leftFrameLabel1.pack(side=LEFT, padx=20)
rightFrameLabel1 = Label(leftFrame, text="Password", fg="#383a39", bg="#a1dbcd", font=("Helvetica", 16))
rightFrameLabel1.pack(side=RIGHT, fill=X, padx=20)

entUserName1 = Entry(leftFrame, width=40)
entUserName1.pack(side=LEFT, padx=20, pady=2)
entPassowrd1 = Entry(leftFrame, width=40)
entPassowrd1.pack(side=RIGHT, padx=20, pady=2)

entUserName2 = Entry(leftFrame, width=40)
entUserName2.pack(side=LEFT, padx=20, pady=2)
entPassowrd2 = Entry(leftFrame, width=40)
entPassowrd2.pack(side=RIGHT, padx=20, pady=2)

entUserName3 = Entry(leftFrame, width=40)
entUserName3.pack(side=LEFT, padx=20, pady=2)
entPassowrd3 = Entry(leftFrame, width=40)
entPassowrd3.pack(side=RIGHT, padx=20, pady=2)

entUserName4 = Entry(leftFrame, width=40)
entUserName4.pack(side=LEFT, padx=20, pady=2)
entPassowrd4 = Entry(leftFrame, width=40)
entPassowrd4.pack(side=RIGHT, padx=20, pady=2)

entUserName5 = Entry(leftFrame, width=40)
entUserName5.pack(side=LEFT, padx=20, pady=2)
entPassowrd5 = Entry(leftFrame, width=40)
entPassowrd5.pack(side=RIGHT, padx=20, pady=2)

entUserName6 = Entry(leftFrame, width=40)
entUserName6.pack(side=LEFT, padx=20, pady=2)
entPassowrd6 = Entry(leftFrame, width=40)
entPassowrd6.pack(side=RIGHT, padx=20, pady=2)

entUserName7 = Entry(leftFrame, width=40)
entUserName7.pack(side=LEFT, padx=20, pady=2)
entPassowrd7 = Entry(leftFrame, width=40)
entPassowrd7.pack(side=RIGHT, padx=20, pady=2)

entUserName8 = Entry(leftFrame, width=40)
entUserName8.pack(side=LEFT, padx=20, pady=2)
entPassowrd8 = Entry(leftFrame, width=40)
entPassowrd8.pack(side=RIGHT, padx=20, pady=2)

entUserName9 = Entry(leftFrame, width=40)
entUserName9.pack(side=LEFT, padx=20, pady=2)
entPassowrd9 = Entry(leftFrame, width=40)
entPassowrd9.pack(side=RIGHT, padx=20, pady=2)

entUserName10 = Entry(leftFrame, width=40)
entUserName10.pack(side=LEFT, padx=20, pady=2)
entPassowrd10 = Entry(leftFrame, width=40)
entPassowrd10.pack(side=RIGHT, padx=20, pady=2)

proxyLabel = Label(leftFrame, text="")
proxyLabel.pack(padx=20, pady=10)

# proxyLabel = Label(leftFrame, text="Path to proxy file", fg="#383a39", font=("Helvetica", 12))
# proxyLabel.pack(side=LEFT, padx=20, pady=10)
# proxyEnt = Entry(leftFrame, width=60)
# proxyEnt.pack(side=RIGHT, padx=20, pady=10)
#
# filePath = Label(leftFrame, text="File saving path", fg="#383a39", font=("Helvetica", 12))
# filePath.pack(side=LEFT, padx=20, pady=10)
# filePathEnt = Entry(leftFrame, width=60)
# filePathEnt.pack(side=RIGHT, fill=X)

btnStart = Button(leftFrame, text="Start")
btnStart.pack(side=BOTTOM)

root.mainloop()

