from tkinter import *
fields = ('Username 1', 'Password 1', 'Username 2', 'Password 2', 'Username 3', 'Password 3', 'Username 4', 'Password 4', 'Username 5', 'Password 5', 'Time')

def fetch(entries):
   for entry in entries:
      field = entry[0]
      text  = entry[1].get()
      print('%s: "%s"' % (field, text))

def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=15, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries

if __name__ == '__main__':
     window = Tk()
     window.configure(background="#a1dbcd")
     window.title("InstaClient")
     photo = PhotoImage(file="instagram-logo.gif")

     w = Label(window, image=photo)
     w.pack()

     lblInst = Label(window, text="Please fill the instagram user details:", fg="#383a39", bg="#a1dbcd",
                             font=("Helvetica", 16))
     lblInst.pack()

     ents = makeform(window, fields)
     window.bind('<Return>', (lambda event, e=ents: fetch(e)))

     lblInst1 = Label(window, text="Please insert the time:", fg="#383a39", bg="#a1dbcd",
                     font=("Helvetica", 14))
     lblInst1.pack()

     lblTime = Label(window, width=15, text="Time", anchor='w')
     timeInput = Entry(window)
     lblTime.pack(side=LEFT)
     timeInput.pack(side=RIGHT, expand=YES, fill=X)

     b1 = Button(window, text='Start',
               command=(lambda e=ents: fetch(e)))
     b1.pack(side=LEFT, padx=5, pady=5)
     b2 = Button(window, text='Quit', command=window.quit)
     b2.pack(side=LEFT, padx=5, pady=5)
window.mainloop()