from tkinter import *
fields = ('Username 1', 'Password 1', 'Username 2', 'Password 2', 'Username 3', 'Password 3', 'Username 4', 'Password 4', 'Username 5', 'Password 5', 'Time')

def fetch(entries):
   for entry in entries:
      field = entry[0]
      text  = entry[1].get()
      print('%s: "%s"' % (field, text))

def makeform(root, fields):
   entries = []
   count = 0
   for field in fields:
      row = Frame(root)
      if count == 1:
          userNameLab = Label(row, text="Username", fg="#383a39", bg="#a1dbcd", font=("Helvetica", 16))
          passwordLab = Label(row, text="Password", fg="#383a39", bg="#a1dbcd", font=("Helvetica", 16))
          userNameLab.pack(side=LEFT)
          passwordLab.pack(side=RIGHT)
      userNameEnt = Entry(row, width=40)
      passwordEnt = Entry(row, width=40)
      row.pack(side=TOP, padx=5, pady=5)
      userNameEnt.pack(side=RIGHT, fill=X)
      passwordEnt.pack(side=LEFT, fill=X)
      entries.append((field, userNameEnt))
      count = count + 1
   return entries

if __name__ == '__main__':
     window = Tk()
     window.configure(background="#a1dbcd")
     window.title("InstaClient")
     photo = PhotoImage(file="instagram-logo.gif")
     logo = Label(window, image=photo)
     logo.pack(side=TOP)

     lblInst = Label(window, text="Instagram users:", fg="#383a39", bg="#a1dbcd", font=("Helvetica", 16))
     lblInst.pack()

     ents = makeform(window, fields)
     window.bind('<Return>', (lambda event, e=ents: fetch(e)))

     lblInst1 = Label(window, text="Please insert the time:", fg="#383a39", bg="#a1dbcd",
                     font=("Helvetica", 14))
     lblInst1.pack()

     lblTime = Label(window, width=15, text="Time", anchor='w')
     timeInput = Entry(window)
     lblTime.pack(side=LEFT)
     timeInput.pack(side=RIGHT, fill=X)

     b1 = Button(window, text='Start',
               command=(lambda e=ents: fetch(e)))
     b1.pack(side=LEFT, padx=5, pady=5)
     b2 = Button(window, text='Quit', command=window.quit)
     b2.pack(side=LEFT, padx=5, pady=5)
window.mainloop()