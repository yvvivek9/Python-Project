from tkinter import *
import pickle

root = Tk()


def Student():
    root.destroy()
    loot = Tk()
    tlabel = Label(loot, text='Welcome to Student login page')
    tlabel.config(font=('Helvetica bold', 20))
    tlabel.grid(row=0,column=1)
    te1 = Entry(loot, width=50, borderwidth=1).grid(row=1,column=1)
    l=Label(loot,text='Enter SRN:').grid(row=1,column=0)

    def Sview():
        with open("STUDENT.DAT", "rb") as F:
            c = False
            try:
                while not c:
                    R = pickle.load(F)
                    for i in R:
                        if te1.get() == i[0]:
                            loot.destroy()
                            t_1 = Tk()
                            mylabel31 = Label(t_1, text=i)
                            mylabel31.pack()
                            c = True
                            break
            except:
                mylabel3 = Label(loot, text='Student not found')
                mylabel3.pack()

    tb1 = Button(loot, text='Login', command=Sview).grid(row=3,column=1)
    loot.mainloop()


def Teacher():
    root.destroy()
    noot = Tk()
    slabel = Label(noot, text='Welcome to Teachers login page')
    slabel.config(font=('Helvetica bold', 20))
    slabel.grid(row=0,column=1)
    se1 = Entry(noot, width=50, borderwidth=1)
    se1.grid(row=1,column=1)
    se2=Label(noot,text='Enter password: ').grid(row=1,column=0)
    def login():
        if se1.get() == 'admin123':
            noot.destroy()
            addorsee = Tk()
            mylabel12 = Label(addorsee, text='Would you like to add students or delete existing ones').grid(row=1,column=0)

            def Add():
                add_1 = Tk()
                mylabel2 = Label(add_1, text='Create new Student')
                mylabel2.config(font=('Helvetica bold', 20))
                mylabel2.grid(row=0,column=0)
                ae1 = Entry(add_1, width=40, borderwidth=5).grid(row=1,column=1)
                le1=Label(add_1,text='Enter SRN: ').grid(row=1,column=0)
                ae2 = Entry(add_1, width=40, borderwidth=5).grid(row=2,column=1)
                le2=Label(add_1,text='Enter Name:').grid(row=2,column=0)
                ae3 = Entry(add_1, width=40, borderwidth=5).grid(row=3,column=1)
                le3=Label(add_1,text='Enter Semester:').grid(row=3,column=0)
                ae4 = Entry(add_1, width=40, borderwidth=5).grid(row=4,column=1)
                le4=Label(add_1,text='Enter marks for Physics:').grid(row=4,column=0)
                ae5 = Entry(add_1, width=40, borderwidth=5).grid(row=5,column=1)
                le5=Label(add_1,text='Enter marks for Maths:').grid(row=5,column=0)
                ae6 = Entry(add_1, width=40, borderwidth=5).grid(row=6,column=1)
                le6=Label(add_1,text='Enter marks for Computers:').grid(row=6,column=0)
                ae7 = Entry(add_1, width=40, borderwidth=5).grid(row=7,column=1)
                le7=Label(add_1,text='Enter marks for Electrical:').grid(row=7,column=0)
                ae8 = Entry(add_1, width=40, borderwidth=5).grid(row=8,column=1)
                le8=Label(add_1,text='Enter marks for Mechanical:').grid(row=8,column=0)
                ae9 = Entry(add_1, width=40, borderwidth=5).grid(row=9,column=1)
                le9=Label(add_1,text='Enter marks for EVS:').grid(row=9,column=0)
    

                def Save():
                    srn = ae1.get()
                    name = ae2.get()
                    sem = ae3.get()
                    marksp = ae4.get()
                    marksm = ae5.get()
                    marksc = ae6.get()
                    markse = ae7.get()
                    marksme = ae8.get()
                    marksev = ae9.get()
                    if srn.isalnum() and (
                            name.isalpha() or ' ') and sem.isdigit() and marksp.isdigit() and marksm.isdigit() and marksme.isdigit() and marksc.isdigit() and markse.isdigit() and marksev.isdigit():
                        with open("STUDENT.DAT", "ab") as F:
                            R = []
                            R.append([srn, name, sem, marksp, marksm, marksc, markse, marksme, marksev])
                            pickle.dump(R, F)
                        add_1.destroy()


                    else:
                        mylabel9 = Label(add_1, text='Wrong entries')
                        mylabel9.pack()

                ab1 = Button(add_1, text='Save', command=Save).grid(row=10,column=1)

            addb1 = Button(addorsee, text='Add new', command=Add).grid(row=1,column=1)

            def Average():
                with open("STUDENT.DAT", "rb") as F:
                        c = False
                        while not c:
                                R = pickle.load(F)
                                for i in R:
                                      if avg.get() == i[0]:
                                          avg1 =(int(i[3])+int(i[4])+int(i[5])+int(i[6])+int(i[7])+int(i[8]))/6
                                          mymsg3 = Label(addorsee, text=avg1)
                                          mymsg3.pack()
                                          c = True
                                          break
                        if c==False:
                              mymsg4 = Label(addorsee, text='Student not found')
                              mymsg4.pack()

            mymsg = Label(addorsee, text="Enter SRN to check average of student: ").grid(row=2,column=0)
            avg = Entry(addorsee, width=40).grid(row=2,column=1)
            mybutton = Button(addorsee, text="Average", command=Average).grid(row=2,column=3)


            def Pass():
                with open("STUDENT.DAT", "rb") as F:
                        c = False
                        while not c:
                                R = pickle.load(F)
                                for i in R:
                                      if pas.get() == i[0]:
                                          t=3
                                          while t<9:
                                                if int(i[t])<40:
                                                      break
                                                else:
                                                      t+=1
                                          else:
                                                mymsg5=Label(addorsee,text='You passed!')
                                                mymsg5.pack()
                                                break
                                          mymsg3 = Label(addorsee, text='Fail')
                                          mymsg3.pack()
                                          c = True
                                          break
                        if c==False:
                              mymsg4 = Label(addorsee, text='Student not found')
                              mymsg4.pack()
            mymsg2 = Label(addorsee, text='Enter SRN to check  if student passed or failed: ').grid(row=3,column=0)
            pas = Entry(addorsee, width=40).grid(row=3,column=1)
            mybutton2 = Button(addorsee, text="Pass/Fail", command=Pass).grid(row=3,column=3)


            def Delete():
                with open("STUDENT.DAT", "rb+") as F:
                    c = False
                    try:
                        while not c:
                            R = pickle.load(F)
                            for i in R:
                                if de1.get() == i[0]:
                                    R.remove(i)
                                    mylabe31 = Label(addorsee,text='Student deleted')
                                    mylabe31.pack()
                                    c = True
                                    break
                    except:
                        mylabel3 = Label(loot, text='Student not found')
                        mylabel3.pack()

    

            mylabel10 = Label(addorsee, text='Enter SRN of student to be deleted: ').grid(row=4,column=0)
            de1 = Entry(addorsee, width=40).grid(row=4,column=1)
            addb2 = Button(addorsee, text='Delete', command=Delete).grid(row=4,column=3)


        else:
            mylabel8 = Label(noot, text='Wrong password')
            mylabel8.pack()

    sb1 = Button(noot, text='Login', command=login).grid(row=3,column=1)
    noot.mainloop()


mylabel1 = Label(root, text='Welcome to Info')
mylabel1.pack()
button1 = Button(root, text='Teacher', command=Teacher)
button1.pack()
button2 = Button(root, text='Student', command=Student)
button2.pack()

root.mainloop()
