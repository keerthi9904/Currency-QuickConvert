import tkinter as tk
top = tk.Tk()
top.title("Currency Converter")
top.resizable(height=False,width=False)
top.rowconfigure((0,1,2,3,4,5),weight=1)
top.columnconfigure((0,1,2),weight=1)
root=tk.Frame(top)
root.grid(sticky='NEWS')
def onclick():
    global e1
    exchange_rate=exchange.get()
    inr=float(e1.get())
    try:
        calc=inr/exchange_rate
        result=round(calc,2)   
    except:
        result="Error"
    finally:
        l4.config(text=f"{result}")

l1=tk.Label(root,text="Enter amount(INR): ",font=("Arial", 15))
l1.grid(row=0,column=0,columnspan=2,sticky='W',padx=5)
e1=tk.Entry(root,width=10,bg="white",font=("Arial", 15))
e1.grid(row=1,column=2,padx=10)
l2=tk.Label(root,text="Convert to: ",font=("Arial", 15))
l2.grid(row=2,column=0,sticky='W',padx=5)

exchange=tk.DoubleVar()

r1 = tk.Radiobutton(root, text="USD", variable=exchange, value=83.16)
r1.grid(row=3,column=0,sticky='W',padx=5)
r2 = tk.Radiobutton(root, text="POUNDS", variable=exchange, value=102.91)
r2.grid(row=4,column=0,sticky='W',padx=5)
r3 = tk.Radiobutton(root, text="AED", variable=exchange, value=22.68)
r3.grid(row=5,column=0,sticky='W',padx=5)
btn=tk.Button(root,text="Calculate",bg="yellow",command=onclick,font=("Arial", 15))
btn.grid(row=6,column=1,pady=10)

l3=tk.Label(root,text="Converted amount: ",font=("Arial", 15))
l3.grid(row=3,column=1,columnspan=2)
l4=tk.Label(root,bg="white",width=10,font=("Arial", 15))
l4.grid(row=4,column=2)

top.mainloop()