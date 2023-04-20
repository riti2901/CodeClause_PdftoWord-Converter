import tkinter as tk
from tkinter import filedialog   #filedialog provides classes and library to create file selection windows
import pdf2docx  #open source python library for converting pdf file to word file.
import os #the os module provides functions for interacting with the operating system


def select_file():
   #opens up a window to select a PDF file which you want to convert it into the word file

    file_path = filedialog.askopenfilename(    
        filetypes=[("PDF Files", "*.pdf")])
    pdf_path_entry.delete(0, tk.END)
    pdf_path_entry.insert(0, file_path)

def convert_pdf_to_word():
#In this, It converts the Selected pdf file into the word file

    pdf_path = pdf_path_entry.get()
    word_path = word_path_entry.get()

    downloads_dir = os.path.expanduser("~/Downloads")

    initial_dir = downloads_dir

    file_path = filedialog.asksaveasfilename(
        initialdir=initial_dir,
        initialfile=word_path,
        title="Save Word File",
        defaultextension=".docx",
        filetypes=[("Word Files", "*.docx")],
    )

    pdf2docx.parse(pdf_path, file_path)

root = tk.Tk()
root.title("PDF_to_Word Converter")
root.geometry("400x400")
root.configure(padx=200, pady=200)
root.configure(padx=20, pady=20, bg="salmon1")


font = ("TkDefaultFont", 20)

pdf_path_label = tk.Label(root,text="Pdf file to Word file Converter!!", font=("Arial",32),bg="salmon1")
pdf_path_label.grid(row=0, column=2, padx=20, pady=20)

pdf_path_label = tk.Label(root, text="PDF File:", font=(font),bg="salmon1")
pdf_path_label.grid(row=1, column=1, padx=120, pady=60)

pdf_path_entry = tk.Entry(root, font=font)
pdf_path_entry.grid(row=1, column=2, padx=120, pady=60)

pdf_path_button = tk.Button(root, text="Select File", command=select_file, font=font,bg="skyblue")
pdf_path_button.grid(row=1, column=3, padx=100, pady=60)

word_path_label = tk.Label(root, text=" Word File:", font=font,bg="salmon1")
word_path_label.grid(row=2, column=1, padx=10, pady=10)

word_path_entry = tk.Entry(root, font=font)
word_path_entry.grid(row=2, column=2, padx=10, pady=10)

convert_button = tk.Button(root, text="Convert to Word", command=convert_pdf_to_word, font=font,bg="skyblue")
convert_button.grid(row=2, column=3, padx=10, pady=10)

root.mainloop()
