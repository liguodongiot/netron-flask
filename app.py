import logging
from flask import Flask, render_template, request, Response
from pathlib import Path

app = Flask(__name__, static_url_path='/', )
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
file_type_list = [".onnx", ".pb", ".meta", ".tflite", ".lite",
                  ".tfl", ".keras", ".h5", ".hd5", ".hdf5", ".json", ".model", ".mar",
                  ".params", ".param", ".armnn", ".mnn", ".ncnn", ".tnnproto", ".tmfile", ".ms", ".nn",
                  ".uff", ".rknn", ".xmodel", ".paddle", ".pdmodel", ".pdparams", ".dnn", ".cmf", ".mlmodel",
                  ".caffemodel", ".pbtxt", ".prototxt", ".pkl", ".pt", ".pth",
                  ".t7", ".joblib", ".cfg", ".xml", ".zip", ".tar"
                  ]


@app.route('/downloadfile', methods=['GET'])
def downloadfile():
    store_path = request.args.get('modelFile')
    logging.info(f"model download path: {store_path}")
    # 流式读取
    def send_file():
        with open(store_path, 'rb') as targetfile:
            while 1:
                data = targetfile.read(20 * 1024 * 1024)  # 每次读取20M
                if not data:
                    break
                yield data

    path = Path(store_path)
    model_name = path.name
    response = Response(send_file(), content_type='application/octet-stream')
    response.headers["Content-disposition"] = 'attachment; filename=%s' % model_name
    response.headers["filename"] = model_name
    return response


@app.route('/', methods=["GET"])
def index():
    model_file = request.args.get('modelFile')
    if model_file is None or model_file == '':
        model_file = "./squeezenet1.0-3.onnx"

    logging.info(f"model file path: {model_file}")
    path = Path(model_file)
    model_file_suffix = path.suffix
    if not (path.exists() and path.is_file()):
        logging.info("模型文件不存在")
        return render_template('error.html')

    if model_file_suffix not in file_type_list:
        logging.info("不支持该格式文件")
        return render_template('error.html')
    return render_template('index.html', model_file=model_file)


if __name__ == '__main__':
    app.run()
