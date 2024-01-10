from flask import Flask, jsonify, request, redirect
import time
import ssl
import os

app = Flask(__name__)
port = 443

# 证书和私钥文件路径
cert_path = os.path.join(os.path.dirname(__file__), 'mykey.crt')
key_path = os.path.join(os.path.dirname(__file__), 'mykey.key')

# 创建SSL上下文
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(certfile=cert_path, keyfile=key_path)


# 自定义中间件
@app.before_request
def print_request_params():
    # 打印请求参数
    print("请求路径:", request.path)
    print("请求方法:", request.method)
    print("请求参数:", request.args)


@app.route('/csrfToken', methods=['GET'])
def get_csrf_token():
    response_data = {
        '_csrf': 'Tbs6hIVo--Ngb_G9VJ3lnoMR1EYRnQli5bEY'
    }
    return jsonify(response_data)


@app.route('/api/v1/config', methods=['GET'])
def get_config():
    response_data = {
        'wl': '0a4fd5d5accf385b8d5f382d7abcfea7'
    }
    return jsonify(response_data)


####-------文档路径----####
@app.route('/docs')
def redirect_to_docs():
    return redirect("https://www.joysboy.com/docs/v8/", code=302)


####-------返回的账号信息----####
@app.route('/api/v1/account', methods=['GET'])
def get_account():
    current_timestamp = int(time.time() * 1000)
    response_data = {
        'id': '6131f76468e4553fba39ae4c',
        'now': current_timestamp,
        'emailAddress': '社区论坛:Https://JoySboy.com',
        'fullName': '『掌玩小子』公众号',
        'paidServices': {
            'v8': {
                'expires': current_timestamp + 1000000
            }
        },
        'permissions': {}
    }
    return jsonify(response_data)


####-------验证----####
@app.route('/static/legal/version.json', methods=['GET'])
def get_version():
    response_data = {
        'version': 20240211,
        'wording': 'AutojsPro\n阅读%s和%s全文了解详细信\n请点击“同意”继续接受我们的服务。'
    }
    return jsonify(response_data)


@app.route('/api/v1/security/validation2', methods=['GET', 'POST', 'PUT', 'DELETE'])
def post_validation():
    response_data = {
        "data": "uNl8AK0WM6mIAQAAM9bHGgAAAACaX4kztI8jdDdMKBwYbba4oNAKCHba0nRgN7zXoP0IzjEyM2NjZjgzMmFiZTg5OGYAAQAAAAAAAAAyWsXfnWpHYVlJ4ZPT/u3n+ZH3NLvubrTRJnas08r0ijocgKnKqCxTFvJgeZnWx2omp6CzeSFWEG8aEaarJ4XMkp9+F8sdy2yFkqkOrp41KmCfShbIQX4hCYeD0mVOOwfOVLpQLJjg18FvFvHm9TKYzK5ysfv9UHuHn8+dexgnLM28j5BDrIFv9B9XS+UW1x/lLAwe+QzBEAWzsYFKPkVJ9Mc0L5lG/i8Eh7bxcGHIg1L+VbC4t9+CZXcF6DOoy75I40omuQs/gtbLCsMEr7fdsiDQ76iukr1SwLHVIEaXrNutrvvqKp+UBcq4WGQEM+aMj46S3pd7+h17J8vKdTVknI2IOJPZM2mVjGCQ3MBriG5HQqghbFE3y/VEPWpmtkgjDXqc09vuYA4PLxnV1AbvoAEvy8FgqxY00MXANK2MMixzZorUIC2Jk1hBLgPYHd1lMPlAMt8Deab3KZ0sJNLMo/7tAzk50DrPse3onAg5oA5QTSDfKBI2AtZP+DmPYrtsa96iUFK9iz8/18Pnhw/GBd+ceDR00dpQRVGjqTFxftAtZFr9kFYXTfz94+uq/fnVlH4eDGQiNAvuPg/4nQLXlde3lDYp5loaN2MkjL4uK9m8uQjH68217L195jsXANSo8IKjJYqWzcA1oCF/Smnmwc03k0Uk5OcfunIF/AGJ1g=="
    }
    return jsonify(response_data)


@app.route('/docs/documentation.json', methods=['GET'])
def get_documentation():
    response_data = {
        'documentation_version': 20221024
    }
    return jsonify(response_data)


@app.route('/api/v1/announcements', methods=['GET'])
def get_announcements():
    response_data = {}
    return jsonify(response_data)


