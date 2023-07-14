
from tkinter import ttk
from tkinter import *  
import ttkbootstrap as ttk
def convercion():
   millas =entryInt.get()
   km=millas*1.61
   
   salidatxt.set(str(km)+' km')

#ventana
ventana = ttk.Window(themename='darkly')

ventana.config()
ventana.title("Millas a KM")
ventana.geometry('300x150')
#title
labeltx=Label(ventana, text="Millas a kilometros", font ='Calobri 24 bold',)
labeltx.pack()
#input field
panel = Frame(ventana)
panel.config(height=200, width=250)
entryInt = IntVar()
entry = Entry(panel, textvariable=entryInt)
entry.grid(column=1, row=1)

button = Button(panel, text="convertir",command= convercion)
button.grid(column=2, row=2)

panel.pack()
global salidatxt
salidatxt= StringVar()

salidatexto = Label(ventana, text='salida', 
                    font='Calobri 14 bold', textvariable=salidatxt)
salidatexto.pack(pady=5)
#correr
ventana.mainloop()