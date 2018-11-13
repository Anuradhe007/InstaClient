from tkinter import *

def handleStartBtn():
    for entry in ents:
        field = entry[0]
        text = entry[1].get()
        print('%s: "%s"' % (field, text))

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
          b1 = Button(window, text='Start', command=handleStartBtn)
          b1.pack(side=RIGHT, padx=5, pady=2)
          b2 = Button(window, text='Stop', command=window.quit)
          b2.pack(side=RIGHT, padx=5, pady=2)

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