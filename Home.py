
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = ASSETS_PATH = OUTPUT_PATH / "assets" / "frame4"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class HomeFrame(tk.Frame):
    def __init__(self,master):
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
        self.canvas.create_rectangle(
            0.0,
            3.0,
            800.0,
            87.0,
            fill="#001D75",
            outline="")

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            399.0,
            38.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            400.0,
            289.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            337.0,
            113.0,
            image=self.image_image_3
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
            x=46.000030517578125,
            y=413.9996337890625,
            width=720.0,
            height=52.0
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
            x=46.0,
            y=324.0,
            width=720.0,
            height=52.0
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
            x=46.0,
            y=233.92857360839844,
            width=720.0,
            height=52.0
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
            x=45.0,
            y=144.0,
            width=720.0,
            height=52.0
        )
        
        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.button_5_pressed,
            relief="flat"
        )
        self.button_5.place(
            x=632.0,
            y=3.0,
            width=168.0,
            height=76.0
        )
        
        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            81.0,
            38.0,
            image=self.image_image_4
        )
    
    def button_5_pressed(self):
        print("home_to_search clicked")
        self.canvas.place_forget()
        self.button_1.place_forget()
        self.button_2.place_forget()
        self.button_3.place_forget()
        self.button_4.place_forget()
        from DistributorSearch import SearchFrame
        self.master.search_frame = SearchFrame(self.master)
        self.master.search_frame.place(x=0,y=0)
    
    def button_4_pressed(self):
        print("home_to_add clicked")
        self.canvas.place_forget()
        self.button_1.place_forget()
        self.button_2.place_forget()
        self.button_3.place_forget()
        self.button_4.place_forget()
        from AddDistributor import AddFrame
        self.master.add_frame = AddFrame(self.master)
        self.master.add_frame.place(x=0,y=0)
        
    def button_3_pressed(self):
        print("home_to_delete clicked")
        self.canvas.place_forget()
        self.button_1.place_forget()
        self.button_2.place_forget()
        self.button_3.place_forget()
        self.button_4.place_forget()
        from DeleteDistributor import DeleteFrame
        self.master.delete_frame = DeleteFrame(self.master)
        self.master.delete_frame.place(x=0,y=0)

    def button_2_pressed(self):
        print("home_to_comission clicked")
        self.canvas.place_forget()
        self.button_1.place_forget()
        self.button_2.place_forget()
        self.button_3.place_forget()
        self.button_4.place_forget()
        from ComissionCalculator import CalculatorFrame
        self.master.comission_frame = CalculatorFrame(self.master)
        self.master.comission_frame.place(x=0,y=0)
        
    def button_1_pressed(self):
        print("home_to_ChangePF clicked")
        self.canvas.place_forget()
        self.button_1.place_forget()
        self.button_2.place_forget()
        self.button_3.place_forget()
        self.button_4.place_forget()
        from ChangeProfile import ChangeFrame
        self.master.change_frame = ChangeFrame(self.master)
        self.master.change_frame.place(x=0,y=0)
    
    