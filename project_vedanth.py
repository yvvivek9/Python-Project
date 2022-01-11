from tkinter import *
root=Tk()
def Teacher():
    root.destroy()
    loot=Tk()
    tlabel=Label(loot,text='Welcome to teachers login page')
    tlabel.config(font=('Helvetica bold',40))
    tlabel.pack()     jhdfxgfs
    te1=Entry(loot,width=50,borderwidth=1)
    te1.insert(0,'Enter Password: ')
    te1.pack()
    def Tview():
        a=te1.get()
        if a=='admin123':
            loot.destroy()
            t_1=Tk()
            
        else:
            mylabel3=Label(loot,text='Wrong password')
            mylabel3.pack()
        
    tb1=Button(loot,text='Login',command=Tview)
    tb1.pack()
    loot.mainloop()
def Student():
    root.destroy()
    noot=Tk()
    slabel=Label(noot,text='Welcome to Students login page')
    slabel.config(font=('Helvetica bold',40))
    slabel.pack()
    se1=Entry(noot,width=50,borderwidth=1)
    se1.insert(0,'Enter SRN: ')
    se1.pack()
    sb1=Button(noot,text='Login')
    sb1.pack()
    def Add():
        noot.destroy()
        add_1=Tk()
        mylabel2=Label(add_1,text='Create new login')
        mylabel2.config(font=('Helvetica bold',20))
        mylabel2.pack()
        ae1=Entry(add_1,width=40,borderwidth=5)
        ae1.insert(0,'Enter SRN: ')
        ae1.pack()
        ae2=Entry(add_1,width=40,borderwidth=5)
        ae2.insert(0,'Enter name: ')
        ae2.pack()
        ae3=Entry(add_1,width=40,borderwidth=5)
        ae3.insert(0,'Enter semester: ')
        ae3.pack()
        ae4=Entry(add_1,width=40,borderwidth=5)
        ae4.insert(0,'Enter total marks: ')
        ae4.pack()
        def Save():
            srn=ae1.get()
            name=ae2.get()
            sem=ae3.get()
            marks=ae4.get()
            if srn.isalnum() and name.isalpha() and sem.isdigit() and marks.isdigit():







                
                mylabel4=Label(add_1,text='Wrong entries')
                mylabel4.pack()
        ba1=Button(add_1,text='Save',command=Save)
        ba1.pack()
        add_1.mainloop()

    sb2=Button(noot,text='Create new',command=Add)
    sb2.pack()
    noot.mainloop()


mylabel1=Label(root,text='Welcome to Info')
mylabel1.pack()
button1=Button(root,text='Teacher',command=Teacher)
button1.pack()
button2=Button(root,text='Student',command=Student)
button2.pack()















