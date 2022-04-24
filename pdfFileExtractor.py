import tkinter as tk
from turtle import onclick, width
import PyPDF2
from PIL import Image, ImageTk
import time
from tkinter.filedialog import askopenfile

from numpy import pad

# all the elements we are going to create will be within these 2 lines of code i.e. root = tk.Tk() and root.mainloop()
root = tk.Tk()
root.title("PDF text extractor")
canvas = tk.Canvas(root, width=300, height=450)
canvas.grid(columnspan=6, rowspan=3)

#logo
logo = Image.open("logo.png")
# converting above pil image to tkinter image
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image = logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# instructions
instructions = tk.Label(root,text= "Select a PDF file on your computer to extract all its text", font= "Raleway")
instructions.grid(columnspan=3, row=1, column=0)

# browse button
button_text = tk.StringVar()

button = tk.Button(textvariable= button_text, width=15, height=2, font="Raleway", bg="Red", fg="white", command=lambda:readPdf())
button_text.set("Browse")
button.grid(column=1, row=2)

def readPdf():
    button_text.set("Loading...")
    file = askopenfile(parent= root, mode = "rb", title="Choose a file", filetypes=[("Pdf file", "*.pdf")])
    if file:
        print("file was sucessfully loaded")
        text = PyPDF2.PdfFileReader(file)
        page = text.getPage(0)
        pageContent = page.extractText()
        # print(pageContent)

    # text_box
    
    text_box = tk.Text(root, height=12, width= 50)
    text_box.insert(1.0, pageContent)
    text_box.tag_configure("center", justify="center")
    text_box.tag_add("center", 1.0, "end")
    text_box.grid(column=1, row=3)

    s = tk.Scrollbar( root, orient=tk.VERTICAL, command=text_box.yview)
    text_box.configure(yscrollcommand=s.set)
    button_text.set("Browse")


root.mainloop()