
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
import queue
import config

from supabase import create_client, Client

import cloudinary
import cloudinary.uploader
import cloudinary.api

#Local assets path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame2"

# Supabase connection
url = os.environ.get("SUPABASE_URL")
key= os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

#Get the env of profile pic
config.CLOUDINARY_FOLDER = os.getenv("CLOUDINARY_FOLDER")

def find_rank(parent_id: str):
    q = queue.Queue()
    q.put(parent_id)
    print("Checking: ", parent_id)
    while not q.empty():
        parent_id = q.get()
        result = supabase.table("Parent_Child").select("KidID").eq("ParentID", parent_id).execute()
        if (len(result.data) == 4):
            print("Full")
            for i in range(4):
                q.put(result.data[i].get('KidID'))
        else:
            rank = supabase.table("Distributor").select("Rank").eq("ID", parent_id).execute()
            print("Rank: ", rank.data[0].get('Rank') + 1)
            return (rank.data[0].get('Rank') + 1, parent_id)
        # print(result)
    

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class AddFrame(tk.Frame):
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
            command=self.button_1_clicked,
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
            command=self.button_2_clicked,
            relief="flat"
        )
        self.button_2.place(
            x=609.0,
            y=414.0,
            width=120.0,
            height=32.0
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            669.0,
            318.0,
            image=self.image_image_3
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.button_3_clicked,
            relief="flat"
        )
        self.button_3.place(
            x=12.0,
            y=426.0,
            width=240.0,
            height=40.0
        )
        
        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.button_4_clicked,
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
            381.0,
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
            y=361.0,
            width=368.0,
            height=38.0
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            249.0,
            327.0,
            image=self.image_image_4
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            212.0,
            273.0,
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
            y=253.0,
            width=368.0,
            height=38.0
        )

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        self.image_5 = self.canvas.create_image(
            145.0,
            219.0,
            image=self.image_image_5
        )

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            212.0,
            165.0,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#D7D7D7",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_3.place(
            x=28.0,
            y=145.0,
            width=368.0,
            height=38.0
        )

        self.image_image_6 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        self.image_6 = self.canvas.create_image(
            107.0,
            111.0,
            image=self.image_image_6
        )

    def button_1_clicked(self):
        print("add_to_home clicked")
        self.canvas.place_forget()
        self.button_1.place_forget()
        self.button_2.place_forget()
        self.button_2.place_forget()
        from Home import HomeFrame
        self.master.home_frame = HomeFrame(self.master)
        self.master.home_frame.place(x=0, y=0)

    def button_2_clicked(self):
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
            669.0,
            318.0,
            image=self.image_image_3
            )
    
    def button_3_clicked(self):
        print("submit profile clicked")
        
        #Cloudinary connection
        self.config = cloudinary.config(secure=True)
        
        #Check if all fields are filled
        if (self.entry_3.get()=="" or self.entry_2.get()=="" or self.entry_1.get()==""):
            messagebox.showwarning("Warning", "Please fill all fields!")
            return
        self.pattern = r"^VN-\d{6}$"
        if (re.match(self.pattern, self.entry_3.get())==None):
            messagebox.showwarning("Warning", "Invalid distributor ID! \nID must be in the format of VN-XXXXXX.")
            return
        if (re.match(self.pattern, self.entry_1.get())==None):
            if (self.entry_1.get() == "0"):
                pass
            else:
                messagebox.showwarning("Warning", "Invalid referral ID! \nID must be in the format of VN-XXXXXX.")
                return
        
        #Check if the ID is already in the database
        self.distributor = supabase.table("Distributor").select("ID").eq("ID", self.entry_3.get()).execute()
        if (len(self.distributor.data) > 0):
            messagebox.showwarning("Warning", "Distributor ID already exists!")
            return
        
        #Check if the referral ID is in the database
        self.referral = supabase.table("Distributor").select("*").eq("ID", self.entry_1.get()).execute()
        if (len(self.referral.data) == 0):
            if (self.entry_1.get() != "0"):
                messagebox.showwarning("Warning", "Referral ID does not exist!")
                return
            else:
                pass
        
        #Find rank of this new distributor
        if (self.entry_1.get() == "0"):
            self.rank, self.parent = (1, "0")
        elif (find_rank(self.entry_1.get())==9):
            self.rank, self.parent = (1, "0")
        else:
            self.rank, self.parent = find_rank(self.entry_1.get())

        #Insert data into the database and upload image to Cloudinary
        try:
            #Upload image to Cloudinary
            if not hasattr(self, 'file_path') or not self.file_path:
                self.file_path = "https://res.cloudinary.com/dxb5plez8/image/upload/v1731493751/ProfilePic/default.webp"
                self.check = 1
            else:
                self.result = cloudinary.uploader.upload(self.file_path,
                                                        folder="ProfilePic",
                                                        public_id=self.entry_3.get(),
                                                        format="jpg"
                                                        )
                self.check = 0
            
            #Take the profile link
            if self.check == 1:
                self.link = "https://res.cloudinary.com/dxb5plez8/image/upload/v1731493751/ProfilePic/default.webp"
            else:
                self.link = self.result.get('secure_url')
            
            #Prepare data for insertion into Distributor table
            self.data = {
            "ID": self.entry_3.get(),
            "Name": self.entry_2.get(),
            "Referral_ID": self.entry_1.get(),
            "Rank": self.rank, 
            "ProfilePic": self.link
            }
            
            #Upload to distributor table
            self.result = supabase.table("Distributor").insert(self.data).execute()
            
            #Upload to Parent_Child table
            if (self.entry_1.get() != "0"):
                self.data = {
                    "ParentID": self.parent,
                    "KidID": self.entry_3.get()
                }
                self.result = supabase.table("Parent_Child").insert(self.data).execute()
                # messagebox.showinfo("Success", "Distributor added successfully!")
            
            #Uploaad to Commission table
            self.data = {
                "ID": self.entry_3.get(),
                "Commission": 0
            }
            supabase.table("Distributor_Commission").insert(self.data).execute()
            
        except Exception as e:
            messagebox.showwarning("Warning", "An unexpected error occured:\n\n" + str(e) + '\n\n' + "Your profile has not been added.")
            return
        messagebox.showinfo("Success", "Distributor added successfully!")
        
        #Reset all fields
        self.entry_1.delete(0, 'end')
        self.entry_2.delete(0, 'end')
        self.entry_3.delete(0, 'end')
        self.canvas.delete(self.image_3)
        self.file_path = ""
        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            669.0,
            318.0,
            image=self.image_image_3
        )
    
    def button_4_clicked(self):
        print("add_to_search clicked")
        self.canvas.place_forget()
        self.button_1.place_forget()
        self.button_2.place_forget()
        self.button_3.place_forget()
        self.button_4.place_forget()
        from DistributorSearch import SearchFrame
        self.master.search_frame = SearchFrame(self.master)
        self.master.search_frame.place(x=0,y=0)