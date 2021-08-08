from tkinter import*

root=Tk()
root.geometry('700x500+5+5')
root.configure(bg='brown')
#===================================================
def click():
    x=input('Enter your name:')
    print('your name is: ',x)
bt=Button(root,text='reset',bd=50,bg='yellow',fg='red'
          ,activebackground='yellOW',activeforeground='yellow',relief='raised'
          ,command=click)
bt.pack(side=BOTTOM)
#====================================================================
z='''
uyu
'''
lb=Label(root,text=z,bd=10,bg='brown',fg='white'
         ,relief='raised',font=('times new roman',14,'bold'))
lb.pack(padx=1,pady=1)

#======================================================================

ant=Entry(root,bg='yellow',bd=10,fg='green'
          ,font=('times new roman',20),width=30)
ant.pack(padx=150,pady=30)


root.mainloop()
