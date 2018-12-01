from tkinter import *


class MainWindow:
    def __init__(self):
        self.root = Tk()

        self.canvas = Canvas(self.root, width=640, height=480)
        self.canvas.bind("<Key>", MainWindow.key)
        self.canvas.bind("<Button-1>", MainWindow.callback)
        self.canvas.pack(expand=YES)
        # self.canvas.create_image(image=WebFeed.get_feed_single_image(), anchor=NW)

    @staticmethod
    def key(event):
        print("pressed", repr(event.char))

    @staticmethod
    def callback(event):
        print("clicked at", event.x, event.y)

    def run(self):
        self.root.mainloop()