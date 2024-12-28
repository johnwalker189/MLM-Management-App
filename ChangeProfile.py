
from dotenv import load_dotenv
load_dotenv()

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import tkinter as tk
import os
import re
import config

from supabase import create_client, Client

import cloudinary
import cloudinary.uploader
import cloudinary.api

#Local assets path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame3"

config.CLOUDINARY_FOLDER = os.getenv("CLOUDINARY_FOLDER")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class ChangeFrame(tk.Frame):
    def __init__ (self, master):
        #Some basic settings
        self.master = master
        super().__init__(master)
        self.canvas = Canvas(
            self.master,
            bg = "#FFFFFF",
            height = 500,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            400.0,
            250.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            400.0,
            42.0,
            image=self.image_image_2
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.button_1_pressed,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=160.0,
            height=84.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.button_2_pressed,
            relief="flat"
        )
        self.button_2.place(
            x=602.0,
            y=360.0,
            width=120.0,
            height=32.0
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            662.0,
            254.0,
            image=self.image_image_3
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.button_3_pressed,
            relief="flat"
        )
        self.button_3.place(
            x=296.0,
            y=444.0,
            width=240.0,
            height=40.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.button_4_pressed,
            relief="flat"
        )
        self.button_4.place(
            x=632.0,
            y=0.0,
            width=168.0,
            height=84.0
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            212.0,
            357.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#D7D7D7",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=28.0,
            y=337.0,
            width=368.0,
            height=38.0
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        self.image_4 = self.canvas.create_image(
            127.0,
            293.0,
            image=self.image_image_4
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            212.0,
            229.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#D7D7D7",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=28.0,
            y=209.0,
            width=368.0,
            height=38.0
        )

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        self.image_5 = self.canvas.create_image(
            87.0,
            165.0,
            image=self.image_image_5
        )

    def button_1_pressed(self):
        print("ChangePF_to_home clicked")
        self.canvas.place_forget()
        self.button_1.place_forget()
        self.button_2.place_forget()
        from Home import HomeFrame
        self.master.home_frame = HomeFrame(self.master)
        self.master.home_frame.place(x=0, y=0)

    def button_2_pressed(self):
        print("upload_image clicked")
        self.file_path = filedialog.askopenfilename(title="Select a file",
                                               filetypes=[("Image files", "*.png *.jpg"),
                                                          ]
                                               )
        if not self.file_path:
            messagebox.showwarning("Warning", "No file selected!")
        else:
            self.image_image_3 = Image.open(self.file_path)
            self.image_image_3 = self.image_image_3.resize((160, 160))
            self.image_image_3 = ImageTk.PhotoImage(self.image_image_3)
            self.image_3 = self.canvas.create_image(
            662.0,
            254.0,
            image=self.image_image_3
            )

    def button_3_pressed(self):
        print("change profile clicked")
        #Supabase connection
        self.url = os.environ.get("SUPABASE_URL")
        self.key = os.environ.get("SUPABASE_KEY")
        self.supabase = create_client(self.url, self.key)
        
        #Cloudinary connection
        self.config = cloudinary.config(secure=True)
        
        #Check if the user has enter the ID
        if (self.entry_2.get() == ""):
            messagebox.showwarning("Warning", "Please enter the ID!")
            return
            
        #Check if the user has enter the right ID
        self.pattern = r"^VN-\d{6}$"
        if (re.match(self.pattern, self.entry_2.get())==None):
            messagebox.showwarning("Warning", "Invalid distributor ID!")
            return
            
        #Check if the ID exists in the database
        self.distributor = self.supabase.table("Distributor").select("ID").eq("ID", self.entry_2.get()).execute()
        if (len(self.distributor.data) == 0):
            messagebox.showwarning("Warning", "Distributor ID does not exists!")
            return
            
        #Change the name if the user has entered the name
        if (self.entry_1.get() != ""):
            self.supabase.table("Distributor").update({"Name": self.entry_1.get()}).eq("ID", self.entry_2.get()).execute()
        try:
            #Change image
            if not hasattr(self, 'file_path') or not self.file_path:
                self.file_path = "https://res.cloudinary.com/dxb5plez8/image/upload/v1731493751/ProfilePic/default.webp"
                self.check = 1
            else:
                self.result = cloudinary.uploader.upload(self.file_path,
                                                        folder="ProfilePic",
                                                        public_id=self.entry_2.get(),
                                                        format="jpg"
                                                        )
                self.check = 0
            
            #Update the image link in the database
            if self.check == 1:
                self.link = "https://res.cloudinary.com/dxb5plez8/image/upload/v1731493751/ProfilePic/default.webp"
            else:
                self.link = self.result.get('secure_url')
            self.supabase.table("Distributor").update({"ProfilePic": self.link}).eq("ID", self.entry_2.get()).execute()
            messagebox.showinfo("Success", "Changes applied successfully!")
        except Exception as e:
            messagebox.showwarning("Warning", "An unexpected error occured:\n\n" + str(e) + '\n\n' + "Your changes have not been updated.")
            return
        
        #Reset all the fields
        self.entry_1.delete(0, 'end')
        self.entry_2.delete(0, 'end')    
        self.canvas.itemconfig(self.image_3, image=self.image_image_3)
        self.canvas.delete(self.image_3)
        self.file_path = ""
        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            662.0,
            254.0,
            image=self.image_image_3
        )
        
    def button_4_pressed(self):
        print("changePF_to_search clicked")
        self.canvas.place_forget()
        self.button_1.place_forget()
        self.button_2.place_forget()
        self.button_3.place_forget()
        self.button_4.place_forget()
        from DistributorSearch import SearchFrame
        self.master.search_frame = SearchFrame(self.master)
        self.master.search_frame.place(x=0, y=0)
        