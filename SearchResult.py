# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from dotenv import load_dotenv
load_dotenv()
import config

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import tkinter as tk
import os
import re
import queue
import requests 
from io import BytesIO

from supabase import create_client, Client

import cloudinary
import cloudinary.uploader
import cloudinary.api

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = ASSETS_PATH = OUTPUT_PATH / "assets" / "frame6"

config.CLOUDINARY_FOLDER = os.getenv("CLOUDINARY_FOLDER", "https://res.cloudinary.com/dxb5plez8/image/upload/v1731812075/ProfilePic/")

def format_date(date):
    # Chuyển đổi ngày tháng từ yyyy-mm-ddThh:mm:ss thành dd/mm/yyyy
    date = date.split("T")[0]
    date = date.split("-")
    date = date[2] + "/" + date[1] + "/" + date[0]
    return date

def check_url_exists(url):
    try:
        # Gửi yêu cầu HEAD để kiểm tra tồn tại của URL
        response = requests.head(url, allow_redirects=True, timeout=5)
        
        # Kiểm tra mã trạng thái HTTP
        if 200 <= response.status_code < 300:
            return True  # URL tồn tại
        else:
            return False  # URL không tồn tại hoặc không hợp lệ

    except requests.RequestException as e:
        # Lỗi mạng hoặc URL không hợp lệ
        print(f"Lỗi: {e}")
        return False 
    
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class ResultFrame(tk.Frame):
    def __init__ (self, master): 
        print(config.SEARCH_RESULT)
        
        #Some basic settings
        self.master = master
        super().__init__(master)
        self.current_index = 1
        
        self.canvas = Canvas(
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
            40.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            400.0,
            289.0,
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
            x=264.0,
            y=437.0,
            width=80.0,
            height=40.0
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
            x=456.0,
            y=437.0,
            width=80.0,
            height=40.0
        )

        self.text_1 = self.canvas.create_text(
            387.0,
            448.0,
            anchor="nw",
            text= str(self.current_index) + " / " + str(len(config.SEARCH_RESULT.data)),
            fill="#000000",
            font=("Arial", 15 * -1, "bold")
        )

        #Format the date from Supabase to dd/mm/yyy, currently it is in yyyy-mm-ddThh:mm:ss
        date = format_date(config.SEARCH_RESULT.data[self.current_index-1]["created_at"])
        self.text_2 = self.canvas.create_text(
            264.0,
            384.0,
            anchor="nw",
            text="Date of employment:   " + date,
            fill="#000000",
            font=("Arial", 15 * -1, "bold")
        )

        self.text_3 = self.canvas.create_text(
            265.0,
            334.0,
            anchor="nw",
            text="ID:   " + config.SEARCH_RESULT.data[self.current_index-1]["ID"],
            fill="#000000",
            font=("Arial", 15 * -1, "bold")
        )

        self.text_4 = self.canvas.create_text(
            265.0,
            284.0,
            anchor="nw",
            text="Name:   " + config.SEARCH_RESULT.data[self.current_index-1]["Name"],
            fill="#000000",
            font=("Arial", 15 * -1, "bold")
        )

        # Get the profile pic from the Cloudinary server
        print(config.SEARCH_RESULT.data[self.current_index-1]["ID"])
        url = config.SEARCH_RESULT.data[self.current_index-1]["ProfilePic"]
        if (check_url_exists(url) == False):
            url = config.CLOUDINARY_FOLDER + "default.webp"
        try:
            response = requests.get(url)
            response.raise_for_status()
        except Exception as e:
            messagebox.showerror("Error", "Error while fetching image from the server!\n" + str(e)) 
            return
        
        #Convert image data to PIL image
        img_data = BytesIO(response.content)
        self.image_image_3 = Image.open(img_data)
        self.image_image_3 = self.image_image_3.resize((160, 160))
        self.image_image_3 = ImageTk.PhotoImage(self.image_image_3)
        self.image_3 = self.canvas.create_image(
            400.0,
            189.0,
            image=self.image_image_3
        )
        img_data.close()
        
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
            x=0.0,
            y=0.0,
            width=160.0,
            height=79.0
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
            height=79.0
        )

    def button_1_pressed(self):
        print("prev button pressed")
        self.current_index -= 1
        if (self.current_index < 1):
            self.current_index = len(config.SEARCH_RESULT.data)
        
        #Update the text
        self.canvas.itemconfig(self.text_1, text=str(self.current_index) + " / " + str(len(config.SEARCH_RESULT.data)))
        date = format_date(config.SEARCH_RESULT.data[self.current_index-1]["created_at"])
        self.canvas.itemconfig(self.text_2, text="Date of employment:   " + date)
        self.canvas.itemconfig(self.text_3, text="ID:   " + config.SEARCH_RESULT.data[self.current_index-1]["ID"])
        self.canvas.itemconfig(self.text_4, text="Name:   " + config.SEARCH_RESULT.data[self.current_index-1]["Name"])
        
        # Get the profile pic from the Cloudinary server
        print(config.SEARCH_RESULT.data[self.current_index-1]["ID"])
        url = config.SEARCH_RESULT.data[self.current_index-1]["ProfilePic"]
        if (check_url_exists(url) == False):
            url = config.CLOUDINARY_FOLDER + "default.webp"
        try:
            response = requests.get(url)
            response.raise_for_status()
        except Exception as e:
            messagebox.showerror("Error", "Error while fetching image from the server!\n" + str(e)) 
            return
        
        #Convert image data to PIL image
        img_data = BytesIO(response.content)
        self.image_image_3 = Image.open(img_data)
        self.image_image_3 = self.image_image_3.resize((160, 160))
        self.image_image_3 = ImageTk.PhotoImage(self.image_image_3)
        self.canvas.itemconfig(self.image_3, image=self.image_image_3)
        img_data.close()
    
    def button_2_pressed(self):
        print("next button pressed")
        self.current_index += 1
        if (self.current_index > len(config.SEARCH_RESULT.data)):
            self.current_index = 1
        
        #Update the text
        self.canvas.itemconfig(self.text_1, text=str(self.current_index) + " / " + str(len(config.SEARCH_RESULT.data)))
        date = format_date(config.SEARCH_RESULT.data[self.current_index-1]["created_at"])
        self.canvas.itemconfig(self.text_2, text="Date of employment:   " + date)
        self.canvas.itemconfig(self.text_3, text="ID:   " + config.SEARCH_RESULT.data[self.current_index-1]["ID"])
        self.canvas.itemconfig(self.text_4, text="Name:   " + config.SEARCH_RESULT.data[self.current_index-1]["Name"])
        
        # Get the profile pic from the Cloudinary server
        print(config.SEARCH_RESULT.data[self.current_index-1]["ID"])
        url = config.SEARCH_RESULT.data[self.current_index-1]["ProfilePic"]
        if (check_url_exists(url) == False):
            url = config.CLOUDINARY_FOLDER + "default.webp"
        try:
            response = requests.get(url)
            response.raise_for_status()
        except Exception as e:
            messagebox.showerror("Error", "Error while fetching image from the server!\n" + str(e)) 
            return
        
        #Convert image data to PIL image
        img_data = BytesIO(response.content)
        self.image_image_3 = Image.open(img_data)
        self.image_image_3 = self.image_image_3.resize((160, 160))
        self.image_image_3 = ImageTk.PhotoImage(self.image_image_3)
        self.canvas.itemconfig(self.image_3, image=self.image_image_3)
        img_data.close()
    
    def button_3_pressed(self):
        print("result to home pressed")
        #Return to HomeFrame
        self.canvas.place_forget()
        self.button_1.place_forget()
        self.button_2.place_forget()
        self.button_3.place_forget()
        self.button_4.place_forget()
        from Home import HomeFrame
        self.master.home_frame = HomeFrame(self.master)
        self.master.home_frame.place(x=0, y=0)
    
    def button_4_pressed(self):
        print("result to search pressed")
        #Return to SearchFrame
        self.canvas.place_forget()
        self.button_1.place_forget()
        self.button_2.place_forget()
        self.button_3.place_forget()
        self.button_4.place_forget()
        from DistributorSearch import SearchFrame
        self.master.search_frame = SearchFrame(self.master)
        self.master.search_frame.place(x=0, y=0)
        
        
        