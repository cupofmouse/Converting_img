from flask import Flask, request, render_template
from Converting_img import convert_img
import base64
import numpy as np
import cv2

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    result_img=None
    if request.method == 'POST':
        file = request.files['image']
        n_colors=int(request.form.get('n_colors', 5))

        in_memory_file=file.read()
        np_img=np.frombuffer(in_memory_file, np.uint8)
        img=cv2.imdecode(np_img, cv2.IMREAD_COLOR)

        result_img=convert_img(img, n_colors)
        _,buffer=cv2.imencode('.png', result_img)
        result_base64=base64.b64encode(buffer).decode('utf-8')
        print("Result base64 length: ", len(result_base64))
        print("Result img: ", result_base64[:100])
        return render_template('index.html', result_img=result_base64)
    return render_template('index.html')

import os
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


