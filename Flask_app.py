from flask import Flask, json, render_template, request,jsonify
from flask import send_from_directory
from PIL import Image
from werkzeug.utils import secure_filename
from text_detector import detect_recognise
import easyocr
import pyttsx3
from google_trans_new import google_translator
import cv2
import numpy as np

app=Flask(__name__)


@app.route("/")
def initial():
    return render_template("initial.html")

@app.route("/image_data",methods=["GET","POST"])
def translate():
    image=""
    if(request.method=='POST'):
        data =request.files['img1']
        img = Image.open(request.files['img1'])
        img = np.array(img)
        img = cv2.resize(img,(224,224))
        img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
    print(request.form['from'],request.form['to'])
    string=detect_recognise(request.form['from'],request.form['to'],img)
    engine = pyttsx3.init()
    engine.setProperty('rate', 125) 
    engine.say(string)
    engine.runAndWait()
    text={}
    text['text']=string
    return string


if __name__ == '__main__':
   app.run(debug = True)