from flask import Flask, request, render_template
from Converting_img import convert_img
import base64
import numpy as np
import cv2

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    result_path=None
    if request.method == 'POST':
        file = request.files['image']
        n_colors=int(request.form.get('n_colors', 5))
        #request.form: POST방식의 html폼 데이터에 접근한다.
        in_memory_file=file.read()
        np_img=np.frombuffer(in_memory_file, np.uint8)
        img=cv2.imdecode(np_img, cv2.IMREAD_COLOR)

        result_img=convert_img(img, n_colors)
        _,buffer=cv2.imencode('.png', result_img)
        result_base64=base64.b64encode(buffer).decode('utf-8')
        
        return render_template('index.html', result_img=result_base64)
    return render_template('index.html')
    #render_template는 html등 템플릿 파일을 서버에 렌더링하여 결과생성, 반환한다.
    #templates폴더에 있는 html파일을 가져온다.
    #두번째인자부턴 html에 넘겨줄 변수(데이터)를 전달한다.



