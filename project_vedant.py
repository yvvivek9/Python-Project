from tkinter import *
import pickle
from PIL import Image, ImageTk


root = Tk()
root.title("ABC Institutes")
root.geometry("640x340")


def Student():
    root.destroy()
    loot = Tk()
    loot.title("ABC Institutes")
    loot.geometry("640x340")
    login_page = PhotoImage(file="login page.png")
    login_bg = Label(loot, image=login_page)
    login_bg.place(x=0, y=0)
    tlabel = Label(loot, text='Welcome to Student login page')
    tlabel.config(font=('Helvetica bold', 20))
    tlabel.place(x=120, y=15)
    te1 = Entry(loot, width=40, borderwidth=1).place(x=190, y=171)
    l = Label(loot, text='Enter SRN:').place(x=120, y=170)

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
                            t_1.title("ABC Institutes")
                            mylabel31 = Label(t_1, text=i)
                            mylabel31.pack()
                            c = True
                            break
            except:
                mylabel3 = Label(loot, text='Student not found')
                mylabel3.place(x=250,y=300)

    tb1 = Button(loot, text='Login', command=Sview).place(x=280, y=200)
    loot.mainloop()


def Teacher():
    root.destroy()
    noot = Tk()
    noot.title("ABC Institutes")
    noot.geometry("640x340")
    login_page = PhotoImage(file="login page.png")
    login_bg = Label(noot, image=login_page)
    login_bg.place(x=0, y=0)
    slabel = Label(noot, text='Welcome to Teachers login page')
    slabel.config(font=('Helvetica bold', 20))
    slabel.place(x=120, y=15)
    se1 = Entry(noot, width=40, borderwidth=1)
    se1.place(x=220, y=171)
    se2 = Label(noot, text='Enter password: ')
    se2.place(x=120, y=170)

    def login():
        if se1.get() == '1':
            noot.destroy()
            addorsee = Tk()
            addorsee.title("ABC Institutes")
            addorsee.geometry("800x600")
            background_image = PhotoImage(file = "background1.png")
            background_label = Label(addorsee, image=background_image)
            background_label.place(x=0,y=0)
            mylabel12 = Label(addorsee, text='Would you like to add students or manage existing ones')
            mylabel12.config(font=('Helvetica bold', 20))
            mylabel12.place(x=55,y=15)

            def Add():
                add_1 = Tk()
                add_1.title("ABC Institutes")
                mylabel2 = Label(add_1, text='Create new Student')
                mylabel2.config(font=('Helvetica bold', 20))
                mylabel2.grid(row=0, column=0)
                ae1 = Entry(add_1, width=40, borderwidth=5)
                ae1.grid(row=1, column=1)
                le1 = Label(add_1, text='Enter SRN: ')
                le1.grid(row=1, column=0)
                ae2 = Entry(add_1, width=40, borderwidth=5)
                ae2.grid(row=2, column=1)
                le2 = Label(add_1, text='Enter Name:')
                le2.grid(row=2, column=0)
                ae3 = Entry(add_1, width=40, borderwidth=5)
                ae3.grid(row=3, column=1)
                le3 = Label(add_1, text='Enter Semester:')
                le3.grid(row=3, column=0)
                ae4 = Entry(add_1, width=40, borderwidth=5)
                ae4.grid(row=4, column=1)
                le4 = Label(add_1, text='Enter marks for Physics:')
                le4.grid(row=4, column=0)
                ae5 = Entry(add_1, width=40, borderwidth=5)
                ae5.grid(row=5, column=1)
                le5 = Label(add_1, text='Enter marks for Maths:')
                le5.grid(row=5, column=0)
                ae6 = Entry(add_1, width=40, borderwidth=5)
                ae6.grid(row=6, column=1)
                le6 = Label(add_1, text='Enter marks for Computers:')
                le6.grid(row=6, column=0)
                ae7 = Entry(add_1, width=40, borderwidth=5)
                ae7.grid(row=7, column=1)
                le7 = Label(add_1, text='Enter marks for Electrical:')
                le7.grid(row=7, column=0)
                ae8 = Entry(add_1, width=40, borderwidth=5)
                ae8.grid(row=8, column=1)
                le8 = Label(add_1, text='Enter marks for Mechanical:')
                le8.grid(row=8, column=0)
                ae9 = Entry(add_1, width=40, borderwidth=5)
                ae9.grid(row=9, column=1)
                le9 = Label(add_1, text='Enter marks for EVS:')
                le9.grid(row=9, column=0)
                screen_width = add_1.winfo_width()
                screen_height = add_1.winfo_height()
                print(screen_width)
                print(screen_height)

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

                ab1 = Button(add_1, text='Save', command=Save).grid(row=10, column=1)

            addb1 = Button(addorsee, text='Add new', command=Add)
            addb1.place(x=350,y=110)



            def Average():
                with open("STUDENT.DAT", "rb") as F:
                    c = False
                    while not c:
                        R = pickle.load(F)
                        for i in R:
                            if avg.get() == i[0]:
                                avg1 = (int(i[3]) + int(i[4]) + int(i[5]) + int(i[6]) + int(i[7]) + int(i[8])) / 6
                                mymsg3 = Label(addorsee, text=f"Average of the student is {avg1}")
                                mymsg3.place(x=250,y=260)
                                c = True
                                break
                    if c == False:
                        mymsg4 = Label(addorsee, text='Student not found')
                        mymsg4.place(x=250,y=260)

            mymsg = Label(addorsee, text="Enter SRN to check average of student: ")
            mymsg.place(x=120,y=220)
            avg = Entry(addorsee, width=40)
            avg.place(x=370,y=221)
            mybutton = Button(addorsee, text="Check", command=Average)
            mybutton.place(x=630,y=220)

            def Pass():
                with open("STUDENT.DAT", "rb") as F:
                    c = False
                    while not c:
                        R = pickle.load(F)
                        for i in R:
                            if pas.get() == i[0]:
                                t = 3
                                while t < 9:
                                    if int(i[t]) < 40:
                                        break
                                    else:
                                        t += 1
                                else:
                                    mymsg5 = Label(addorsee, text='Student has passed!')
                                    mymsg5.place(x=250,y=370)
                                    break
                                mymsg3 = Label(addorsee, text='Student has failed!')
                                mymsg3.place(x=250,y=370)
                                c = True
                                break
                    if c == False:
                        mymsg4 = Label(addorsee, text='Student not found')
                        mymsg4.place(x=250,y=370)

            mymsg2 = Label(addorsee, text='Enter SRN to check  if student has passed or failed: ')
            mymsg2.place(x=90,y=330)
            pas = Entry(addorsee, width=40)
            pas.place(x=370,y=331)
            mybutton2 = Button(addorsee, text="Check", command=Pass)
            mybutton2.place(x=630,y=330)

            def Delete():
                with open("STUDENT.DAT", "rb+") as F:
                    c = False
                    try:
                        while not c:
                            R = pickle.load(F)
                            for i in R:
                                if de1.get() == i[0]:
                                    R.remove(i)
                                    mylabe31 = Label(addorsee, text='Student deleted')
                                    mylabe31.place(x=250,y=480)
                                    c = True
                                    break
                    except:
                        mylabel3 = Label(addorsee, text='Student not found')
                        mylabel3.place(x=250,y=480)

            mylabel10 = Label(addorsee, text='Enter SRN of student to be deleted: ')
            mylabel10.place(x=130,y=440)
            del1 = Entry(addorsee, width=40)
            del1.place(x=370, y=441)
            addb2 = Button(addorsee, text='Delete', command=Delete)
            addb2.place(x=630,y=440)
            addorsee.mainloop()


        else:
            mylabel8 = Label(noot, text='Wrong password')
            mylabel8.place(x=280,y=300)

    sb1 = Button(noot, text='Login', command=login)
    sb1.place(x=320, y=200)
    noot.mainloop()


main_page_image = PhotoImage(file="main page.png")
mylabel1 = Label(root, image=main_page_image)
mylabel1.place(x=0, y=0)
button1 = Button(root, text='Teacher', command=Teacher)
button1.place(x=450, y=170)
button2 = Button(root, text='Student', command=Student)
button2.place(x=450, y=210)

root.mainloop()


