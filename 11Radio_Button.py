import tkinter as tk
win = tk.Tk()
win.geometry("500x500+50+50")

def selection():
    if (radio.get()==1):
       selection = "You selected the option Android"
    elif(radio.get()==2):
        selection = "You selected the option Advanced Python"
    else:
        selection = "You selected the option SQL Server" 
    label.config(text = selection) 
radio = tk.IntVar()
R1 = tk.Radiobutton(win, text="Android", variable=radio, value=1, command=selection)  
R1.place(x=50,y=100) 
R2 = tk.Radiobutton(win, text="Advanced Python", variable=radio, value=2, command=selection)  
R2.place(x=50,y=150)  
R3 = tk.Radiobutton(win, text="SQL Server", variable=radio, value=3, command=selection)  
R3.place(x=50,y=200)  
label = tk.Label(win)  
label.pack() 
win.mainloop()