import tkinter as tk
from tkinter import ttk
import shutil

class Home_layout(object):
    def __init__(self):
        self.main_frame = tk.Frame()

        grid_frame = tk.Frame(self.main_frame)
        grid_frame.pack()

        label_status = tk.Label(grid_frame, text='SSD')
        label_status.grid(column=0, row=0)

        prog_bar = ttk.Progressbar(grid_frame, orient='horizontal', length=286)
        prog_bar.grid(column=1,row=0)

    # ==================================================================================================================

        total, usado, free = shutil.disk_usage('/')
        
        perc = usado*100/total

        prog_bar['value']=perc
        prog_bar.update()

        print(perc)

        pass
