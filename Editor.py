from tkinter import *
from PIL import ImageTk, Image, ImageOps
from tkinter import filedialog
import os
import tkinter as tk


start_engine = Tk()
root = Toplevel(start_engine)
start_engine.withdraw()


def openfile():
    filename = filedialog.askopenfilename(title='Choose the file')
    return filename


def setup_main():
    o = openfile()
    img = Image.open(o)
    main = Toplevel(start_engine)
    root.destroy()
    width = 50
    height = 50
    photoImg = ImageTk.PhotoImage(img)
    canvas = Canvas(main, width=700, height=300, bg="blue")
    canvas.place(x=100, y=100)
    canvas.create_image(0, 0, image=photoImg, anchor=NW)
    Label(main, text="Rotation degree").place(x=10, y=500)
    e1 = Entry(main).place(x=100, y=500)


def rotate(image_path, degree):
    image_obj = Image.open(image_path)
    rotated_image = image_obj.rotate(degree)
    rotated_image.show()


def crop(left, up, right, bottom):
    border = (left, up, right, bottom)  # left, up, right, bottom
    ImageOps.crop(img, border)


tk.Label(root, text="Made by Thakur Saab", fg="red", font="Times").pack()
logo = tk.PhotoImage(file="logo.png")
w = tk.Label(root, compound=tk.CENTER, image=logo).pack()
b = Button(root, text='Upload image', command=setup_main).pack()
