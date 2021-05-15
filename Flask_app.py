from flask import Flask, json, render_template, request,jsonify
from flask import send_from_directory
from PIL import Image
from tkinter import filedialog
from werkzeug.utils import secure_filename
from text_detector import detect_recognise
import easyocr
import pyttsx3
from google_trans_new import google_translator
import cv2
import numpy as np
import os

app=Flask(__name__)
app.config['UPLOAD_FOLDER']="./Uploads"

@app.route("/")
def initial():
    return render_template("initial.html")

@app.route("/image_data",methods=["GET","POST"])
def translate():
    f = request.files['img1']
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
    path="Uploads/"+f.filename
    string=detect_recognise(request.form['from'],request.form['to'],path)
    engine = pyttsx3.init()
    engine.setProperty('rate', 125) 
    engine.say(string)
    engine.runAndWait()
    text={}
    text['text']=string
    return jsonify(text)


if __name__ == '__main__':
   app.run(debug = True)