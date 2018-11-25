import tkinter as tk
import cv2
from tkinter import filedialog
from PIL import ImageTk, Image
import numpy as np

from matplotlib import pyplot as plt


class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("DIP Project GUI")

        # All the widgets which make up the initial window

        # TOP LEFT
        self.ImageChoose = tk.Button(master, text="Choose Image", width=60,
                                     command=self.choose_image, background="white")
        self.ImageChoose.grid(row=0, column=0, columnspan=3, rowspan=2, pady=10, sticky=tk.N)

        # BOTTOM
        self.BOTTOM = tk.Frame(master)
        self.BOTTOM.grid(row=4, column=0, columnspan=6)

        # BOTTOM LEFT
        self.image1 = Image.open("test_images/Lenna.png")
        self.photo1 = ImageTk.PhotoImage(self.image1)

        self.photolabel1 = tk.Label(self.BOTTOM, image=self.photo1, width=640, height=480)
        self.photolabel1.image = self.photo1
        self.photolabel1.grid(row=0, column=0, columnspan=3, sticky=tk.E)

        # BOTTOM RIGHT
        self.image2 = Image.open("test_images/Lenna0.jpg")
        self.photo2 = ImageTk.PhotoImage(self.image2)

        self.photolabel2 = tk.Label(self.BOTTOM, image=self.photo2, width=640, height=480)
        self.photolabel2.image = self.photo2
        self.photolabel2.grid(row=0, column=3, columnspan=3, sticky=tk.E)

        # self.sublabel2 = tk.Label(self.subwindow, bg="black", height=15, width=30,
        #                         font=("Courier, 20"), text="result image here")
        # self.sublabel2.grid(row=0, column=3, columnspan=3, sticky=tk.E)

        # TOP RIGHT

        self.TOPRIGHT = tk.Frame(master, bg="snow")
        self.TOPRIGHT.grid(row=0, column=3, rowspan=3, columnspan=3, stick=tk.W + tk.N)

        self.OptionChoice = tk.StringVar(master)
        self.OptionChoice.set("Choose an Operation")

        self.Operation = tk.OptionMenu(self.TOPRIGHT, self.OptionChoice, "Sharpen", "Smooth")
        self.Operation.configure(width=20, background="white")
        self.Operation.grid(row=0, column=0, columnspan=2, sticky=tk.N + tk.W)

        self.SelectChoice = tk.Button(self.TOPRIGHT, text="Select Operation", command=self.choose_oper,
                                      background="white")
        self.SelectChoice.grid(row=1, column=0, columnspan=2, sticky=tk.N + tk.W)

        self.choicesWindow = tk.Frame(self.TOPRIGHT)
        self.choicesWindow.grid(row=0, column=1, rowspan=3, columnspan=2)

        # self.Operation = tk.OptionMenu(master, self.OptionChoice, "Sharpen", "Smooth")
        # self.Operation.configure(width=20, background="white")
        # self.Operation.grid(row=0, column=3, columnspan=2, sticky=tk.N + tk.W)

        # self.SelectChoice = tk.Button(master, text="Select", command=self.choose_oper, background="white")
        # self.SelectChoice.configure(width=5)
        # self.SelectChoice.grid(row=1,column=3, columnspan=2, sticky=tk.N + tk.W)

        # self.choicesWindow = tk.Frame(self.master)
        # self.choicesWindow.grid(row=0, column=4, rowspan=3, columnspan=2)

    def choose_oper(self):
        # Chooses sharpen or smooth
        print("Chose: " + self.OptionChoice.get())
        if (self.OptionChoice.get() == "Sharpen"):
            self.sharpen_choice()

        if (self.OptionChoice.get() == "Smooth"):
            self.smooth_choice()

    def sharpen_choice(self):
        # Loads all the parameter fields for the sharpen operation
        # Apply and Save button to apply and save the right image
        print("sharpen")

        self.choicesWindow.grid_forget()

        self.choicesWindow = tk.Frame(self.TOPRIGHT, background="snow")
        self.choicesWindow.grid(row=0, column=2, rowspan=3, columnspan=2, sticky=tk.E)

        self.InputLabel1 = tk.Label(self.choicesWindow, text="input1", background="snow")
        self.InputLabel1.grid(row=0, column=1, sticky=tk.E)
        self.InputField1 = tk.Entry(self.choicesWindow, text="input1", background="white")
        self.InputField1.grid(row=0, column=2, pady=5, padx=5, sticky=tk.E + tk.W)
        self.InputLabel2 = tk.Label(self.choicesWindow, text="input2", background="snow")
        self.InputLabel2.grid(row=1, column=1, sticky=tk.E)
        self.InputField2 = tk.Entry(self.choicesWindow, text="input2", background="white")
        self.InputField2.grid(row=1, column=2, pady=5, padx=5, sticky=tk.E + tk.W)
        self.InputLabel3 = tk.Label(self.choicesWindow, text="input3", background="snow")
        self.InputLabel3.grid(row=2, column=1, sticky=tk.E)
        self.InputField3 = tk.Entry(self.choicesWindow, text="input3", background="white")
        self.InputField3.grid(row=2, column=2, pady=5, padx=5, sticky=tk.E + tk.W)

        self.ApplyButton = tk.Button(self.TOPRIGHT, text="Apply", background="white", command=self.apply)
        self.ApplyButton.grid(row=2, column=0, sticky=tk.E)

        self.SaveButton = tk.Button(self.TOPRIGHT, text="Save Image", background="white")
        self.SaveButton.grid(row=2, column=0, sticky=tk.W)

    def smooth_choice(self):
        # Loads all the parameter fields for the smooth operation
        # Apply and Save button to apply and save the right image
        print("smooth")

        self.choicesWindow.grid_forget()

        self.choicesWindow = tk.Frame(self.TOPRIGHT, background="snow")
        self.choicesWindow.grid(row=0, column=2, rowspan=3, columnspan=2, sticky=tk.E)

        self.InputField1 = tk.Button(self.TOPRIGHT, text="Averaging", background="white", command=self.load_avg_options)
        # self.InputField1 = tk.Entry(self.choicesWindow, text="input1", background="white")
        self.InputField1.grid(row=0, column=2, pady=5, padx=5, sticky=tk.E + tk.W)

        self.InputField2 = tk.Button(self.TOPRIGHT, text="Guassian", background="white",
                                     command=self.load_gaussian_options)
        # self.InputField2 = tk.Entry(self.choicesWindow, text="input2", background="white")
        self.InputField2.grid(row=1, column=2, pady=5, padx=5, sticky=tk.E + tk.W)

    def choose_image(self):
        # Changes the left image

        # prompts the user for an image path
        path = filedialog.askopenfile()
        print(path)
        print(path.name)

        # Label for image path name
        self.ImagePath = tk.Label(self.master, text=path.name, bg="snow")
        self.ImagePath.grid(row=2, column=0, columnspan=3, stick=tk.N)

        # Load the image and create a thumbnail
        self.image1 = Image.open(path.name)
        self.image1.thumbnail((640, 480))
        self.photo1 = ImageTk.PhotoImage(self.image1)

        # Actual Image
        self.photolabel1 = tk.Label(self.BOTTOM, image=self.photo1, width=640, height=480)
        self.photolabel1.image = self.photo1
        self.photolabel1.grid(row=0, column=0, columnspan=3, sticky=tk.E)

    def apply(self):
        # Here the shapen/smooth filter will be applied and the right image will be updated

        print("apply")
        self.photo2 = self.photo1
        self.photolabel2.configure(image=self.photo2)

    def load_avg_options(self):
        print("Smoothing with Averaging kernel")
        self.variable = "Average"

        img = np.array(self.image1)
        blur = cv2.blur(img, (3, 3))

        plt.subplot(121), plt.imshow(img), plt.title('Original')
        plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(blur), plt.title('Average ' )
        plt.xticks([]), plt.yticks([])
        plt.show()

        self.photolabel2.configure(image=self.photo2)

    def load_gaussian_options(self):
        print("Smoothing with Gaussian kernel")
        self.variable = "Gaussian"


        img = np.array(self.image1)
        blur = cv2.GaussianBlur(img, (9, 9), 0)

        plt.subplot(121), plt.imshow(img), plt.title('Original')
        plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(blur), plt.title('Gaussian')
        plt.xticks([]), plt.yticks([])
        plt.show()

        self.photo2 = self.photo1
        self.photolabel2.configure(image=self.photo2)


# Creates the entire window and runs it
root = tk.Tk()
root.configure(background="snow")
main = MainWindow(root)
root.mainloop()
