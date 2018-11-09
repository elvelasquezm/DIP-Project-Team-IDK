import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("DIP Project GUI")

        #TOP LEFT
        self.ImageChoose = tk.Button(master, text="Choose Image", width=60,
                                     command=self.choose_image, background="white")
        self.ImageChoose.grid(row=0, column=0, columnspan=3, rowspan=3, pady=10, sticky= tk.N)

        #BOTTOM
        self.BOTTOM=tk.Frame(master)
        self.BOTTOM.grid(row=4, column=0, columnspan=6)

        #BOTTOM LEFT

        image = Image.open("test_images/Lenna.png")
        photo = ImageTk.PhotoImage(image)

        self.photolabel=tk.Label(self.BOTTOM, image=photo, width = 640, height=480)
        self.photolabel.image = photo
        self.photolabel.grid(row=0, column=0, columnspan=3, sticky=tk.E)

        # BOTTOM RIGHT

        image2 = Image.open("test_images/Lenna0.jpg")
        photo2 = ImageTk.PhotoImage(image2)

        self.photolabel2=tk.Label(self.BOTTOM, image=photo2, width=640, height=480)
        self.photolabel2.image = photo2
        self.photolabel2.grid(row = 0, column=3, columnspan=3, sticky=tk.E)

        #self.sublabel2 = tk.Label(self.subwindow, bg="black", height=15, width=30,
        #                         font=("Courier, 20"), text="result image here")
        #self.sublabel2.grid(row=0, column=3, columnspan=3, sticky=tk.E)



        #TOP RIGHT

        self.TOPRIGHT = tk.Frame(master, bg="snow")
        self.TOPRIGHT.grid(row=0, column=3, rowspan=3, columnspan=3, stick= tk.W + tk.N)

        self.OptionChoice = tk.StringVar(master)
        self.OptionChoice.set("Choose an Operation")

        self.Operation = tk.OptionMenu(self.TOPRIGHT, self.OptionChoice, "Sharpen", "Smooth")
        self.Operation.configure(width=20, background="white")
        self.Operation.grid(row=0, column=0, columnspan=2, sticky=tk.N + tk.W)

        self.SelectChoice = tk.Button(self.TOPRIGHT, text="Select Operation", command=self.choose_oper,
                                      background="white")
        self.SelectChoice.grid(row=1,column=0, columnspan=2, sticky=tk.N + tk.W)

        self.choicesWindow = tk.Frame(self.TOPRIGHT)
        self.choicesWindow.grid(row=0, column=1, rowspan=3, columnspan=2)

        #self.Operation = tk.OptionMenu(master, self.OptionChoice, "Sharpen", "Smooth")
        #self.Operation.configure(width=20, background="white")
        #self.Operation.grid(row=0, column=3, columnspan=2, sticky=tk.N + tk.W)

        #self.SelectChoice = tk.Button(master, text="Select", command=self.choose_oper, background="white")
        #self.SelectChoice.configure(width=5)
        #self.SelectChoice.grid(row=1,column=3, columnspan=2, sticky=tk.N + tk.W)

        #self.choicesWindow = tk.Frame(self.master)
        #self.choicesWindow.grid(row=0, column=4, rowspan=3, columnspan=2)

    def choose_oper(self):
        print("Chose: " + self.OptionChoice.get())
        if(self.OptionChoice.get() == "Sharpen"):
            self.sharpen_choice()

        if(self.OptionChoice.get() == "Smooth"):
            self.smooth_choice()

    def sharpen_choice(self):
        print("sharpen")


        self.choicesWindow.grid_forget()

        self.choicesWindow=tk.Frame(self.TOPRIGHT, background="snow")
        self.choicesWindow.grid(row=0,column=2, rowspan=3,columnspan=2, sticky=tk.E)

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

        self.ApplyButton = tk.Button(self.TOPRIGHT, text="Apply", background="white")
        self.ApplyButton.grid(row=2, column=0, sticky=tk.E)

        self.SaveButton = tk.Button(self.TOPRIGHT, text="Save Image", background="white")
        self.SaveButton.grid(row=2, column=0, sticky=tk.W)

    def smooth_choice(self):
        print("smooth")

        self.choicesWindow.grid_forget()

        self.choicesWindow=tk.Frame(self.TOPRIGHT, background="snow")
        self.choicesWindow.grid(row=0,column=2, rowspan=3,columnspan=2, sticky=tk.E)

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

        self.ApplyButton = tk.Button(self.TOPRIGHT, text="Apply", background="white")
        self.ApplyButton.grid(row=2, column=0, sticky=tk.E)

        self.SaveButton = tk.Button(self.TOPRIGHT, text="Save Image", background="white")
        self.SaveButton.grid(row=2, column=0, sticky=tk.W)

    def choose_image(self):
        path = filedialog.askopenfile()
        print(path)

root = tk.Tk()
root.configure(background="snow")
main = MainWindow(root)
root.mainloop()