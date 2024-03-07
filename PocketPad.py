import tkinter as tk
import os, sys
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = tk.Tk()
window.title("PocketPad")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

icon_path = os.path.join(getattr(sys, '_MEIPASS', os.path.abspath(".")), "favicon.ico")
try:
    window.iconbitmap(icon_path)
except tk.TclError:
    print("Warning: Icon file 'favicon.ico' not found or could not be loaded.")

def open_file():
    filepath = askopenfilename(
        filetypes=[('Text Files', "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return None
    with open(filepath, mode="r+", encoding="utf-8") as input_files:
        txt_edit.delete("1.0", tk.END)
        text = input_files.read()
        txt_edit.insert(tk.END ,text)
    window.title(f"Text Editor - {filepath}")    

def save_file():
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath: return None
    with open(filepath, mode="w", encoding="utf-8") as output_files:
        text = txt_edit.get("1.0", tk.END)
        output_files.write(text)
    window.title(f"Text Editor - {filepath}")    

def dark_mode():
    status = btn_dark.cget("text")
    if (status == "Dark Mode"):
        txt_edit.config(bg="black", fg="#16FF00")
        frm_buttons.config(bg="black", cursor="cross")
        btn_open.config(bg="black", fg="#16FF00")
        btn_save.config(bg="black", fg="#16FF00")
        btn_dark.config(bg="black", fg="#16FF00", text="Light Mode")
        txt_edit.config(insertbackground="white")
    if (status == "Light Mode"):
        txt_edit.config(bg="white", fg="black")
        frm_buttons.config(bg="white", cursor="arrow")
        btn_open.config(bg="white", fg="black")
        btn_save.config(bg="white", fg="black")
        btn_dark.config(bg="white", fg="black", text="Dark Mode")
        txt_edit.config(insertbackground="black")


txt_edit = tk.Text(master=window, font=("Sans, 14"))
frm_buttons = tk.Frame(master=window, relief=tk.RAISED, border=2)
btn_open = tk.Button(master=frm_buttons, text="Open", command=open_file)
btn_save = tk.Button(master=frm_buttons, text="Save As", command=save_file)
btn_dark = tk.Button(master=frm_buttons, text="Dark Mode", command=dark_mode)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_dark.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()