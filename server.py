from paddleocr import PaddleOCR
from sanic import Sanic
from sanic.response import json
import re

app = Sanic("ocr_api")


def get_ocr_json(img):
    # 模型路径下必须含有model和params文件，如果没有，现在可以自动下载了，不过是最简单的模型
    # use_gpu 如果paddle是GPU版本请设置为 True
    ocr = PaddleOCR(use_angle_cls=True, use_gpu=False)

    resultStr = ocr.ocr(img, cls=False).__str__()

    result = re.findall(r'\((.*?)\)', resultStr)

    for line in result:
        print(line)
    return result


def get_text_json(text):
    json_str = []

    for line in text:
        line = line.replace(', ', ':')
        json_str.append(line)

    json_str = json_str.__str__().replace('"', '').replace('[', '{').replace(']', '}')
    return json_str


@app.post("/ocr")
async def ocr_api(request):
    # 获取文件流转bytes
    result = get_ocr_json(request.files.get("img").body)

    json_str = get_text_json(result)
    return json(json_str)
