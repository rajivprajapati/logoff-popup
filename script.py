import time
import tkinter as tk
from turtle import width
from PIL import Image, ImageTk
import os

root = tk.Tk()
root.attributes('-fullscreen', True)
root.title('cool')

label = tk.Label(root, text = "TIME TO LOG-OFF", font=('Arial', 36))
label.place(relx=0.5, rely=0.3, anchor='center')


fl = Image.open('download.jpg')
img = ImageTk.PhotoImage(fl, width= 450)
label = tk.Label(image=img)
label.place(relx=0.5, rely=0.5, anchor='center')
# label.pack()
tw = 10*60
label_time = tk.Label(text = '10:00', font=('Arial', 48))
label_time.place(relx=0.5, rely=0.9, anchor='center')
while tw:
    m, s = divmod(tw, 60)
    if len(str(s))<=1:
        s = f"0{s}"
    if len(str(m))<=1:
        m = f"0{m}"
    label_time.configure(text=f'{m}:{s}')
    label_time.update()
    time.sleep(1)
    tw = tw-1
os.system('shutdown /a')
os.system('shutdown /s /t 0')
root.mainloop()
