from flask import Flask,render_template,Response
from flask import request
import logging
import netron
import urllib.request
import _thread

app = Flask(__name__, static_url_path='/',)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s')


@app.route('/downloadfile', methods=['GET', 'POST'])
def downloadfile():
    # 流式读取
    def send_file():
        store_path = "/Users/liguodong/temp/softmax.pth"
        with open(store_path, 'rb') as targetfile:
            while 1:
                data = targetfile.read(20 * 1024 * 1024)  # 每次读取20M
                if not data:
                    break
                yield data

    response = Response(send_file(), content_type='application/octet-stream')
    response.headers["Content-disposition"] = 'attachment; filename=%s' % "softmax.pth"
    response.headers["filename"] = "softmax.pth"
    return response


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
