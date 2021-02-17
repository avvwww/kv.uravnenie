from tkinter import *

def text_to_lbl(event):
    text=c.get() #num=int(text),если нужны цифры
   

def lahenda():
    if(a.get()!="" and b.get()!="" and c.get()!=""):
        a_=int(a.get())
        b_=int(b.get())
        c_=int(c.get())
        D=b_*b_-4*a_*c_
        if D>0:
            x1_=round((-1*b_+sqrt(D))/(2*a_),2)
            x2_=round((-1*b_-sqrt(D))/(2*a_),2)
            t=f"X1={x1_}, \nX2={x2_}"
        elif D==0:
            x1_=round((-1*b_)/(2*a_),2)
            t=f"X1={x1_}"
        else:
            t="Корней нет"
        lbl_reshenie.configure(text=f"D={D}\n{t}")
        a.configure(bg="lightblue")
        b.configure(bg="lightblue")
        c.configure(bg="lightblue")
    else:
        if a.get()=="":
            a.configure(bg="red")
        elif b.get()=="":
            b.configure(bg="red")
        elif c.get()=="":
            c.configure(bg="red")



aken=Tk()
aken.title("Решение кв. уравнений") 


lbl_zagolovok=Label(aken,text="Решение кв.уравнений",font="Arial 20",borderwidth=5,height=3,width=30,relief="groove",bg="black",fg="white")
lbl_zagolovok.pack()

a=Entry(aken,width=5,borderwidth=5,font="Arial 20")
a.pack(side=LEFT)
a.bind("<Return>",text_to_lbl) #Enter

a1=Label(aken,text="x**2+",font="Arial 20",borderwidth=5,height=3,width=5,relief="groove")
a1.pack(side=LEFT)

b=Entry(aken,width=5,borderwidth=5,font="Arial 20")
b.pack(side=LEFT)
b.bind("<Return>",text_to_lbl) #Enter

b2=Label(aken,text="x+",font="Arial 20",borderwidth=5,height=3,width=5,relief="groove")
b2.pack(side=LEFT)

c=Entry(aken,width=5,borderwidth=5,font="Arial 20")
c.pack(side=LEFT)
c.bind("<Return>",text_to_lbl) #Enter

d=Label(aken,text="=0",font="Arial 20",borderwidth=5,height=3,width=5,relief="groove")
d.pack(side=LEFT)


btn=Button(aken,text="Решить",font="Arial 20",borderwidth=5,height=3,width=30,relief="groove",bg="green",command=lambda:lahenda())
btn.pack(side=LEFT)

lbl_reshenie=Label(aken,text="Решение",font="Arial 20",borderwidth=5,height=3,width=30,relief="groove",activebackground="green")
lbl_reshenie.pack(side=BOTTOM)

aken.mainloop()