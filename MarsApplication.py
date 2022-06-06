from Mars import run_thread
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import webbrowser

root = Tk()
root.title("M.A.R.S Assistant")
root.iconbitmap('./extras/icon.ico')
root.eval("tk::PlaceWindow . center")
# root.geometry("720x400")
root.resizable(False, False)

def start_mars():
    run_thread(True)
    run_btn.config(state="disabled")
    refresh_btn.config(state='normal')


def refresh():
    # messagebox.showwarning("Warning", 'Before you start MARS assistant again you should close it by saying "exit"')
    confirm = messagebox.askyesno("Confirm", 'Did you exit MARS assistant by saying "exit"?')
    if(confirm):
        run_btn.config(state="normal")
        refresh_btn.config(state="disabled")

def open_mars_web():
    webbrowser.open_new_tab('http://localhost:1234')


label_frame = Frame(root)
label_frame.pack(fill='x')

icon = ImageTk.PhotoImage(Image.open('./extras/logo.png'))
Label(label_frame, image=icon, height=90).grid(row=0, column=0, padx=(145, 0))

Label(label_frame, text='Welcome to M.A.R.S Assistant', font=("Arial", 14, "bold")).grid(row=0, column=1)


frame = Frame(root, pady=20)
frame.pack(fill="x")

run_btn = Button(frame, text="Start", font=("Courier", 14, "bold"), pady=15, fg='white', bg='#2F85EA', command=start_mars)
run_btn.pack(fill="x")

refresh_btn = Button(frame, text="Refresh", font=("Courier", 14, "bold"), pady=15, fg='black', bg='#C2CCD9', command=refresh)
refresh_btn.pack(fill="x")
refresh_btn.config(state="disabled")

learn_btn = Button(frame, text="Learn More", font=("Courier", 10, "bold"), pady=13, bg="#C6E0FF", command=open_mars_web).pack(fill="x")

# log_btn = Button(frame, text="View Log", font=("Courier", 10, "bold"), pady=13, bg="#C6E0FF", command=view_log_wd)
# log_btn.pack(fill="x")


Label(frame, text='Once M.A.R.S Assistant is running, to exit the virtual assistant just say "exit" \n and she will respond to you by saying "byebye"', font=("Arial", 12)).pack(pady=5)


root.mainloop()
