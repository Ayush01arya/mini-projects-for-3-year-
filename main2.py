from tkinter import *
from tkinter.font import Font
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import os
from tkinter import ttk
from PIL import Image,ImageTk
root=Tk()
root.geometry("700x670")
root.configure(bg="white")
root.resizable(0,0)
root.title("Image Editior")
photo=PhotoImage(file="ui.png")
root.iconphoto(False,photo)
img134 = ImageTk.PhotoImage(Image.open("2496846.png"))
Label(root,image=img134,relief=FLAT,border=0).place(x=185,y=20)

# create functions
def selected():
    global img_path, img
    img_path = filedialog.askopenfilename(initialdir=os.getcwd())
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    # imgg = img.filter(ImageFilter.BoxBlur(0))
    img1 = ImageTk.PhotoImage(img)
    canvas2.create_image(300, 140, image=img1)
    canvas2.image = img1


def blur(event):
    global img_path, img1, imgg
    for m in range(0, v1.get() + 1):
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        imgg = img.filter(ImageFilter.BoxBlur(m))
        img1 = ImageTk.PhotoImage(imgg)
        canvas2.create_image(300, 140, image=img1)
        canvas2.image = img1


def brightness(event):
    global img_path, img2, img3
    for m in range(0, v2.get() + 1):
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        imgg = ImageEnhance.Brightness(img)
        img2 = imgg.enhance(m)
        img3 = ImageTk.PhotoImage(img2)
        canvas2.create_image(300, 140, image=img3)
        canvas2.image = img3


def contrast(event):
    global img_path, img4, img5
    for m in range(0, v3.get() + 1):
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        imgg = ImageEnhance.Contrast(img)
        img4 = imgg.enhance(m)
        img5 = ImageTk.PhotoImage(img4)
        canvas2.create_image(300, 140, image=img5)
        canvas2.image = img5


def rotate_image(event):
    global img_path, img6, img7
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    img6 = img.rotate(int(rotate_combo.get()))
    img7 = ImageTk.PhotoImage(img6)
    canvas2.create_image(300, 140, image=img7)
    canvas2.image = img7


def flip_image(event):
    global img_path, img8, img9
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    if flip_combo.get() == "FLIP LEFT TO RIGHT":
        img8 = img.transpose(Image.FLIP_LEFT_RIGHT)
    elif flip_combo.get() == "FLIP TOP TO BOTTOM":
        img8 = img.transpose(Image.FLIP_TOP_BOTTOM)
    img9 = ImageTk.PhotoImage(img8)
    canvas2.create_image(300, 140, image=img9)
    canvas2.image = img9



def image_border(event):
    global img_path, img10, img11
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    img10 = ImageOps.expand(img, border=int(border_combo.get()), fill=95)
    img11 = ImageTk.PhotoImage(img10)
    canvas2.create_image(300, 140, image=img11)
    canvas2.image = img11


img1 = None
img3 = None
img5 = None
img7 = None
img9 = None
img11 = None


def save():
    global img_path, imgg, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11
    # file=None
    ext = img_path.split(".")[-1]
    file = asksaveasfilename(defaultextension=f".{ext}",
                             filetypes=[("All Files", "*.*"), ("PNG file", "*.png"), ("jpg file", "*.jpg")])
    if file:
        if canvas2.image == img1:
            imgg.save(file)
        elif canvas2.image == img3:
            img2.save(file)
        elif canvas2.image == img5:
            img4.save(file)
        elif canvas2.image == img7:
            img6.save(file)
        elif canvas2.image == img9:
            img8.save(file)
        elif canvas2.image == img11:
            img10.save(file)
        # create labels, scales and comboboxes


canvas2 = Canvas(root, width="550", height="320", relief=RIDGE, bd=2,bg="white",border=1)
canvas2.place(x=70, y=100)
img2we = ImageTk.PhotoImage(Image.open("3594969.png"))
Label(root,image=img2we,relief=FLAT,border=0).place(x=20,y=440)
v1 = IntVar()
scale1 = ttk.Scale(root, from_=0, to=10, variable=v1, orient=HORIZONTAL,command=blur)
scale1.place(x=200, y=443)
#brightness
img3b = ImageTk.PhotoImage(Image.open("1076582.png"))
Label(root,image=img3b,relief=FLAT,border=0).place(x=20,y=500)
v2 = IntVar()
scale1 = ttk.Scale(root, from_=0, to=10, variable=v2, orient=HORIZONTAL,command=brightness)
scale1.place(x=200, y=500)

#cntrast
img4c = ImageTk.PhotoImage(Image.open("587352.png"))
Label(root,image=img4c,relief=FLAT,border=0).place(x=20,y=550)
v3 = IntVar()
scale1 = ttk.Scale(root, from_=0, to=10, variable=v3, orient=HORIZONTAL,command=contrast)
scale1.place(x=200, y=560)

#rotate
img5r = ImageTk.PhotoImage(Image.open("1330172.png"))
Label(root,image=img5r,relief=FLAT,border=0).place(x=385,y=440)


values = [0, 90, 180, 270, 360]
rotate_combo = ttk.Combobox(root, values=values, font=('ariel 10 bold'))
rotate_combo.place(x=520, y=443)
rotate_combo.bind("<<ComboboxSelected>>", rotate_image)

#flip
img6f = ImageTk.PhotoImage(Image.open("734592.png"))
Label(root,image=img6f,relief=FLAT,border=0).place(x=385,y=500)
values1 = ["FLIP LEFT TO RIGHT", "FLIP TOP TO BOTTOM"]
flip_combo = ttk.Combobox(root, values=values1, font=('ariel 10 bold'))
flip_combo.place(x=520, y=500)
flip_combo.bind("<<ComboboxSelected>>", flip_image)


#border
img7br = ImageTk.PhotoImage(Image.open("16288-1.png"))
Label(root,image=img7br,relief=FLAT,border=0).place(x=385,y=550)
values2 = [i for i in range(10, 45, 5)]
border_combo = ttk.Combobox(root, values=values2, font=("ariel 10 bold"))
border_combo.place(x=520, y=550)
border_combo.bind("<<ComboboxSelected>>", image_border)


img121 = ImageTk.PhotoImage(Image.open("4814764.png"))
Button(root,image=img121,border=1,command=selected).place(x=20,y=620)
img12 = ImageTk.PhotoImage(Image.open("892634.png"))
Button(root,image=img12,border=1,command=save).place(x=300,y=620)
img13 = ImageTk.PhotoImage(Image.open("3596144.png"))
Button(root,image=img13,border=1,command=root.destroy).place(x=520,y=620)

root.mainloop()