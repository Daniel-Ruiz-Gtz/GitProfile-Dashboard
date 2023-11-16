from card import *
import ttkbootstrap as ttk
from PIL import Image, ImageTk

def sendUsername():
    UserCard(username_entry.get())
    
# main window
root = ttk.Window()
root.iconbitmap('public/github.ico')
root.title('GitProfile Dashboard')
window_width = 600
window_height = 400
root.configure(bg='#1b1f23')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# title
image = Image.open("public/logo.png")
photo = ImageTk.PhotoImage(image)
image_label = ttk.Label(root, image=photo, background='#1b1f23')
image_label.pack(side="top")
title_label = ttk.Label(root, text='GitProfile Dashboard', font=("Mona Sans", 30), foreground="white", background='#1b1f23')
title_label.pack(side="top")

# Style
s = ttk.Style()
s.configure('TFrame', background='#1b1f23')

entry_frame = ttk.Frame(root, style='TFrame')
title_label = ttk.Label(entry_frame, background='#1b1f23', text='Username', font=("Mona Sans", 15), foreground="white")
title_label.pack(side="left")
username_entry= ttk.Entry(entry_frame,background="#FFFFFF", font=("Mona Sans", 12), )
username_entry.pack(side="left", padx=10)
search_button = ttk.Button(entry_frame, text='Search', command=sendUsername)
search_button.pack(side="left")
entry_frame.pack(pady=15)



root.mainloop()