from flask import Flask
from flask import request
import logging
import server as netron
import urllib.request
import _thread

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s')

port = 9000


# 为线程定义一个函数
def netron_app(port):
    result = netron.start('/Users/liguodong/temp/softmax.pth', address=('localhost', port), browse=False, log=False)
    logging.info(f"{result}")

@app.route('/start')
def start():
    global port
    port += 1
    try:
        _thread.start_new_thread(netron_app, (port,))
    except:
        print("Error: 无法启动线程")
    return str(port)


@app.route('/', methods=["GET"])
def open():
    ports = request.args.get('ports')
    logging.info(f"get input: {ports}")
    resp=urllib.request.urlopen("http://localhost:"+str(ports))
    the_page = resp.read()
    return the_page


if __name__ == '__main__':
    app.run()

