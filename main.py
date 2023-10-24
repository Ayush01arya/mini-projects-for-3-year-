import time
from tkinter import*
from tkinter import ttk
from tkinter .ttk import Progressbar
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
import cv2

from PIL import Image, ImageTk
fun=Tk()
fun.configure(bg="white")
fun.geometry("1500x664+10+50")
fun.overrideredirect(TRUE)
cross = ImageTk.PhotoImage(Image.open("Rectangle 10.png"))

def run():
    task = 10
    x = 0
    while (x < task):
        time.sleep(0.5)
        bar['value'] += 30
        x += 1
        fun.update_idletasks()
    fun.destroy()
    from PIL import Image, ImageTk

    from tkinter.font import Font
    from tkinter import filedialog
    from tkinter.filedialog import askopenfilename, asksaveasfilename
    import os
    root = Tk()

    root.config(bg="white")
    root.geometry("1500x664+10+50")
    root.resizable(0, 0)
    root.title("Image cartoonifier By Ayush Arya")
    photo = PhotoImage(file="start.png")
    root.iconphoto(False, photo)
    from PIL import Image, ImageTk
    img1o = ImageTk.PhotoImage(Image.open("homeml.png"))
    Label(root, image=img1o, bd=0,border=0, relief=FLAT).place(x=0, y=0)
    root.update()
    time.sleep(3)
    cross = ImageTk.PhotoImage(Image.open("Rectangle 10.png"))

    img1 = ImageTk.PhotoImage(Image.open("home.png"))
    Label(root, image=img1,bd=0, border=0, bg="white",relief=FLAT).place(x=0, y=0)
    root.update()

    root.update()

    def selected():
        global img_path, img
        img_path = filedialog.askopenfilename(initialdir=os.getcwd())
        img = Image.open(img_path)
        img.thumbnail((550, 350))
        # imgg = img.filter(ImageFilter.BoxBlur(0))
        img1 = ImageTk.PhotoImage(img)
        canvas2.create_image(380, 194, image=img1)
        canvas2.image = img1

    def cartoon():

        global img_path, img4, img5

        img = Image.open(img_path)
        img.thumbnail((350, 350))
        image = cv2.imread(img_path)
        image = cv2.resize(image, (760, 388))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
        color = cv2.bilateralFilter(image, d=9, sigmaColor=250, sigmaSpace=250)
        cartoon = cv2.bitwise_and(color, color, mask=edges)
        cv2.imshow('Cartoon',cartoon)


    def blur():
        global img_path, img4, img5
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        image = cv2.imread(img_path)
        image = cv2.resize(image, (760, 388))
        ksize = (10, 10)

        image3 = cv2.blur(image, ksize)
        cv2.imshow('Blur', image3)

    def medianblur():
        global img_path, img4, img5
        imgs = Image.open(img_path)
        imgs.thumbnail((350, 350))
        import numpy as np
        import cv2

        # Read image
        img_src = cv2.imread(img_path)

        # Edge detection filter
        kernel = np.array([[0.0, -1.0, 0.0],
                           [-1.0, 4.0, -1.0],
                           [0.0, -1.0, 0.0]])

        kernel = kernel / (np.sum(kernel) if np.sum(kernel) != 0 else 1)

        # Filter the source image
        img_rst = cv2.filter2D(img_src, -1, kernel)

        # Save result image
        image = cv2.resize(img_rst, (760, 388))
        cv2.imshow('Edge Detection', image)
        #cv2.imwrite('result.jpg', img_rst)
    def saturation():
        global img_path, img4, img5
        img = Image.open(img_path)
        img.thumbnail((350, 350))

        image = cv2.imread(img_path)
        image = cv2.resize(image, (760, 388))
        img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        #cv2.imshow("HSV Image", img_hsv)
        #cv2.imshow("Hue Channel", img_hsv[:, :, 0])
        cv2.imshow("Saturation", img_hsv[:, :, 1])
        #cv2.imshow("Value", img_hsv[:, :, 2])
    def hsv():
        global img_path, img4, img5
        img = Image.open(img_path)
        img.thumbnail((350, 350))

        image = cv2.imread(img_path)
        image = cv2.resize(image, (760, 388))
        img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        cv2.imshow("HSV", img_hsv)

    def hue():
        global img_path, img4, img5
        img = Image.open(img_path)
        img.thumbnail((350, 350))

        image = cv2.imread(img_path)
        image = cv2.resize(image, (760, 388))
        img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        cv2.imshow("Hue Channel", img_hsv[:, :, 0])
    def blackwhite():
        global img_path, img4, img5
        img = Image.open(img_path)
        img.thumbnail((350, 350))

        image = cv2.imread(img_path)
        image = cv2.resize(image, (760, 388))
        img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Black & White", img_hsv)
    def croped():
        global img_path, img4, img5
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        import numpy as np
        img = cv2.imread(img_path)
        height, widht = img.shape[:2]
        row, col = int(height * .25), int(widht * .25)
        end_row, end_col = int(height * .75), int(widht * .75)
        crop = img[row:end_row, col:end_col]
        image = cv2.resize(crop, (760, 388))
        cv2.imshow("Cropped", image)
    def sobelx():
        global img_path, img4, img5
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        import numpy as np
        img = cv2.imread(img_path, 0)
        heigth, width = img.shape
        sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)

        image = cv2.resize(sobelx, (760, 388))
        cv2.imshow("SobelX", image)
    def sobely():
        global img_path, img4, img5
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        import numpy as np
        img = cv2.imread(img_path, 0)
        heigth, width = img.shape

        sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
        image = cv2.resize(sobely, (760, 388))
        cv2.imshow("SobelY", image)
    def smaller():
        global img_path, img4, img5
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        image = cv2.imread(img_path)
        image = cv2.resize(image, (760, 388))
        smaller = cv2.pyrDown(image)
        cv2.imshow("Smaller", smaller)

    def larger():
        global img_path, img4, img5
        img = Image.open(img_path)
        image = cv2.imread(img_path)
        image = cv2.resize(image, (760, 388))
        larger = cv2.pyrUp(image)

        cv2.imshow("Larger", larger)
    def binaryimage():
        global img_path, img4, img5
        img = Image.open(img_path)
        img.thumbnail((350, 350))

        image = cv2.imread(img_path)
        image = cv2.resize(image, (550, 550))
        img = cv2.imread(img_path, 0)
        ret, bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        image = cv2.resize(bw, (760, 388))
        cv2.imshow("Binary Image", image)
    def blue():
        import numpy as np
        global img_path, img4, img5
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        imgm = cv2.imread(img_path)

        B, G, R = cv2.split(imgm)
        zeros = np.zeros(imgm.shape[:2], dtype="uint8")
        image = cv2.resize(cv2.merge([B, zeros, zeros]), (760, 388))
        cv2.imshow("Blue",image )
    def green():
        import numpy as np
        global img_path, img4, img5
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        imgm = cv2.imread(img_path)


        B, G, R = cv2.split(imgm)
        zeros = np.zeros(imgm.shape[:2], dtype="uint8")
        image = cv2.resize(cv2.merge([zeros, G, zeros]), (760, 388))
        cv2.imshow("Green", image)

    def red():
        import numpy as np
        global img_path, img4, img5
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        imgm = cv2.imread(img_path)


        B, G, R = cv2.split(imgm)
        zeros = np.zeros(imgm.shape[:2], dtype="uint8")
        image = cv2.resize(cv2.merge([zeros, zeros, R]), (760, 388))
        cv2.imshow("Red", image)
    def luv():
        import numpy as np
        global img_path, img4, img5
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        img = cv2.imread(img_path)

        ret = cv2.cvtColor(img, cv2.COLOR_RGB2LUV)
        image = cv2.resize(ret, (760, 388))
        cv2.imshow("Luv Filter", image)
    def contrast():
        global img_path, img4, img5
        img = Image.open(img_path)
        img.thumbnail((350, 350))

        image = cv2.imread(img_path)
        image = cv2.resize(image, (760, 388))
        ret, bw = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
        cv2.imshow("Threshold (Contrast)", bw)
        #cv2.imshow("Contrast", img_hsv)






    canvas2 = Canvas(root, width="767", height="381", relief=RIDGE, bd=1, bg="white", border=0)
    canvas2.place(x=81, y=78)
    root.update()
    Button(root, image=cross, bg="#D9D9D9", relief=FLAT, activebackground="#D9D9D9", command=selected, border=0).place(x=65,
                                                                                                                   y=554)
    cartoon23 = ImageTk.PhotoImage(Image.open("Rectangle 14.png"))
    Button(root, image=cartoon23, bg="#D9D9D9", relief=FLAT, activebackground="#D9D9D9", command=cartoon, border=0).place(
        x=1180,
        y=87)
    blur23 = ImageTk.PhotoImage(Image.open("Rectangle 15.png"))
    Button(root, image=blur23, bg="#D9D9D9", relief=FLAT, activebackground="#D9D9D9", command=blur,
           border=0).place(
        x=1259,
        y=87)
    medianblur23 = ImageTk.PhotoImage(Image.open("Rectangle 26.png"))
    Button(root, image=medianblur23, bg="#D9D9D9", relief=FLAT, activebackground="#D9D9D9", command=medianblur,
           border=0).place(
        x=1338,
        y=87)
    saturation23 = ImageTk.PhotoImage(Image.open("Rectangle 34.png"))
    Button(root, image=saturation23, bg="#D9D9D9", relief=FLAT, activebackground="#D9D9D9", command=saturation,
           border=0).place(
        x=1338,
        y=435)
    hsv23 = ImageTk.PhotoImage(Image.open("Rectangle 25.png"))
    Button(root, image=hsv23, bg="#D9D9D9", relief=FLAT, activebackground="#D9D9D9", command=hsv,
           border=0).place(
        x=1259,
        y=522)
    huechannel23 = ImageTk.PhotoImage(Image.open("Rectangle 24.png"))
    Button(root, image=huechannel23, bg="#D9D9D9", relief=FLAT, activebackground="#D9D9D9", command=hue,
           border=0).place(
        x=1180,
        y=522)
    blackwhite23 = ImageTk.PhotoImage(Image.open("Rectangle 18.png"))
    Button(root, image=blackwhite23, bg="#D9D9D9", relief=FLAT, activebackground="#D9D9D9", command=blackwhite,
           border=0).place(
        x=1180,
        y=261)
    crop23 = ImageTk.PhotoImage(Image.open("Rectangle 16.png"))
    Button(root, image=crop23, bg="#D9D9D9", relief=FLAT, activebackground="#D9D9D9", command=croped,
           border=0).place(
        x=1180,
        y=174)
    sobelx23 = ImageTk.PhotoImage(Image.open("Rectangle 17.png"))
    Button(root, image=sobelx23, bg="#D9D9D9", relief=FLAT, activebackground="#D9D9D9", command=sobelx,
           border=0).place(
        x=1259,
        y=174)
    sobely23 = ImageTk.PhotoImage(Image.open("Rectangle 28.png"))
    Button(root, image=sobely23, bg="#D9D9D9", relief=FLAT, activebackground="#D9D9D9", command=sobely,
           border=0).place(
        x=1338,
        y=174)
    smaller23 = ImageTk.PhotoImage(Image.open("Rectangle 19.png"))
    Button(root, image=smaller23, bg="#D9D9D9", relief=FLAT, activebackground="#D9D9D9", command=smaller,
           border=0).place(
        x=1259,
        y=261)
    larger23 = ImageTk.PhotoImage(Image.open("Rectangle 30.png"))
    Button(root, image=larger23, bg="#D9D9D9", relief=FLAT, activebackground="#D9D9D9", command=larger,
           border=0).place(
        x=1338,
        y=261)
    binary23 = ImageTk.PhotoImage(Image.open("Rectangle 21.png"))
    Button(root, image=binary23, bg="#D9D9D9", relief=FLAT, activebackground="#D9D9D9", command=binaryimage,
           border=0).place(
        x=1259,
        y=348)

    blue23 = ImageTk.PhotoImage(Image.open("Rectangle 32.png"))
    Button(root, image=blue23, bg="#D9D9D9", relief=FLAT, activebackground="#D9D9D9", command=blue,
           border=0).place(
        x=1338,
        y=348)
    green23 = ImageTk.PhotoImage(Image.open("Rectangle 22.png"))
    Button(root, image=green23, bg="#D9D9D9", relief=FLAT, activebackground="#D9D9D9", command=green,
           border=0).place(
        x=1180,
        y=435)
    red23 = ImageTk.PhotoImage(Image.open("Rectangle 23.png"))
    Button(root, image=red23, bg="#D9D9D9", relief=FLAT, activebackground="#D9D9D9", command=red,
           border=0).place(
        x=1259,
        y=435)
    contrast23 = ImageTk.PhotoImage(Image.open("Rectangle 36.png"))
    Button(root, image=contrast23, bg="#D9D9D9", relief=FLAT, activebackground="#D9D9D9", command=contrast,
           border=0).place(
        x=1338,
        y=524)
    luv23 = ImageTk.PhotoImage(Image.open("Rectangle 20.png"))
    Button(root, image=luv23, bg="#D9D9D9", relief=FLAT, activebackground="#D9D9D9", command=luv,
           border=0).place(
        x=1180,
        y=348)

    root.update()










    root.mainloop()

fun.after(1000,run)


imge1 = ImageTk.PhotoImage(Image.open("start.png"))
Label(fun,image=imge1,font=("simsun","10","bold"),bg="white",border=0,relief=FLAT).place(x=0,y=0)
bar = Progressbar(fun,orient=HORIZONTAL,length=1500)
bar.place(x=0,y=645,height=20)

fun.update()
fun.update()
fun.mainloop()