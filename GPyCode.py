import numpy as np
import tkinter as tk
import customtkinter as ctk

class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.minsize(800, 600)
        self.title('GPyCode')
    
    


app = App()
app.mainloop()