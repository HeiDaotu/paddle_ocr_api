FROM python:3.10.9

# 设置工作目录，即cd命令
WORKDIR /paddle_ocr_api

COPY ./ ./

# 安装一些重要的包

RUN pip install Sanic -i https://mirror.baidu.com/pypi/simple
RUN pip install PaddleOCR -i https://mirror.baidu.com/pypi/simple
RUN pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

EXPOSE 8000

# 镜像运行时执行的命令，这里的配置等于 EXPOS server.app
CMD ["sanic","server.app","--host=0.0.0.0","--port=8000"]