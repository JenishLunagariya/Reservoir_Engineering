from tkinter import *
from tkinter.messagebox import *
root=Tk()
root.geometry("550x400")
root.title('Petroleum Units Converter')

def FT3_TO_BBL():
    new_window=Toplevel()
    new_window.geometry("200x200")
    new_window.title('ft3 to bbl')
    number=num1value.get()
    Label(new_window,text=f'Answer:{round(number*0.18,4)} bbl').pack()
    Button(new_window,text='close',command=lambda :new_window.destroy()).pack()

def Calcius_To_Fahrenheit():
    new_window=Toplevel()
    new_window.geometry("200x200")
    new_window.title('C to F')
    number=num1value.get()
    Label(new_window,text=f'Answer:{round((number*9/5)+32,2)} Fahrenheit').pack()
    Button(new_window,text='close',command=lambda :new_window.destroy()).pack()

def Fahrenheit_To_Calcius():
    new_window=Toplevel()
    new_window.geometry("200x200")
    new_window.title('F to C')
    number=num1value.get()
    Label(new_window,text=f'Answer:{round((number-32)*5/9,2)} Calcius').pack()
    Button(new_window,text='close',command=lambda :new_window.destroy()).pack()

def INCH3_TO_BBL():
    new_window=Toplevel()
    new_window.geometry("200x200")
    new_window.title('inch3 to bbl')
    number=num1value.get()
    Label(new_window,text=f'Answer:{round(number/9702,4)} bbl').pack()
    Button(new_window,text='close',command=lambda :new_window.destroy()).pack()

def ATM_TO_PSI():
    new_window=Toplevel()
    new_window.geometry("200x200")
    new_window.title('atm to psi')
    number=num1value.get()
    Label(new_window,text=f'Answer:{round(number*14.6959,4)} psi').pack()
    Button(new_window,text='close',command=lambda :new_window.destroy()).pack()

def PSI_TO_ATM():
    new_window=Toplevel()
    new_window.geometry("200x200")
    new_window.title('psi to atm')
    number=num1value.get()
    Label(new_window,text=f'Answer:{round(number/14.6959,4)} atm').pack()
    Button(new_window,text='close',command=lambda :new_window.destroy()).pack()

def PSI_TO_PASCAL():
    new_window=Toplevel()
    new_window.geometry("200x200")
    new_window.title('psi to pascal')
    number=num1value.get()
    Label(new_window,text=f'Answer:{round(number*6894.757,4)} pascal').pack()
    Button(new_window,text='close',command=lambda :new_window.destroy()).pack()

def FT_TO_METER():
    new_window=Toplevel()
    new_window.geometry("200x200")
    new_window.title('ft to meter')
    number=num1value.get()
    Label(new_window,text=f'Answer:{round(number*0.3048,4)} meter').pack()
    Button(new_window,text='close',command=lambda :new_window.destroy()).pack()


def selection():
    try:
        selected=lb.get(lb.curselection())
        if selected=='ft to meter':
            ans=FT_TO_METER()
        elif selected=='ft3 to bbl':
            ans=FT3_TO_BBL()
        elif selected=='C to F':
            ans=Calcius_To_Fahrenheit()
        elif selected=='F to C':
            ans=Fahrenheit_To_Calcius()
        elif selected=='inch3 to bbl':
            ans=INCH3_TO_BBL()
        elif selected=='atm. to psi':
            ans=ATM_TO_PSI()
        elif selected=='psi to atm.':
            ans=PSI_TO_ATM()
        elif selected=='psi to pascal':
            ans=PSI_TO_PASCAL()
    except:
        print(showerror('showerror','Selction Error'))
    return ans

Label(root,text='Petro Units Converter ',font="Arial 20 bold",padx=50,pady=15).grid(row=0,column=1)
num1=Label(root,text='Input value:',font='Arial 14')

num1.grid(row=1,column=0)

num1value=IntVar()

Entry(root,textvariable=num1value).grid(row=1,column=1)


var2=StringVar()
lb=Listbox(root,listvariable=var2)
lb.insert(1,'ft to meter')
lb.insert(2,'ft3 to bbl')
lb.insert(3,'C to F')
lb.insert(4,'F to C')
lb.insert(5,'inch3 to bbl')
lb.insert(6,'atm. to psi')
lb.insert(7,'psi to atm.')
lb.insert(8,'psi to pascal')
lb.grid(row=3,column=1)

btn=Button(root,text='Answer',command=selection)
btn.grid(row=4,column=1)

root.mainloop()