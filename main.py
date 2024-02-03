import tkinter as tk

def command_bt1():
    print("button 1 was clicked")



def command_bt2():
    print("button 2 was clicked")


def command_bt3():
    print("button 3 was clicked")        


def command_bt4():
    print("button 4 was clicked")
root = tk.Tk()


root.title("Hello World!")
root.geometry("500x500+500+500")
root.wm_resizable(width=False, height=False)
root.configure(bg="#118568")

button_1 = tk.Button(root,text="Azul",command=command_bt1 ,font="time 20 bold")
button_1.place(width=150, height=50, x=100, y=50)

button_2 = tk.Button(root,text="Vermelho",command=command_bt2 , font="time 20 bold")
button_2.place(width=150, height=50, x=300, y=50)

button_3 = tk.Button(root,text="Verde",command=command_bt3 ,font="time 20 bold")
button_3.place(width=150, height=50, x=100, y=200)

button_4 = tk.Button(root,text="Preto",command=command_bt4 ,font="time 20 bold")
button_4.place(width=150, height=50, x=300, y=200)

root.mainloop()
