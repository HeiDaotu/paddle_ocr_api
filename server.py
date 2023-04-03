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
    return result


def get_text_json(text):
    text_dict = {}

    for line in text:
        line_rep = line.replace('\'', '')
        index = line_rep.index(', ')
        var_dict_before = line_rep[:index]
        var_dict_after = line_rep[index + 2:]
        text_dict[var_dict_before] = var_dict_after
    return text_dict


@app.post("/ocr")
async def ocr_api(request):
    # 获取文件流转bytes
    result = get_ocr_json(request.files.get("img").body)

    json_str = get_text_json(result)
    return json(json_str)
