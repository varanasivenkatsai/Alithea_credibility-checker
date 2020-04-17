from flask import Flask,render_template,url_for,request,redirect
import cv2
import numpy as np
import nlp
import img_audio
app = Flask(__name__)



@app.route('/', methods=["POST","GET"])
@app.route('/home', methods=["POST","GET"])

def home():
    if request.method =="POST":
        Art_str=request.form["ar"]
        file_f=request.form["myfile"]

        if file_f.endswith('.txt'):
            Art_str=open(file_f, 'r').read()
        if file_f.endswith('.jpg'):
            Image=cv2.imread(file_f)
            Art_str=img_audio.Image2txt(Image)
        if file_f.endswith('.wav'):
            Art_str=img_audio.Aud2txt(file_f)
            
            
        
        #Score= nlp.credibility_score(Art_str)
        Related_Art=nlp.relevant_tweets(Art_str)
        return render_template("result.html",user_score=78,user_art=Related_Art,user_input=Art_str)
        
        #return redirect(url_for("user", usr=user))
    else: 
        return render_template("login.html")

@app.route('/<usr>') #dynamic
def user(usr):
    return render_template("result.html",user_name=usr)
    #return render_template()

@app.route('/w3')
def temp():
    return render_template("w3.html")


if __name__=='__main__':
    app.run(debug=True)


