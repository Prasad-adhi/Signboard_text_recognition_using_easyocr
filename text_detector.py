import easyocr
import pyttsx3
from google_trans_new import google_translator

def detect_recognise(l_from,l_to,path):
    reader1=easyocr.Reader([l_from])
    output=reader1.readtext(path)
    translator = google_translator() 
    translate_text=""
    for i in range(len(output)): 
        try:
            translate_text += translator.translate(output[i][1],lang_tgt=l_to) 
        except:
            print() 
    return translate_text



