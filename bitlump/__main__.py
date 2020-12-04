
import tkinter as tk
from bitlump.bit_lump import BitLump

def main():
    root = tk.Tk()
    root.option_add('*font', ('FixedSys', 24))
    bl = BitLump(master = root)
    bl.mainloop()

if __name__ == "__main__":
    main()