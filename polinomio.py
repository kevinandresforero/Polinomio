import tkinter as tk
from tkinter import Canvas

marco = tk.Tk()
marco.title("Solucion de Polinomio")
marco.geometry("1000x500")

l1 = tk.Label(marco, text ="A continución digíte el grado de la ecuación",bg="black",fg="white").pack(padx=3,pady=3,ipadx=2,ipady=20,fill=tk.X)
#l2 = tk.Label(marco, text ="p = ",width=20,fg="white").grid(row=1,sticky=tk.W)
#entrada1 = tk.Entry(marco).grid(row=1,column=0)


marco.mainloop()
