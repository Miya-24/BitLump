import tkinter as tk
from tkinter import messagebox
import random

NUM_OF_BIT = 8

class BitLump(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.title('Bit Lump')
    
        #Initialize bit flags
        self.bitflg_answer = 0x00
        self.bitflg_prolem = random.randrange(256)
        self.bit_msg_problem = tk.StringVar()
        self.bit_msg_problem.set('Problem: %d' % self.bitflg_prolem)
        
        #Initialize Lump images
        image = tk.PhotoImage(file = "images/denkyuu_off.png")
        self.lump_off = image.subsample(8, 8)
        image = tk.PhotoImage(file = "images/denkyuu_on.png")
        self.lump_on = image.subsample(8, 8)

        #Initialize Lump images
        image = tk.PhotoImage(file = "images/denkyuu_off.png")
        self.lump_off = image.subsample(8, 8)
        image = tk.PhotoImage(file = "images/denkyuu_on.png")
        self.lump_on = image.subsample(8, 8)

        self.lump_img = []
        for i in range(0, NUM_OF_BIT):
            self.lump_img.append(tk.Canvas(bg = "white", width = 80, height = 110))
            self.lump_img[i].create_image(0, 0, image = self.lump_off, anchor = tk.NW)
            
        #Initialize labels and buttons
        self.bit_msg_label = tk.Label(self.master, textvariable=self.bit_msg_problem)
        self.check_answer_bt = tk.Button(self.master, text='Check Answer', command = self.check_answer)
        self.reset_bt = tk.Button(self.master, text='Reset', command = self.reset)

        self.off_on_button = []
        for i in range(0, NUM_OF_BIT):
            text = '{} bit'.format(i + 1)
            self.off_on_button.append(tk.Button(text = text))
            self.off_on_button[i].bind("<1>", self.update)

        #Place
        self.bit_msg_label.grid(row = 0, column = 3, columnspan = 2)
        for i in range(0, len(self.lump_img)):
            self.lump_img[len(self.lump_img) - 1 - i].grid(row = 1, column = i)
        for i in range(0, len(self.off_on_button)):
            self.off_on_button[len(self.off_on_button) - 1 - i].grid(row = 3, column = i)
        self.check_answer_bt.grid(row = 4, column = 2, columnspan = 2)
        self.reset_bt.grid(row = 4, column = 4, columnspan = 2)

        for i in range(0, 5):
            if i == 1 or i == 2:
                self.master.grid_rowconfigure(i, weight = 1)
            else:
                self.master.grid_rowconfigure(i, weight = 10)
        for i in range(0, 8):
            self.master.grid_columnconfigure(i, weight = 1)

    #Update bit flags and lump images
    def update(self, event):
        for i in range(0, len(self.off_on_button)):
            text = '{} bit'.format(i + 1)
            if event.widget["text"] == text:
                bitflg = 1 << i
                if (self.bitflg_answer & bitflg) == 0:
                    self.bitflg_answer += bitflg
                    self.lump_img[i].create_image(0, 0, image = self.lump_on, anchor = tk.NW)
                else:
                    self.bitflg_answer -= bitflg
                    self.lump_img[i].create_image(0, 0, image = self.lump_off, anchor = tk.NW)

    #Check answer
    def check_answer(self):
        if self.bitflg_answer == self.bitflg_prolem:
            messagebox.showinfo("Answer", "Correct!!")
        else:
            messagebox.showinfo("Answer", "Wrong...")

    #Reset bit flags and lump images
    def reset(self):
        self.bitflg_answer = 0x00
        self.bitflg_prolem = random.randrange(256)
        self.bit_msg_problem.set('Problem: %d' % self.bitflg_prolem)
        
        for i in range(0, len(self.lump_img)):
            self.lump_img[i].create_image(0, 0, image = self.lump_off, anchor = tk.NW)
