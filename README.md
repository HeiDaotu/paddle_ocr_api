# paddle_ocr_api

>  这是一个OCR接口，里面内置了sanic框架和paddleocr框架，可以通过http直接请求接口，传图片File文件，然后返回识别的json信息。

默认端口是 `8000` ，调用接口示例：`http://localhost:8000/ocr` ，请求 `post` 请求。

## 本地运行项目

### 环境

+ python：conda3.10   这边建议安装conda虚拟环境

### 依赖

+ 安装Sanic： ` pip install Sanic -i https://mirror.baidu.com/pypi/simple` 
+ 安装飞浆OCR： `pip install PaddleOCR -i https://mirror.baidu.com/pypi/simple` 
+ 安装飞浆：`pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple`

### 运行

在命令行输入 `sanic server.app` ，即可。

![image-20230406110707799](https://fastly.jsdelivr.net/gh/HeiDaotu/img-bucket/img/202304061107692.png)

## Docker运行项目（推荐）

运行Docker，没有镜像会自动拉取镜像在运行的，默认端口是8000，需要改外面暴露的端口，请讲排在前面的8000修改为你需要的端口，第一次运行可能会比较慢，因为没有模型，需要自动下载最新的模型，后续速度就正常了。

```bash
docker run -itd --name paddle_ocr_api -p 8000:8000 wufeihdt/paddle_ocr_api
```

## request请求

表单传输 `File` 类型，传输名为 `img`。

```bash
curl -X POST -F 'img=@xxx.png' http://localhost:8000/ocr
```

## response响应

`json` 类型，`key:`识别名字，`value:`识别的可信度，越高越好。

```json
{
    "3": "0.984226405620575",
    "BT1207-好用的磁力链接搜索引擎": "0.951934278011322",
    "window版本下载镜像网站": "0.9146453142166138",
    "10749": "0.9955421686172485",
    "视频网": "0.9975712895393372",
    "公司项目地址": "0.997933566570282",
    "是科": "0.9960678815841675",
    "业务管理": "0.8964824676513672",
    "又或": "0.7516067028045654",
    "资源立": "0.8773576617240906",
    "Portainer": "0.9844127297401428",
    "学习资料": "0.9976288080215454",
    "在线工具": "0.975907564163208",
    "Birthday Ideas for 10-year-old": "0.9278088212013245",
    "其他收藏夹": "0.9727570414543152"
}
```

## 演示图片

![image-20230406103232422](https://fastly.jsdelivr.net/gh/HeiDaotu/img-bucket/img/202304061035857.png)