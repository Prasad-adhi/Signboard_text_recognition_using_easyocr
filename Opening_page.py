# import the necessary packages
import tkinter as tk
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
import cv2
from text_detector import detect_recognise
import pyttsx3
def select_image():
    global panelA 
    global path
    path = filedialog.askopenfilename()
    if(len(path)>0):
        image = cv2.imread(path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image,(300,200))
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        if panelA is None:
            panelA = ttk.Label(image=image)
            panelA.image = image
            panelA.pack(side="left", padx=10, pady=10)
        # otherwise, update the image panels
        else:
            # update the pannels
            panelA.configure(image=image)
            panelA.image = image
def process():
    languages={"Hindi":"hi","Tamil":"ta","Assamese":"as","English":"en","Bengali":"bn",
               "Kannada":"kn","Marathi":"mr","Telugu":"te","Urdu":"ur"}
    string=detect_recognise(languages[combofrom.get()],languages[comboto.get()],path)
    engine = pyttsx3.init()
    engine.setProperty('rate', 125) 
    engine.say(string)
    engine.runAndWait()
    label=ttk.Label(root,text=string,font=("Arial",20)).pack(side="bottom")

root = tk.Tk()
panelA = None
btn = tk.Button(root, text="Select an image", command=select_image)
btn.pack( fill="both", expand="yes", padx="10", pady="10")

combofrom = tk.StringVar()
combofrom.set('Select')
l_from = ttk.Combobox(root, textvariable=combofrom, state='readonly')
l_from.pack()
l_from['values'] = ("Hindi",
                 "Tamil",
                 "Assamese",
                 "English",
                 "Bengali",
                 "Kannada",
                 "Marathi",
                 "Telugu",
                 "Urdu")

comboto = tk.StringVar()
comboto.set('Select')
l_to = ttk.Combobox(root, textvariable=comboto, state='readonly')
l_to.pack()
l_to['values'] = ("Hindi",
                 "Tamil",
                 "Assamese",
                 "English",
                 "Bengali",
                 "Kannada",
                 "Marathi",
                 "Telugu",
                 "Urdu")
btn1 = tk.Button(root, text="Process", command=process)
btn1.pack( fill="both", expand="yes", padx="10", pady="10")
# kick off the GUI
root.mainloop()