# netron-flask（netron模型可视化工具的Flask版本）
netron原生模型可视化，需要启动应用，然后通过浏览器选择文件，如果想要集成到其他项目之中，交互流程较长，
本项目通过http请求方式传入模型路径即可完成可视化，便于集成到其他项目之中。



## 执行步骤
```bash
# 安装依赖包
pip install -r requirements.txt

# 启动应用
python app.py
```

## 验证模型可视化

打开浏览器，输入`http://127.0.0.1:5000/`，可查看默认模型文件可视化。

如果想打开其他模型进行可视化，则传入模型文件路径，如下所示：
```http
http://127.0.0.1:5000/?modelFile=/Users/lgd/temp/softmax.pth
```
