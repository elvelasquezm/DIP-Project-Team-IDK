import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("DIP Project GUI")

        self.ImageChoose = tk.Button(master, text="Choose Image", width=60,
                                     command=self.choose_image, background="white")
        self.ImageChoose.grid(row=0, column=0, columnspan=3, rowspan=3, pady=10, padx=28,
                              sticky=tk.N)

        self.subwindow=tk.Frame(master)
        self.subwindow.grid(row=4,column=0, columnspan=6)
        self.sublabel1=tk.Label(self.subwindow, bg="light blue", height=15, width=30,
                                font = ("Courier, 20"), text="input image here?")
        self.sublabel1.grid(row=0,column=0, columnspan=3, sticky=tk.E)
        self.sublabel2 = tk.Label(self.subwindow, bg="light green", height=15, width=30,
                                 font=("Courier, 20"), text="result image here?")
        self.sublabel2.grid(row=0, column=3, columnspan=3, sticky=tk.E)

        self.OptionChoice = tk.StringVar(master)
        self.OptionChoice.set("Choose an Operation")
        self.Operation = tk.OptionMenu(master, self.OptionChoice, "Sharpen", "Smooth")
        self.Operation.configure(width=20, background="white")
        self.Operation.grid(row=0, column=3, columnspan=2, sticky=tk.N + tk.W)

        self.SelectChoice = tk.Button(master, text="Select", command=self.choose_oper, background="white")
        self.SelectChoice.configure(width=5)
        self.SelectChoice.grid(row=1,column=3, columnspan=2, sticky=tk.N + tk.W)

        self.choicesWindow = tk.Frame(self.master)
        self.choicesWindow.grid(row=0, column=4, rowspan=3, columnspan=2)

    def choose_oper(self):
        print("Chose: " + self.OptionChoice.get())
        if(self.OptionChoice.get() == "Sharpen"):
            self.sharpen_choice()

        if(self.OptionChoice.get() == "Smooth"):
            self.smooth_choice()

    def sharpen_choice(self):
        print("sharpen")

        self.choicesWindow.grid_forget()

        self.choicesWindow=tk.Frame(self.master, background="snow")
        self.choicesWindow.grid(row=0,column=4, rowspan=3,columnspan=2)

        self.InputLabel1 = tk.Label(self.choicesWindow, text="input1", background="snow")
        self.InputLabel1.grid(row=0, column=0, sticky=tk.E)
        self.InputField1 = tk.Entry(self.choicesWindow, text="input1", background="white")
        self.InputField1.grid(row=0, column=1, pady=5, padx=5, sticky=tk.E + tk.W)
        self.InputLabel2 = tk.Label(self.choicesWindow, text="input2", background="snow")
        self.InputLabel2.grid(row=1, column=0, sticky=tk.E)
        self.InputField2 = tk.Entry(self.choicesWindow, text="input2", background="white")
        self.InputField2.grid(row=1, column=1, pady=5, padx=5, sticky=tk.E + tk.W)
        self.InputLabel3 = tk.Label(self.choicesWindow, text="input3", background="snow")
        self.InputLabel3.grid(row=2, column=0, sticky=tk.E)
        self.InputField3 = tk.Entry(self.choicesWindow, text="input3", background="white")
        self.InputField3.grid(row=2, column=1, pady=5, padx=5, sticky=tk.E + tk.W)

        self.ApplyButton = tk.Button(self.master, text="Apply", background="white")
        self.ApplyButton.grid(row=2, column=3, sticky=tk.E)

        self.SaveButton = tk.Button(self.master, text="Save Image", background="white")
        self.SaveButton.grid(row=2, column=3, sticky=tk.W)

    def smooth_choice(self):
        print("smooth")

        self.choicesWindow.grid_forget()

        self.choicesWindow = tk.Frame(self.master, background="snow")
        self.choicesWindow.grid(row=0, column=4, rowspan=3, columnspan=2)

        self.InputLabel1 = tk.Label(self.choicesWindow, text="input1", background="snow")
        self.InputLabel1.grid(row=0, column=0, sticky=tk.E)
        self.InputField1 = tk.Entry(self.choicesWindow, text="input1", background="white")
        self.InputField1.grid(row=0, column=1, pady=5, padx=5, sticky=tk.E + tk.W)
        self.InputLabel2 = tk.Label(self.choicesWindow, text="input2", background="snow")
        self.InputLabel2.grid(row=1, column=0, sticky=tk.E)
        self.InputField2 = tk.Entry(self.choicesWindow, text="input2", background="white")
        self.InputField2.grid(row=1, column=1, pady=5, padx=5, sticky=tk.E + tk.W)
        self.InputLabel3 = tk.Label(self.choicesWindow, text="input3", background="snow")
        self.InputLabel3.grid(row=2, column=0, sticky=tk.E)
        self.InputField3 = tk.Entry(self.choicesWindow, text="input3", background="white")
        self.InputField3.grid(row=2, column=1, pady=5, padx=5, sticky=tk.E + tk.W)

        self.ApplyButton = tk.Button(self.master, text="Apply", background="white")
        self.ApplyButton.grid(row=2, column=3, sticky=tk.E)

        self.SaveButton = tk.Button(self.master, text="Save Image", background="white")
        self.SaveButton.grid(row=2, column=3, sticky=tk.W)

    def choose_image(self):
        path = filedialog.askopenfile()
        print(path)

root = tk.Tk()
root.resizable(False, False)
root.configure(background="snow")
main = MainWindow(root)
root.mainloop()