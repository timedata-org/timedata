from tkinter import Tk, ttk

from timedata.instruments.dmx.laser import ui


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.dmx_level = ui.DMXLevelCanvas(self.master)
        self.dmx_level.pack()

    def greet(self):
        print("Greetings!")

    def old(self):
        self.label = ttk.Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = ttk.Button(
            master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = ttk.Button(
            master, text="Close", command=master.quit)
        self.close_button.pack()


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
