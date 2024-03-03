import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = tk.Tk()
window.title("NotePad")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

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


txt_edit = tk.Text(master=window)
frm_buttons = tk.Frame(master=window, relief=tk.RAISED, border=2)
btn_open = tk.Button(master=frm_buttons, text="Open", command=open_file)
btn_save = tk.Button(master=frm_buttons, text="Save As", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")


window.mainloop()