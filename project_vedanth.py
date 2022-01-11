from tkinter import *
import pickle
root=Tk()
def Student():
    root.destroy()
    loot=Tk()
    tlabel=Label(loot,text='Welcome to Student login page')
    tlabel.config(font=('Helvetica bold',40))
    tlabel.pack()
    te1=Entry(loot,width=50,borderwidth=1)
    te1.insert(0,'Enter SRN: ')
    te1.pack()
    def Sview():
        with open('STUDENT.DAT','rb') as F:
              R=pickle.load(F)
              for i in R:
                    if te1.get()==i[0]:
                        loot.destroy()
                        t_1=Tk()
                        mylabel31=Label(t_1,text=i)
                        mylabel31.pack()
            
                    else:
                        mylabel3=Label(loot,text='Student not found')
                        mylabel3.pack()
        
    tb1=Button(loot,text='Login',command=Sview)
    tb1.pack()
    loot.mainloop()
def Teacher():
    root.destroy()
    noot=Tk()
    slabel=Label(noot,text='Welcome to Teachers login page')
    slabel.config(font=('Helvetica bold',40))
    slabel.pack()
    se1=Entry(noot,width=50,borderwidth=1)
    se1.insert(0,'Enter password: ')
    se1.pack()
    def login():
        if se1.get()=='admin123':
            noot.destroy()
            addorsee=Tk()
            mylabel12=Label(addorsee,text='Would you like to add students or edit existing ones')
            mylabel12.pack()
            def Add():
                add_1=Tk()
                mylabel2=Label(add_1,text='Create new Student')
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
                ae4.insert(0,'Enter marks for Physics: ')
                ae4.pack()
                ae5=Entry(add_1,width=40,borderwidth=5)
                ae5.insert(0,'Enter marks for Maths: ')
                ae5.pack()
                ae6=Entry(add_1,width=40,borderwidth=5)
                ae6.insert(0,'Enter marks for Computers: ')
                ae6.pack()
                ae7=Entry(add_1,width=40,borderwidth=5)
                ae7.insert(0,'Enter marks for Electrical: ')
                ae7.pack()
                ae8=Entry(add_1,width=40,borderwidth=5)
                ae8.insert(0,'Enter marks for Mechanical: ')
                ae8.pack()
                ae9=Entry(add_1,width=40,borderwidth=5)
                ae9.insert(0,'Enter marks for EVS: ')
                ae9.pack()
                def Save():
                        srn=ae1.get()
                        name=ae2.get()
                        sem=ae3.get()
                        marksp=ae4.get()
                        marksm=ae5.get()
                        marksc=ae6.get()
                        markse=ae7.get()
                        marksme=ae8.get()
                        marksev=ae9.get()
                        if srn.isalnum() and name.isalpha() and sem.isdigit() and marksp.isdigit() and marksm.isdigit() and marksme.isdigit() and marksc.isdigit() and markse.isdigit() and marksev.isdigit():
                              with open("STUDENT.DAT","ab") as F:
                                    R=[]
                                    R.append([srn,name,sem,marksp,marksm,marksc,markse,marksme,marksev])
                                
                                    pickle.dump(R,F)
                              add_1.destroy()
                          

                        else:
                            mylabel9=Label(add_1,text='Wrong entries')
                            mylabel9.pack()
                ab1=Button(add_1,text='Save',command=Save)
                ab1.pack()
            addb1=Button(addorsee,text='Add new',command=Add)
            addb1.pack()
            def Delete():
                  with open ('STUDENT.DAT','rb+') as F:
                        R=pickle.load(F)
                        for i in R:
                              if de1.get()==i[0]:
                                    mylabel45=Label(addorsee,text=i[1]+'is about to be deleted')
                                    mylabel45.pack()
                                    del i
                              else:
                                    mylabel46=Label(addorsee,text='Student not found')
                                    mylabel46.pack()
                                    
            mylabel10=Label(addorsee,text='For deleting students:')
            mylabel10.pack()
            de1=Entry(addorsee,width=40)
            de1.pack()
            de1.insert(0,'Enter SRN of student to be deleted: ')           
            addb2=Button(addorsee,text='Delete',command=Delete)
            addb2.pack()





        else:
            mylabel8=Label(noot,text='Wrong password')
            mylabel8.pack()
        
    sb1=Button(noot,text='Login',command=login)
    sb1.pack()
    noot.mainloop()


mylabel1=Label(root,text='Welcome to Info')
mylabel1.pack()
button1=Button(root,text='Teacher',command=Teacher)
button1.pack()
button2=Button(root,text='Student',command=Student)
button2.pack()









                
                mylabel4=Label(add_1,text='Wrong entries')
                mylabel4.pack()
        ba1=Button(add_1,text='Save',command=Save)
        ba1.pack()
        add_1.mainloop()
        '''