@app.route('/api/v1/plugins', methods=['GET'])
def get_plugins():
    plugins = [
        {
            "package_name": "org.autojs.plugin.ffmpeg",
            "name": "官方FFMpeg插件",
            "version": "1.1",
            "version_code": 1,
            "summary": "FFmpeg是一套可以用来记录、转换数字音频、视频，并能将其转化为流的开源计算机程序。本插件用于利用ffmpeg处理音视频文件，比如从格式转换等。",
            "icon": "https://www.joysboy.com/docs/assets/image/ffmpeg-plugin.png",
            "url": "https://www.joysboy.com/docs/blog/ffmpeg-plugin.html",
            "installed": False,
            "update_timestamp": 0
        },
        {
            "package_name": "org.autojs.autojspro.plugin.mlkit.ocr",
            "name": "官方MLKitOCR插件",
            "version": "1.1",
            "version_code": 1,
            "summary": "基于谷歌MLKit，识别速度超过绝大部分OCR。",
            "icon": "https://www.joysboy.com/docs/assets/image/mlkit-ocr-plugin.png",
            "url": "https://www.joysboy.com/docs/blog/mlkit-ocr-plugin.html",
            "installed": False,
            "update_timestamp": 0
        },
        {
            "package_name": "cn.lzx284.p7zip",
            "name": "7Zip通用压缩插件",
            "version": "1.2.1",
            "version_code": 4,
            "summary": "本插件基于p7zip 16.02制作，支持多种格式文件的压缩与解压。7-Zip是一款完全免费而且开源的压缩软件，相比其他软件有更高的压缩比但同时耗费的资源也相对更多，能提供比使用 PKZip 及 WinZip 高2~10%的压缩比率。",
            "icon": "https://www.joysboy.com/docs/assets/image/7zip-plugin.png",
            "url": "https://www.joysboy.com/docs/blog/7zip-plugin.html",
            "documentation_url": "https://www.joysboy.com/docs/blog/7zip-plugin.html",
            "installed": False,
            "update_timestamp": 0
        },
        {
            "package_name": "com.hraps.pytorch",
            "name": "Pytorch插件",
            "version": "1.0.0",
            "version_code": 1,
            "summary": "Pytorch模块提供了已完成的深度学习神经网络模型在安卓设备上执行的功能，可以实现常规程序难以实现的功能，如：图像识别，语言翻译，语言问答等。",
            "icon": "https://www.joysboy.com/docs/assets/image/pytorch-logo.png",
            "url": "https://www.joysboy.com/docs/v8/thirdPartyPlugins.html",
            "documentation_url": "https://www.joysboy.com/docs/v8/thirdPartyPlugins.html#pytorch插件",
            "installed": False,
            "update_timestamp": 0
        },
        {
            "package_name": "org.autojs.autojspro.ocr.v2",
            "name": "PaddleOCR",
            "version": "1.3",
            "version_code": 1,
            "summary": "PaddleOCR",
            "icon": "",
            "url": "",
            "documentation_url": "",
            "installed": False,
            "update_timestamp": 0
        }
    ]
    return jsonify(plugins)


@app.route('/api/v1/project', methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_project():
    response_data = [{
        "packageName": "com.ninedays.a.b",
        "file": "http://pcdn.autojs.org/projects/migrated/97beef80-d1d7-4812-8000-c91bd4e03007.zip",
        "name": "下拉框高度更改",
        "permissions": [],
        "version": "2.69",
        "versionCode": 1,
        "minSdkVersion": 0,
        "contacts": {},
        "summary": "花了两天研究改下拉框高度",
        "details": "有更好的更改方法告诉我一下2307136635",
        "images": [],
        "releaseNotes": {},
        "maxAutoJsVersion": 0,
        "minAutoJsVersion": 0,
        "minProVersion": 0,
        "maxProVersion": 0,
        "compileVersion": "Pro 9.1.20-0",
        "category": "模块",
        "tags": [],
        "status": 0,
        "fileSize": 1556,
        "user": {
            "id": "62a57ee9879b9e3dbb07a9b0",
            "emailAddress": "wm_v@qq.com",
            "fullName": "九天"
        },
        "upvoted": False,
        "upvotedCount": 0,
        "id": "6309b505f9e3cc1848d963bb"
    }, {
        "packageName": "来一局TicTacToe?",
        "file": "http://pcdn.autojs.org/projects/migrated/4494cd62-73bb-445f-8317-7723e3ed7548.zip",
        "name": "人机井字棋对弈",
        "permissions": [],
        "version": "1.0.0",
        "versionCode": 0,
        "minSdkVersion": 0,
        "contacts": {},
        "summary": "井字棋人机对弈",
        "details": "权值算法计算最优解",
        "images": [],
        "releaseNotes": {},
        "maxAutoJsVersion": 0,
        "minAutoJsVersion": 0,
        "minProVersion": 0,
        "maxProVersion": 0,
        "compileVersion": "Pro 9.1.19-0",
        "category": "其他",
        "tags": [],
        "status": 0,
        "fileSize": 3525,
        "user": {
            "id": "5e426df225fbe26cc58cacc0",
            "emailAddress": "418740992@qq.com",
            "fullName": "楚轩"
        },
        "upvoted": False,
        "upvotedCount": 0,
        "id": "62fba096874d234d9ee41ece"
    }
    ]
    return jsonify(response_data)


@app.route('/api/v1/project/categories', methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_project_categories():
    response_data = ["官方示例", "模块", "系统工具", "实用工具", "学习教育", "软件辅助", "游戏辅助", "游戏", "其他"]
    return jsonify(response_data)


# https://pro.autojs.org/api/v1/project/tags
@app.route('/api/v1/project/tags', methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_project_tags():
    response_data = ["精品", "官方", "UI"]
    return jsonify(response_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, ssl_context=ssl_context)
