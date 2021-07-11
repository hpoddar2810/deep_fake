from flask import Flask, render_template, request, url_for
import cv2
import os
from Process import process

app = Flask(__name__)
app.config["UPLOADS"] = "E:/PROJECTS/Deep_fake/first-order-model/"   #E:\PROJECTS\Deep_fake\first-order-model

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    if not request.files.get('img') or not request.files.get('src_video'):
        return render_template('index.html')
    
    src_video = request.files.get('src_video')
    img = request.files.get('img')

    src_video.save(os.path.join(app.config["UPLOADS"], '1.mp4'))
    img.save(os.path.join(app.config["UPLOADS"], '2.jpg'))
    process()

    return render_template('result.html')


if __name__ == '__main__':
    app.run()