import ttkbootstrap as ttk
from tkinter import *
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO
import webbrowser

class UserProfileWindow:
    def __init__(self, username):
        self.data = self.API_request(username)
        if 'message' in self.data and self.data['message'] == 'Not Found':
            error_text = "Github user not found, please check username"
            messagebox.showerror("User Not Found", error_text)
        else:
            self.create_window()

    def API_request(self, username):
        url = f'https://api.github.com/users/{username}'
        res = requests.get(url)
        data = res.json()
        return data

    def getImageLabel(self, url, width, height):
        response = requests.get(url)
        img_data = response.content
        image = Image.open(BytesIO(img_data))
        resized_image = image.resize((width, height), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.BICUBIC)
        tk_image = ImageTk.PhotoImage(resized_image)
        return tk_image
    
    def callback(self, url):
        webbrowser.open_new(url)

    def create_window(self):
        if hasattr(self, 'window') and self.window:
            self.window.destroy()

        self.window = ttk.Toplevel()
        self.window.iconbitmap('public/github.ico')
        self.window.title(f"UserName Card")
        window_width = 600
        window_height = 400
        self.window.configure(bg='#1b1f23')
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        self.window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        
        # Style
        s = ttk.Style()
        s.configure('TFrame', background='#1b1f23')

        TopFrame = ttk.Frame(master=self.window, style='TFrame')
        LeftFrame = ttk.Frame(master=self.window, style='TFrame')
        RightFrame = ttk.Frame(master=self.window, style='TFrame')
        BottomFrame = ttk.Frame(master=self.window, style='TFrame')
        
        userName_label = ttk.Label(master=TopFrame, text=f"UserName: {self.data['login']}", font=("Mona Sans", 25, "bold"), background='#1b1f23', foreground="white", cursor="hand2")
        userLink = self.data['html_url']
        userName_label.bind("<Button-1>", lambda e: self.callback(userLink))
        userName_label.pack()
        
        image_url = self.data['avatar_url']
        image_label = ttk.Label(master=LeftFrame)
        image_label.pack()
        tk_image = self.getImageLabel(image_url, width=100, height=100)
        image_label.configure(image=tk_image)
        image_label.image = tk_image
        userFollowers_label = ttk.Label(master=LeftFrame, text=f"Followers: {self.data['followers']}", font=("Mona Sans", 10, "bold"), background='#1b1f23', foreground="white").pack(fill='x', pady=5)
        userFollowing_label = ttk.Label(master=LeftFrame, text=f"Following: {self.data['following']}", font=("Mona Sans", 10, "bold"), background='#1b1f23', foreground="white").pack(fill='x')
        
        userBio_label = ttk.Label(master=RightFrame, text=f"Bio: {self.data['bio']}", font=("Mona Sans", 15), background='#1b1f23', foreground="white").pack(fill='x')
        userComp_label = ttk.Label(master=RightFrame, text=f"Company: {self.data['company']}", font=("Mona Sans", 15), background='#1b1f23', foreground="white").pack(fill='x')
        userLoc_label = ttk.Label(master=RightFrame, text=f"Location: {self.data['location']}", font=("Mona Sans", 15), background='#1b1f23', foreground="white").pack(fill='x')
        userEmail_label = ttk.Label(master=RightFrame, text=f"Email: {self.data['email']}", font=("Mona Sans", 15), background='#1b1f23', foreground="white").pack(fill='x')
        
        TopFrame.pack(side='top', pady=10)
        LeftFrame.pack(side='left', expand=True, fill='y')
        RightFrame.pack(side='right', expand=True, fill='y')
        BottomFrame.pack(side='bottom', expand=True, fill='x')
        
def UserCard(username):
    UserProfileWindow(username)
