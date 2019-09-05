import tkinter as tk
from tkinter import Canvas

def main():
    marco = tk.Tk()
    marco.title("Polinomio Entero")
    marco.geometry("500x500")
    marco.resizable(0,1)
    marco.configure(background="#000000")
    ln = tk.Label(marco, text ="A continución digíte el grado de la Función",bg="black",fg="yellow").pack(
        padx=3,pady=3,ipadx=2,ipady=20,fill=tk.X)
    cn = tk.Entry(marco, bg="blue",fg="yellow")
    cn.pack()

    def cargarn():

        def cargarv():
            coe = list(range(labeln))
            for i in range(labeln):
                coe[i] = camTex[i].get()

            lx = tk.Label(marco, text="Cargar el número a evaluar la función Función",bg="black",fg="yellow")
            lx.pack()
            lx.place(x=100,y= labeln*h+12*h+75)
            x = tk.Entry(marco,bg="blue",fg="yellow")
            x.pack()
            x.place(x=100,y= labeln*h+12*h+100)

            def evalua():
                r=0
                for i in range(labeln):
                    r = r + (float(x.get())**i) * float(coe[i])
                lr = tk.Label(marco, text="El Resultado de la función evaluada en "+str(x.get())+" es : "+
                                          str(r),bg="black",fg="yellow")
                lr.place(x=100,y= labeln*h+12*h+160)


            cargarx = tk.Button(marco, text="Evaluar",bg="Blue",fg="yellow",command=evalua)
            cargarx.place(x=100,y= labeln*h+12*h+125)

        lcoe = tk.Label(marco, text ="A continución digíte cada coeficiente de las variables",bg="Black",fg="yellow").pack(
            padx=3,pady=3,ipadx=2,ipady=20,fill=tk.X)
        labeln = int(cn.get())
        h = 15
        labelv = list(range(labeln))
        camTex = list(range(labeln))
        r = 0
        for i in range(labeln):
            labelv[i] = tk.Label(marco, text="X:"+str(i),bg="black",fg="red")
            labelv[i].pack()
            labelv[i].place(x=100,y=i*h+12*h)
            camTex[i] = tk.Entry(marco, bg="blue",fg="yellow")
            camTex[i].pack(ipady=30)
            camTex[i].place(x=167 , y= i*h+12*h)
        cargarv = tk.Button(marco, text="Cargar Variables",bg="Blue",fg="yellow",command=cargarv)
        cargarv.pack()
        cargarv.place(x=100,y= labeln*h+12*h+25)


    


    cargarn = tk.Button(marco, text="Cargar El Grado de la Función",bg="Blue",fg="yellow",command=cargarn).pack(pady=5)
    #l2 = tk.Label(marco, text ="p = ",width=20,fg="white").grid(row=1,sticky=tk.W)
    #entrada1 = tk.Entry(marco).grid(row=1,column=0)

    marco.mainloop()

main()
