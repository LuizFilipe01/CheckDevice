import tkinter as tk
from screen import home

class App(object):
    def __init__(self):
        win = tk.Tk()

        win.wm_title('Relatório de disco')

        pack = home.Home_layout()
        pack.main_frame.pack()

        win.geometry('350x100')
        win.mainloop()
        pass


if __name__ == "__main__":
    App()
